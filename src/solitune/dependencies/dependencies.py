from kedro.pipeline import Pipeline
from solitune.pipelines.data_preparation import create_pipeline
from typing import Iterable

def encode_categorical_pipeline() -> Iterable[Pipeline]:
    yield create_pipeline()

def reorder_dataset_pipeline() -> Iterable[Pipeline]:
    yield create_pipeline()
    
