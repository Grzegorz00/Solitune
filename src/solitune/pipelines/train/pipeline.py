"""
This is a boilerplate pipeline 'train'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=train_model, inputs=None, outputs="classifier"),
    ])
