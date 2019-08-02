FROM jupyter/scipy-notebook:latest

RUN pip install --upgrade pip && pip install PyAthena