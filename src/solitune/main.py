from kedro.framework.session import KedroSession
from pathlib import Path
from typing import Any, Iterable
from fastapi import Depends, FastAPI
from kedro.framework.context import KedroContext
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from kedro.pipeline import Pipeline
from src.solitune.pipelines.data_preparation import create_pipeline

app = FastAPI()

def get_session() -> Iterable[KedroSession]:
    bootstrap_project(Path().cwd())
    with KedroSession.create() as session:
        yield session

def get_context(session: KedroSession = Depends(get_session)) -> Iterable[KedroContext]:
    context = session.load_context()
    session.load_context = lambda: context
    yield context

def create_variance_pipeline() -> Iterable[Pipeline]:
    yield create_pipeline()

@app.get("/")
def main(pipeline: Pipeline = Depends(create_variance_pipeline)) -> dict[str, str]:
    print(pipeline)
    return {"message": "Hello World!"}



