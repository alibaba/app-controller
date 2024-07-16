# Use Ubuntu 18.04 as base image
FROM ubuntu:18.04

# Set enviroment variables for llm4api service
ARG OPENAI_BASE_URL
ARG OPENAI_API_KEY
ARG DASHSCOPE_API_KEY
ARG SERVER_PORT=5000

ENV OPENAI_BASE_URL=${OPENAI_BASE_URL}
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV DASHSCOPE_API_KEY=${DASHSCOPE_API_KEY}


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

RUN ${CONDA_DIR}/bin/conda create --name llm4api python=3.10

# Install llm4api service 
RUN git -c http.sslVerify=false clone --depth 1 --branch master https://github.com/alibaba/pilotscope.git /root/Llm4Api

# Install libraries
RUN source ${CONDA_DIR}/bin/activate llm4api && \
    cd /root/Llm4Api && \
    pip install -r requirement.txt

# Expose SSHD port (optional based on requirement)
EXPOSE 22

# Command to run SSH server (if SSH is necessary)
CMD ["/usr/sbin/sshd", "-D"]

# The default command to run a bash shell (Overwrite if needed)
CMD ["/bin/bash"]

# Start server
python server.py -p ${SERVER_PORT}