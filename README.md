# Manual to run 

How to run this Python module will be described here. 

## Prerequisites 

Before you can run the program, you need to pip install the dependencies that are located in `requirements.txt` 

```
pip3 install -r requirements.txt
```

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
