# Solitune
This app will predict employee future based on "Employee" dataset. 
Example implementation can be found here: 
https://www.kaggle.com/datasets/tejashvi14/employee-future-prediction
## Team
***Bagniuk Karol*** - Data Scientist\
***Misior Dominik*** - ML Engineer\
***Ołdakowski Maciej*** - Project manager\
***Stasiak Zuzanna*** - ML Engineer\
***Święcicki Grzegorz*** - Coder and System Architect\
***Sadownik Michał*** - Coder and Data Scientist

## Useful commends and links 

[Data versioning](https://dvc.org/doc/start)

[kedro documentation](https://kedro.readthedocs.io)

[Anaconda](https://anaconda.org/)

[Git commends](https://docs.github.com/en/get-started/using-git/about-git)

[Docker](https://docs.docker.com/get-started/overview/)

[Wandb](https://docs.wandb.ai/)

[Optuna](https://optuna.readthedocs.io/en/stable/index.html)

[PyCaret](https://pycaret.readthedocs.io/en/latest/index.html)

[FastAPI](https://fastapi.tiangolo.com/)

## How to use DVC

Adding and commiting changes:
```
dvc add data/01_raw/employee.csv 
git commit data/01_raw/employee.csv.dvc -m "<message>"
```

Pushing changes:
```
dvc push
git push
```

To get status of the dataset:
```
dvc status
git status
```

To pull data from server:
```
git pull
dvc pull
```

[DVC user guide](https://dvc.org/doc/user-guide/how-to/update-tracked-data)

## Overview

This is a employee future prediction project based on "Employee" dataset. It was generated using Kedro, Docker and RestAPI. All the information about the data you can find in JupyterNotebook file in notebooks directory.

## How to install dependencies

To install packages run: `conda install --file requirements.txt -n name-of-environment`
or: `pip install -r requirements.txt`

## Kedro
Kedro is an open source Python workflow tool that allows you to create portable data science pipelines.
You can run your Kedro project with:

```
kedro run
```
All piplines are in src/solitune/pipelines/ directory.
There are three ready piplines:
- data_preparation
- train
- train_pycaret
To run specific pipline, or choosen nodes use:
```
kedro run --pipeline pipline_name
kedro run --node node_name,node_name_2
```

You can also see a project structure using:
```
kedro viz
```
This command automatically opens a browser tab to serve the visualisation at http://127.0.0.1:4141/.

All documentation conected to kedro pipelines can be accessed by:
```
kedro build-docs --open
```
## Project dependencies

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.

## WandadB, Optuna, Pycaret
This project used WandadB for experiment tracking. It is easy to use and for anyone it allows to share results with colleagues and their future self.
Optuna is an open source hyperparameter optimization framework to automate hyperparameter search.
PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows.

## Docker
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.
To run docker file type:
```
docker build -t solitune_doc
```
Then you can use `docker image` to check all docker images. To run image use:
```
docker run solitune_doc
```
Then you can call `docker ps -a` to all the running and exited containers. To access type:
```
docker exec -it solitune_doc bash
```
You can stop the container using: `docker stop solitune_doc` or kill it: `docker kill solitune_doc`

## FastAPI and Uvicorn
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
To run type:
```
uvicorn scr/solitune/main:app --reload
```
 Then you go and check an automatic interactive API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)
