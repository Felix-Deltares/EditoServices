#!/bin/bash

# kill process if anything fails
set -e

ENV_NAME=4dvarnet-relocatable-model
ENV_FILE=https://github.com/Deltares-research/EditoServices/blob/main/4dvarnet-relocatable/environment_reduced.yaml

echo "▶ Updating conda environment from ${ENV_FILE}"
conda env update -f ${ENV_FILE}

echo "▶ Activating environment ${ENV_NAME}"
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate ${ENV_NAME}

# clear output
# jupyter nbconvert --clear-output --inplace modelbuilder_example.ipynb
# extend modelbuilder notebook, creates modelbuilder_example_edito.ipynb
# wget https://raw.githubusercontent.com/Deltares-research/EditoServices/main/modelbuilder/extend_modelbuilder_notebook.py
# python extend_modelbuilder_notebook.py
# remove redundant files
# rm modelbuilder_example.ipynb
# rm extend_modelbuilder_notebook.py
