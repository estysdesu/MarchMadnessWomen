#!/bin/bash

# open web browser
open /Applications/Safari.app

# Shell command to start docker for project
docker run --rm -it -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work estysdesu/jupyter-datasci

