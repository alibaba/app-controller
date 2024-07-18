# Use Ubuntu 18.04 as base image
FROM ubuntu:18.04

# Set enviroment variables for llm4api service
ARG OPENAI_BASE_URL
ARG OPENAI_API_KEY
ARG SERVER_PORT=5000

ARG PROJECT_PATH=/usr/local/bin
ENV PYTHON_ENV_NAME=app-controller

ENV OPENAI_BASE_URL=${OPENAI_BASE_URL}
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Set environment to non-interactive to avoid any prompts during the build process
ENV DEBIAN_FRONTEND=noninteractive
    
RUN apt-get update && \
    apt-get install -y \
    gcc \
    openssh-server \
    git \
    vim \
    sudo \
    wget

# Configuration for SSH (optional step if you need to enable SSH)
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN mkdir /var/run/sshd

# Install Miniconda
ENV CONDA_DIR=/root/miniconda3
RUN mkdir -p ${CONDA_DIR} && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ${CONDA_DIR}/miniconda.sh && \
    bash ${CONDA_DIR}/miniconda.sh -b -u -p ${CONDA_DIR} && \
    rm -rf ${CONDA_DIR}/miniconda.sh 

RUN ${CONDA_DIR}/bin/conda init

RUN ${CONDA_DIR}/bin/conda create --name ${PYTHON_ENV_NAME} python=3.10

# Install llm4api service 
RUN git -c http.sslVerify=false clone --depth 1 --branch master https://github.com/alibaba/app-controller.git ${PROJECT_PATH}

# Install libraries
RUN source ${CONDA_DIR}/bin/activate ${PYTHON_ENV_NAME} && \
    cd ${PROJECT_PATH} && \
    pip install -r requirement.txt

# 复制启动脚本到镜像中
COPY entrypoint.sh ${PROJECT_PATH}/entrypoint.sh

# 设置ENTRYPOINT来执行启动脚本
ENTRYPOINT ["${PROJECT_PATH}/entrypoint.sh"]