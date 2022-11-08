"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import prepare_data_for_modeling, load_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=load_data, inputs=None, outputs="df"),
        node(func=prepare_data_for_modeling, inputs="dataset", outputs="prepared_data"),
    ])
