"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import encode_categorical_values,reorder_dataset


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=encode_categorical_values, inputs="employee", outputs="employee_encoded"),
        node(func=reorder_dataset, inputs="employee_encoded", outputs="employee_prepared"),
    ])
