#!/bin/bash

# Start the ssh service
/usr/sbin/sshd -D

# start server
conda activate ${APP_CONTROLLER_PYTHON_NAME}

cd ${APP_CONTROLLER_PROJECT_PATH}
python server.py -p ${APP_CONTROLLER_SERVER_PORT}