# LLM Documentation Framework: FARLLID

This GitHub project started as the practical side of my creation of FARLLID, an automatic documentation generation tool that creates documentation for entire repositories using LLM and ANTLR language parsing. It works for C++ and Java, but with ANTLR parsing, it can easily be extended to more languages.  FARLLID was created as part of my Master's Thesis, but will continue as a hobby project. 

## Prerequisites 

Before you can run the program, you need to pip install the dependencies that are located in `requirements.txt` 

```
pip3 install -r requirements.txt
```

Ollama is used for local model usage, so it must be installed and configured before you run it (https://ollama.com/download/).  

Then you must ensure that you set the variables listed in the `.env.example` file in your environment. In particular: 

CAPGEMINI_API_KEY=
USE_LOCAL_LLM=True
PROVIDE_CONTEXT=True
PROVIDE_CODE=True
REPOSITORY_PATH=/home/$USER/Documents/astro
MODEL_PROVIDER=azure 
MODEL_NAME=openai.gpt-4o

Where the repository path points towards a C++ or Java repo to be documented. 

## Run configurations

There are certain methods of running the program: 

`Python3 main.py -d` -> Creates the AST and Documentation 

`Python3 main.py -d -w` -> Creates the AST and Documentation and also runs the website after

`Python3 main.py -w` -> Runs the website (has as a requirement that the documentation is already present). 
