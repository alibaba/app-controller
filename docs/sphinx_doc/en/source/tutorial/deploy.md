(deploy-en)=

# Deploy

In this tutorial, we will illustrate the process of introducing intelligence into applications using the App-Controller framework,
including how to add necessaries knowledge to the App-Controller and how to deploy the App-Controller to achieve intelligent
interaction
with users.

## Step1: Data Preparation

First, you need to provide some **knowledge** to the App-Controller, including the app's available API documentation
and other optional documents.

You should create a directory structure for submitting your knowledge(MetaData) to App-Controller as follows.
Note that the `UserData` and `Index` are generated by the App-Controller, so you only need to provide the `MetaData` directory.

```bash
Your application name
├── MetaData
│   ├── Apis                                        # Describing the API information of the application.
│   │   ├── Apis_1.json                             # The first group of APIs.
│   │   ├── ...                   
│   │   ├── Apis_k.json                             # The k-th group of APIs.
│   ├── KnowledgeApi_custom_folder_name             # Knowledge for the first special API. (Optional)
│   │   ├── config.json                             # The configuration file for the special KnowledgeApi.
│   │   ├── KnowledgeFile_1.json                    # The document for the special KnowledgeApi. 
│   ├── KnowledgeApi_custom_folder_name             # Knowledge for k-th special KnowledgeApi. (Optional)
├── Index                                           # The automatically generated index file for Apis and other knowledge.
│   ├── embedding_model_name                        # The index from first embedding model.
│   │   ├── Apis                                    # The index for Apis. 
│   │   ├── KnowledgeApi_custom_folder_name         # The index for the certain specific KnowledgeApi.
│   ├── embedding_model_name2                       # The index from second embedding model.
│   ├── ...
├── UserData                                        # It is generated by the App-Controller to record the user's input and reasoning process
```

### Prepare API Documentation

You must provide available API information for your application. The API information should be stored in the `Apis` directory.
All files in the directory should be a `.json` file and each file can contain multiple APIs. In general, You can organize the API
with similar functions into one file.

Typically, a file can be organized as below.

```json5
{
  "api_name": {
    "name": "api_name",
    "description": "A detailed description of the API function. More detailed information will improve the performance.",
    "parameters": {
      "type": "object",
      "properties": {
        "argument_name_1": {
          "type": "type for argument_name_1, such as string, list, boolean, object, etc.",
          "description": "A detailed description of argument_name_1, including the capability and range of value."
        }
        // the rest of the argument with the same json format
      },
      //The required field is used to specify the required parameters for the API.
      "required": [
        "argument_name_1"
      ]
    }
  },
  // the rest of the APIs with the same json format
}
```

Once the App-Controller is started, it will automatically search all the `.json` files in the `Apis` directory and build index for
each API.
The index file will be stored in the `Index` directory.

Note that, App-Controller will automatically update index file when any api is added or updated to the `Apis` directory.
However, App-Controller will not update the index file when any api is deleted from the `Apis` directory. In this case, you need
to
manually all the index file related to api in the `Index` directory.

### Prepare KnowledgeAPI Documentation

In general, there are some special APIs that can achieve various functions. For example, a special api called "setSetting(key:
str, value: str)" can be used to change the various setting of the application by filling different parameters. We call such api
as KnowledgeAPI.
We design a `KnowledgeApi` mechanism for providing more detailed information for the parameters of KnowledgeAPI.

Specifically, for each user task, we will explore whether the user's input can be fulfilled by the
KnowledgeApi with specific parameters. If the user's input can be fulfilled by the KnowledgeApi, the App-Controller will return
the
KnowledgeApi to fulfill the user's input.

You can create any `KnowledgeApi_customm_folder_name` directory prefixed with `KnowledgeApi_` to provide the knowledge for the
special API and the directory should be organized as below.

```bash
│   KnowledgeApi_customm_folder_name                # Knowledge for the first special API. (Optional)
│   ├── config.json                                 # The configuration file for the special API.
│   ├── knowledge_folder                            # Knowledge folder for KnowledgeApi
│   │   ├── knowledge1.json                         # Knowledge file
│   ├── knowledge2.json                             # Knowledge file
```

It includes a necessary `config.json` and the `knowledge` file recording the information for this special API.
All `knowledge` file can be saved in the anywhere under the folder `KnowledgeApi_customm_folder_name`.

#### Config file

A config file is used to specify the information of the special API. The config file should be organized as below.

