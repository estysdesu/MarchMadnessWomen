FROM jupyter/minimal-notebook:latest

RUN python3 -m pip install numpy pandas scipy sklearn chartify
