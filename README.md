English | [中文](./README_ZH.md)

<h3 align="center"><img src="Assets/logo.png" height="64"><br>AppWielder: Allow users to manipulate your app with natural
language</h3>

<div align="center">

[![](https://img.shields.io/badge/python-3.9+-blue)](https://pypi.org/project/agentscope/)
[![](https://img.shields.io/badge/Docs-English%7C%E4%B8%AD%E6%96%87-blue?logo=markdown)](https://modelscope.github.io/agentscope/#welcome-to-agentscope-tutorial-hub)
[![](https://img.shields.io/badge/license-Apache--2.0-black)](./LICENSE)
[![](https://img.shields.io/badge/Contribute-Welcome-green)](https://modelscope.github.io/agentscope/tutorial/contribute.html)

[//]: # ([![]&#40;https://img.shields.io/github/stars/gencay/vscode-chatgpt?color=blue&label=Github%20Stars&#41;]&#40;&#41;)

</div>

## 新闻

- <img src="https://img.alicdn.com/imgextra/i3/O1CN01SFL0Gu26nrQBFKXFR_!!6000000007707-2-tps-500-500.png" alt="new" width="30" height="30"/>**[2024-06-27]**
  Based on **AppWielder**, we have developed a Visual Studio Code plugin, [SmarterVscode](), which allows users to manipulate
  various VsCode features through natural language commands, such as changing the theme or generating code with a single
  sentence. [Learn more](https://modelscope.github.io/agentscope/zh_CN/tutorial/302-contribute.html#vscode-plugin) -
- <img src="https://img.alicdn.com/imgextra/i3/O1CN01SFL0Gu26nrQBFKXFR_!!6000000007707-2-tps-500-500.png" alt="new" width="30" height="30"/>**[2024-06-27]**
  We are thrilled to announce the release of **AppWielder** version 1.0!

---

## What is AppWielder?

AppWielder is an innovative API orchestration framework built upon Large Language Models (LLMs) and Agents.
It aims to integrate and synchronize APIs provided by any applications (APPs) using the advanced reasoning capabilities of LLMs.

- AppWielder allows applications to respond and execute instructions formulated in natural language, significantly simplifying
  user interaction with applications.

<img src="Assets/function.png" width=1000>

> The above image illustrates how AppWielder enhances application interactivity.
> Specifically, the graphic is divided into two parts: the left-half details the traditional process of inquiry and execution when
> completing tasks, while the right-half displays the streamlined workflow with AppWielder's intervention.
> In a traditional scenario, when a user needs to accomplish a task in an app but doesn’t know how to do it, they first ask the
> LLM and receive an answer, then command the app to obtain the result and complete the task.
> In contrast, after introducing AppWielder, the user simply inputs their requirement in natural language directly into the app to
> get the result and finish the task. With AppWielder's assistance, the app consults the LLM for user intent and learns the
> necessary commands to execute, subsequently returning the result.

- Any application vendor only needs to implement communication interfaces on the app and submit a list of supported APIs to
  AppWielder, which can independently explore and identify the optimal API call sequence to fulfill user instructions.

AppWielder 's core competency lies in its highly automated API orchestration logic and user-friendly data interaction patterns,
making it easier and faster for developers to add intelligent features to their apps.
It also comes with a flexible HTTP interface that enhances the way applications work together.
In the end, AppWielder aims to provide a straightforward and efficient way for users and developers to interact with apps,
enabling a seamless experience that meets diverse needs.

🔥 **Enhanced Usability**: Allows users to control your application via simple natural language commands, eliminating the need to learn complex interfaces or command sets and making the services or content readily accessible.

🛠️ **Easy Integration**: Developers only need to register their application's API directory, and AppWielder will automatically manage the identification and orchestration, negating the need for intricate coding.

🚀 **Asynchronous and Concurrent Processing**: AppWielder enhances its support for concurrent requests using modern asynchronous technology, ensuring efficiency and quick responses even under high-load conditions with multiple users or tasks.

🌐 **Robust API Interactions**: AppWielder offers a stable and user-friendly HTTP API interface, enabling seamless interactions with applications while ensuring high-efficiency and security in data transfer.

🤖 **Multitude of Large Language Models**: AppWielder integrates well with various Large Language Models, allowing developers to choose the most suitable model based on their needs and contexts for optimal understanding and natural language processing.

📚 **Comprehensive Documentation**: AppWielder provides extensive documentation, including quick start guides, API references, best practice examples, and FAQs, to help developers get started and fully utilize the framework.

💾 **Persistent Task Flows**: Task workflows can be stored persistently in databases, facilitating the monitoring and management of tasks and allowing developers to check the status and history at any time.

🛢️ **Smart Caching Mechanism**: With advanced caching technology, AppWielder optimizes performance and response times by intelligently storing frequently requested results, reducing the number of calls to external models (coming soon).

🌟 **Token Optimization**: AppWielder's optimization algorithm intelligently assesses message utility, reducing token usage and cutting down on costs associated with API calls (coming soon).

## Applications: The SmarterVscode Plugin Based on AppWielder

We developed a Visual Studio Code plugin, [SmarterVscode](), that allows users to operate various VsCode features through natural language. Below are some demonstrations of its features:

### Tic-tac-toe Game

https://github.com/alibaba/pilotscope/assets/31238100/eef9765a-8cda-4654-a147-475ed1a13c58

### Style Changing

https://github.com/alibaba/pilotscope/assets/31238100/18480837-b90f-44d6-8c28-d5f17a4552da

### Theme Changing

https://github.com/alibaba/pilotscope/assets/31238100/2a8cd2fd-22df-4ba0-a564-90cad6c708bb

### Enable auto saving

https://github.com/alibaba/pilotscope/assets/31238100/77548e8a-2832-4770-8924-ea479646e3a8

## Connect to your Application

The following image illustrates the process of introducing intelligence into applications using the AppWielder framework,
detailing the tasks that application developers need to undertake and the process by which AppWielder independently orchestrates
API calls to fulfill user instructions.

<img src="Assets/developer.png" width=1000>

#### Preparation Stage:

1. **Communication interface**: Application developers need to achieve a **standard communication interface** with the AppWielder.
2. **Document**: They also need to provide soe **knowledge** to the AppWielder, including the app's available API documentation
   and other optional documents.

#### Deploy stage

After starting AppWielder, the app forwards user input to the AppWielder. The AppWielder integrates user input and available API
information, interacts with the LLM to select the appropriate API to execute, and determine the task status. Iteratively, the app
executes the selected API and returns the execution result to the AppWielder. The AppWielder continues to interact with the LLM to
make the next decision. The pipeline is terminated when the task has been completed, or failed, and the result is returned to the
user.

After completing these steps, the app can achieve intelligent interaction with users.

## Documentation

[Documentation](https://modelscope.github.io/agentscope/#welcome-to-agentscope-tutorial-hub)
provides comprehensive information on how to integrate AppWielder into your application. You can refer to these documents for an improved experience with AppWielder.

## License
AppWielder is released under the Apache License 2.0.

## Contributions
Join us in building AppWielder!
Please see our [Contribution Guide](https://modelscope.github.io/agentscope/zh_CN/tutorial/302-contribute.html) for more detail