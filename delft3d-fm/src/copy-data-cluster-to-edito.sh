#! /bin/bash
echo "Current working directory: ${PWD}"
USER=delt550999
cd "/home/delt/$USER/from-edito" || echo "Error: could not change to the directory /home/delt/$USER/from-edito" && exit 1
scp -r $USER@glogin1.bsc.es:dflowfm/ results/
