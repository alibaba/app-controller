(installation-en)=

# Installation

To install App-Controller, you need to have Python 3.9 or higher installed. We recommend setting up a new virtual environment
specifically for App-Controller:

## Create a Virtual Environment

### Using Conda

If you're using Conda as your package and environment management tool, you can create a new virtual environment with Python 3.9
using the following commands:

```bash
# Create a new virtual environment named 'App-Controller' with Python 3.9
conda create -n App-Controller python=3.9

# Activate the virtual environment
conda activate App-Controller
```

## Installing App-Controller from Source

In order to facilitate the connection with your application, you should install App-Controller directly from the source code, follow
these steps to clone the repository and install the platform in editable mode:

**_Note: This project is under active development, it's recommended to install AgentScope from source._**

```bash
# Pull the source code from Github
git clone https://github.com/modelscope/agentscope.git
cd App-Controller

# Install the required dependencies
pip install -r requirements.txt
```

[[Return to the top]](#installation-en)