```json5
{
  "special_api_name": {
    "name": "special_api_name",
    "description": "A detailed description of the API function. More detailed information will improve the performance.",
    "parameters": {
      "type": "object",
      "properties": {
        "argument_name_1": {
          "type": "type for argument_name_1, such as string, list, boolean, object, etc.",
          "description": "A detailed description of argument_name_1, including the capability and range of value."
        }
        // the rest of the argument with the same json format
      },
      //The required field is used to specify the required parameters for the API.
      "required": [
        "argument_name_1"
      ]
    }
  },
  // the number of candidate knowledge item for index search. 
  "retrieve_size": 10,
  // the Advanced or Lightweight level for the chat model. 
  "chatModelLevel": "Lightweight"
}
```

#### Knowledge file

The file includes a list of knowledge item. Each item use a json format to record the
information and include the `id`, `desc`, and `example`(optional) field.

- `id`: The unique identifier for the knowledge item, such as the name of the setting.
- `desc`: A detailed description of the knowledge item.
- `example(optional)`: An example of the knowledge item. You should provide enough information here such that LLM can learn how to
  utilize this knowledge item to fill with the parameters of the special API.

A example of knowledge file about VsCode should be organized as below.

```json5
[
  {
    "id": "editor.fontSize",
    "desc": " Controls the font size in pixels.",
    "example": {
      "editor.fontSize": 14
    }
  },
  {
    "id": "editor.tokenColorCustomizations",
    "desc": " Overrides editor syntax colors and font style from the currently selected color theme.",
    "example": {
      "editor.tokenColorCustomizations": {
        "comments": "#808080"
      }
    }
  }
]
```

Once the App-Controller is started, it will automatically build knowledge index for each knowledgeApi independently by searching
all
the directories prefixed with `KnowledgeApi_`.

Then, for each knowledgeApi, App-Controller will automatically search all the `knowledge` files in
the `KnowledgeApi_custom_folder_name` and read config file.
Each knowledge item will be indexed independently and the index file will be stored in the `Index` directory.

Similarly, App-Controller will automatically update index file when any knowledge item is added or updated.
However, App-Controller will not update the index file when any item is deleted . In this case, you need to manually all the index
file in the `Index` directory.

## Step2: Communication Interface Implementation

App-Controller offers a robust HTTP-interface for applications to seamlessly communicate with its services. Below you will find
the
detailed descriptions of the interface's endpoints, ensuring smooth interaction between your application and the App-Controller
platform.

### Start Endpoint

**Endpoint**: `/start`

**Method**: `POST`

**Purpose**:
Submit the user input to the App-Controller system to initiate pipeline of scheduler.

**RequestBody**:
JSON object.

**Request Example**:

```json5
{
  "userId": "The unique identifier for the user engaging with the system.",
  "sessionId": "A unique identifier for the current session. Each user input should be assigned a new sessionId",
  "content": "The user input",
  "chat_model_config": "Configuration settings for the chat model that drives dialogue or messaging interactions.",
  "embedding_model_config": "Configuration settings for the embedding model used to process or understand the content.",
  "environments": {
    "The description of first environment": "the value of first environment",
    // the rest of the environment with the same json format
  }
}
```

