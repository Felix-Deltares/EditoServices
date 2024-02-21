import os
from pathlib import Path

import s3fs

from decoimpact.business.application import Application
from decoimpact.business.workflow.model_builder import ModelBuilder
from decoimpact.crosscutting.i_logger import ILogger
from decoimpact.crosscutting.logger_factory import LoggerFactory
from decoimpact.data.entities.data_access_layer import DataAccessLayer, IDataAccessLayer


# Create an file-system object for the s3 bucket
# | replace 'user-' 'oidc-'
USER_NAME = os.environ["USER_NAME"]
bucket_name = USER_NAME.replace("user-", "oidc-")
S3_ENDPOINT_URL = f"https://{os.environ['AWS_S3_ENDPOINT']}"
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_SESSION_TOKEN = os.environ["AWS_SESSION_TOKEN"]

fs = s3fs.S3FileSystem(
    client_kwargs={'endpoint_url': S3_ENDPOINT_URL},
    key=AWS_ACCESS_KEY_ID,
    secret=AWS_SECRET_ACCESS_KEY,
    token=AWS_SESSION_TOKEN
)
fs.ls(bucket_name)

yaml_file = os.environ["YAML_FILE_PATH"]
yaml_file_path = Path(yaml_file)

# download the yaml file
fs.download(f"{bucket_name}/{yaml_file}", yaml_file)

# configure logger and data-access layer for d-ecoimpact
logger: ILogger = LoggerFactory.create_logger()
da_layer: IDataAccessLayer = DataAccessLayer(logger)
model_builder = ModelBuilder(da_layer, logger)

# read the input (nc) and output (nc) path from the yaml input file
model_data = da_layer.read_input_file(yaml_file_path)
nc_file = str(model_data.datasets[0].path.relative_to(os.getcwd()))
output_file_path = str(model_data.output_path)

# download input netCDF (UGrid) file
fs.download(f"{bucket_name}/{nc_file}", nc_file)

# create and run d-ecoimpact application
application = Application(logger, da_layer, model_builder)
application.run(yaml_file_path)

# upload the output file to s3
fs.upload(output_file_path, f"{bucket_name}/{output_file_path}")
