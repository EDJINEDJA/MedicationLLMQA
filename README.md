<p align="center">
    <a href="https://www.python.org/doc/" alt="Python 3.7">
        <img src="https://img.shields.io/badge/python-v3.7+-blue.svg" />
    </a>
    <a href="https://github.com/EDJINEDJA/MedicationLLMQA/blob/main/LICENSE" alt="Licence">
        <img src="https://img.shields.io/badge/license-MIT-yellow.svg" />
    </a>
    <a href="https://github.com/EDJINEDJA/MedicationLLMQA" alt="Activity">
        <img src="https://img.shields.io/badge/contributions-welcome-orange.svg" />
    </a>
    <a href="http://matthaythornthwaite.pythonanywhere.com/" alt="Web Status">
        <img src="https://img.shields.io/website?down_color=red&down_message=down&up_color=success&up_message=up&url=http%3A%2F%2Fmatthaythornthwaite.pythonanywhere.com%2F" />
    </a>
</p>


## Table of Contents

<!--ts-->
* [Aims and Objectives](#Aims-and-Objectives)
* [What LLM](#llm)
* [Usage](#Usage)

<!--te-->

## Aims and Objectives

MedicationLLMQA is a question-answering system specifically designed to assist physicians in their medical practices. It allows physicians to inquire about appropriate medications for a specific disease or set of symptoms.

## What llm
A large language model is a type of artificial intelligence algorithm that has been trained on vast amounts of text data, allowing it to generate human-like language output. These models are designed to process and understand natural language input, such as text or speech, and generate appropriate responses.

Large language models use deep learning techniques, such as neural networks, to analyze and understand patterns in language data. They are trained on massive datasets, often consisting of billions of words, in order to develop an understanding of the complexities and nuances of human language.

Some examples of large language models include GPT-3, BERT, and Transformer-XL. These models are used in a variety of applications, including natural language processing, chatbots, language translation, and more. 

# Usage

#### Install

- git clone 

Clone this repository in the main folder of your project to use MedicationLLMQA
```bash
$ git clone https://github.com/EDJINEDJA/MedicationLLMQA.git
```
- set you OpenAI API_KEY

Create new file .env inside env in the root folder
Inside put in variable  API_KEY you API_KEY
```bash
$ API_KEY = ""
```
- requirements

The toolkit support Python 3.10.6 

To install required packages use:

```bash
$ pip3 install -r requirements.txt
```
run app.py to get started:

```bash
$  python app.py --config config.yaml
```
