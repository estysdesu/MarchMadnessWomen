FROM jupyter/minimal-notebook:latest

RUN conda upgrade -q -y notebook jupyterhub jupyterlab

RUN python3 -m pip -q install numpy pandas scipy sklearn chartify



