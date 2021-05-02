FROM continuumio/miniconda3

# Update the environment
RUN apt-get update -y; apt-get upgrade -y

# Install VIM
RUN apt-get install -y vim-tiny vim-athena ssh

# Create a user to run the project
RUN adduser --home /home/flask flask
USER flask
WORKDIR /home/flask

# Create a working directory
RUN mkdir -p flask_app
WORKDIR /home/flask/flask_app

# Setup a python environment and install dependencies
COPY requirements.txt requirements.txt
# RUN conda create --name flask-app python=3
# RUN conda activate flask-app
RUN pip install -r requirements.txt
RUN echo "alias l='ls -lah'" >> ~/.bashrc

RUN echo "source activate flask-app" >> ~/.bashrc

# This is the equivalent of running `source activate`
# Its handy to have in case you want to run additional commands in the Dockerfile
ENV CONDA_EXE /opt/conda/bin/conda
ENV CONDA_PREFIX /home/flask/.conda/envs/flask-app
ENV CONDA_PYTHON_EXE /opt/conda/bin/python
ENV CONDA_PROMPT_MODIFIER (flask-app)
ENV CONDA_DEFAULT_ENV flask-app
ENV PATH /home/flask/.conda/envs/flask-app/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin