from kedro.framework.session import KedroSession
from pathlib import Path
from typing import Any, Iterable
from kedro.pipeline import Pipeline
from fastapi import Depends, FastAPI
from kedro.framework.context import KedroContext
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from solitune.dependencies.dependencies import encode_categorical_pipeline
from solitune.routers import data_processing


app = FastAPI()
app.include_router(data_processing.router, prefix="/data_processing")

def get_session() -> Iterable[KedroSession]:
    bootstrap_project(Path().cwd())
    with KedroSession.create() as session:
        yield session

def get_context(session: KedroSession = Depends(get_session)) -> Iterable[KedroContext]:
    context = session.load_context()
    session.load_context = lambda: context
    yield context

@app.get("/")
def main(pipeline: Pipeline = Depends(encode_categorical_pipeline)) -> dict[str, str]:
    print(pipeline)
    return {"message": "Hello World!"}



