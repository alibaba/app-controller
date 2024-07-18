#!/bin/bash

# Start the ssh service
/usr/sbin/sshd -D

# start server
conda activate ${PYTHON_ENV_NAME}
python server.py -p ${SERVER_PORT}