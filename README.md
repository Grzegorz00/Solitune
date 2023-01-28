# Solitune
This app is designed to use machine learning algorithms to classificate the future of employees, based on "Employee" dataset, predicting if they will stay or leave current working place. It does this by analyzing a dataset that contains information about the employees, such as their education, joining year, gender, payment tier and experience. The app is built using a combination of technologies, including the programming language Python, the data pipeline framework Kedro, and the containerization technology Docker. These technologies work together to allow for efficient data processing and model training, as well as easy deployment and scaling of the app. Overall, the app could help organizations make better decisions about employee management and development, by providing them with predictions about employee performance and behavior.

Example implementation and dataset can be found here: 
https://www.kaggle.com/datasets/tejashvi14/employee-future-prediction
## Team
***Bagniuk Karol*** - Data Scientist\
***Misior Dominik*** - ML Engineer\
***Ołdakowski Maciej*** - Project manager\
***Stasiak Zuzanna*** - ML Engineer\
***Święcicki Grzegorz*** - Coder and System Architect\
***Sadownik Michał*** - Coder and Data Scientist

## Useful links 

[Data versioning(DVC)](https://dvc.org/doc/start)

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
In this project, the Wandb, Optuna, and PyCaret libraries were used to optimize, evaluate, and deploy machine learning models.

Wandb, or Weights and Biases, was used to track the performance of the models during training, as well as to store and visualize the results. This allowed the team to monitor the progress of the models in real-time and to quickly identify any issues or areas for improvement. Additionally, Wandb provides useful features such as hyperparameter tuning, and model comparison which can be useful in this project.

Optuna was used to perform hyperparameter optimization on the models. This is a technique that involves automatically searching for the best values for the parameters of the model, such as the learning rate or number of neurons in a neural network, in order to improve its performance. Optuna uses a variety of optimization algorithms and techniques to explore the parameter space and identify the best combination of values for the specific problem.

PyCaret was used to simplify the model selection and deployment process. PyCaret is a library that provides a high-level interface for several machine learning libraries, including scikit-learn, XGBoost, and LightGBM. It also provides a variety of useful features such as automated machine learning, model comparison and model interpretability. PyCaret allows the team to quickly test different models and select the best one for the task at hand, as well as to easily deploy the final model in a production environment.

## Docker
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. It allows the team to work on the project on diffrent machines without a need to constantly fixing the environment. It also allows easly to test the app with wirtual environments.
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
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It cames with build-in swagger, which is perfect for testing. What is more kedro pipelines can be implementent into FastAPI app. That allows team to work more efficiently.  
To run type:
```
uvicorn scr/solitune/main:app --reload
```
 Then you go and check an automatic interactive API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)