**Response**:
Please refer to the [Response](#endpoint-response) section for more details.

---

### HandleApiResponse Endpoint

**Endpoint**: `/handleApiResponse`

**Method**: `POST`

**Purpose**:
Submit the execution result to the App-Controller system.

**RequestBody**:
JSON object.

**Request Example**:

```json5
{
  // return the original response from the App-Controller with extra parameter "result" for each api.
  "status": "Task_Api_Call",
  "data": {
    "apis": [
      {
        "name": "the name of the api",
        "arguments": {
          "argument1 name": "value or list or object",
          "argument2 name": "value or list or object",
          // the rest of the argument with the same json format
        },
        // extra parameter
        "result": "the result of the api call, including whether the api call is successful or not. The error message if the api call is failed."
      }
    ]
  },
  "isTerminal": "true or false using boolean type",
}
```

**Response**:
Please refer to the [Response](#endpoint-response) section for more details.

---

### Finish Endpoint

**Endpoint**: `/finish`

**Method**: `POST`

**Purpose**:
Inform the App-Controller system that the task has been completed.
It is only called when the App-Controller returns the `Task_Api_Call` response with `isTerminal` set to `true` and the api call is
successful.

**RequestBody**:
JSON object.

**Request Example**:

```json5
{
  "userId": "The unique identifier for the user engaging with the system.",
  "sessionId": "A unique identifier for the current session. Each user input should be assigned a new sessionId",
}
```

**Response**:
Please refer to the [Response](#endpoint-response) section for more details.

---

### Cancel Endpoint

**Endpoint**: `/cancel`

**Method**: `POST`

**Purpose**:
Inform the App-Controller system that the task has been cancelled. The task will be stopped directly.

**RequestBody**:
JSON object.

**Request Example**:

```json5
{
  "userId": "The unique identifier for the user engaging with the system.",
  "sessionId": "A unique identifier for the current session. Each user input should be assigned a new sessionId",
}
```

**Response**:

Please refer to the [Response](#deploy) section for more details.

---

### Endpoint Response

In general, the App-Controller will return the following several responses, including `Task_Api_Call`,`Task_Failed`
,`Task_Finished`
,`Task_Cancelled`,`Task_Exception`,`Task_Question`.

#### Task_Api_Call

The response will be returned when the App-Controller needs to call the API to fulfill the user's input.

```json5
{
  // Indicate the status of the response.
  "status": "Task_Api_Call",
  // 
  "data": {
    "apis": [
      {
        "name": "the name of the api",
        "arguments": {
          "argument1 name": "value or list or object",
          "argument2 name": "value or list or object",
          // the rest of the argument with the same json format
        }
      }
    ]
  },
  "isTerminal": "true or false using boolean type",
}
```

- `apis`: return the list of api that need to be sequentially called to fulfill the user's input. Each api includes the `name`
  and `arguments`.
- `isTerminal`: `true` mean the task has been completed directly after the api is successfully called, `false` mean the task has
  not been completed after the api is successfully called, the interaction will continue.

#### Task_Finished

The response will be returned when the App-Controller consider the task has been completed.

```json5
{
  "status": "Task_Finished"
}
```

Note that, App-Controller use two ways to notify the task has been completed. One is to return the `Task_Finished` response with
the
close of the session context, the other is to return the `Task_Api_Call` response with `isTerminal` set to `true`. However, the
task will continue if the api call is failed.

#### Task_Failed

The response will be returned when the App-Controller consider the task cannot be completed.

```json5
{
  "status": "Task_Failed"
}
```

#### Task_Cancelled

The response will be returned when you send request to App-Controller with a session_id that has been stopped.

```json5
{
  "status": "Task_Cancelled"
}
```

#### Task_Exception

The response will be returned when there are any exceptions during the task processing. The task will be stopped directly.

```json5
{
  "status": "Task_Exception"
}
```

#### Task_Question

The response will be returned when the App-Controller consider the input as a question instead of a task.

```json5
{
  "status": "Task_Question",
}
```

## Step3: Configuration your App-Controller

### Embedding Model Configuration

App-Controller need to use two types of model, including the chat model and the embedding model. These models need api key to be
called.
In our system, the user of your application need to provide api keys of two types model. In addition, the developer of application
need to provide the api key of the embedding model for pre-building the index.

- **Chat model**: It is used to reason the suitable API for the user's input. All users of your application need to send api key
  of selected chat model to the App-Controller. Then, the chat model will be called by the api key.
- **Embedding model**: For developer of application, you need to provide the api key of the embedding model for pre-building the
  index on available apis and other knowledge. For user of your application, the api key of the embedding model will be used to
  embed the user's input for searching the most similar knowledge.

You can configure your embedding model by modifying the `embed_model_config` file.
It supports multiple embedding models. Each embedding model will build index for all apis and knowledge independently.
Each config of embed model should refer to  [Model Config](https://modelscope.github.io/agentscope/en/tutorial/203-model.html)

For example, you can configure the embedding model of openai as below.

```json5
[
  {
    "config_name": "openai_embedding_config",
    "model_type": "openai_embedding",
    "model_name": "{model_name}",
    "api_key": "{your_api_key}",
    "organization": "{your_organization}",
    "client_args": {
      // e.g. "max_retries": 3,
    },
    "generate_args": {
      // e.g. "encoding_format": "float"
    }
  }
]
```

### Basic Configuration

You can configure the App-Controller by modifying the `config.ini` file.
There are several important parameters that you need to pay attention to.

```ini
[App]
; Application name
app = visual studio code
; the path of the app data directory, which is used to store the "MetaData","Index","UserData" and others.
app_data_dir = /Users/wlg/Documents/alibaba/llm4apis/LLM_For_APIs/AppSupports/SmartVscodeExtension/

; Model settings
[Models]
; build index for these embedding models separately
; enabled_embed_models = openai_embedding_config:text-embedding-3-small,qwen_embedding_config:text-embedding-v2
enabled_embed_models = openai_embedding_config:text-embedding-3-small

; Server configuration
[Server]
http_port = 5000
```

- app: The name of the application.
- app_data_dir: The path of the app data directory, which is used to store the "MetaData","Index","UserData" and others.
- enabled_embed_models: The index are dependent on the embedding model. You can specify multiple embedding models separated by
  `,`. Each embedding model should be organized as `model_orgnization_name:embedding_model_name`. All indexes will build for each
  embedding model separately.
- http_port: The port of the App-Controller server.
  More details about the configuration file can be found in the `config.ini` file.

[[Return to the top]](#103-start-en)