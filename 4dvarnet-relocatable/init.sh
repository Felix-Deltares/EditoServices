#!/bin/bash

# kill process if anything fails
set -e

$EnvName = "jupyter_env"
$EnvFile = "https://github.com/Deltares-research/EditoServices/blob/main/4dvarnet-relocatable/environment_reduced.yaml"

#Write-Host "Updating conda environment from $EnvFile"
conda env update -f $EnvFile

Write-Host "Activating environment $EnvName"
conda activate $EnvName

wget https://raw.githubusercontent.com/Deltares-research/EditoServices/main/4dvarnet-relocatable/4DVarNet_NorthSea_workflow.ipynb
