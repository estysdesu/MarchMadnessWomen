#!/bin/bash

# Shell command to start docker for project
docker run --rm -p 8888:8888 -v "$PWD":/home/jovyan/work estysdesu/jupyter-data-science