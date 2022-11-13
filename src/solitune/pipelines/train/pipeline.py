"""
This is a boilerplate pipeline 'train'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import prepare_data_for_modeling, split_data, train_model, evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
                func=prepare_data_for_modeling,
                inputs="customers_labeled",
                outputs="data_prepared_for_modeling",
                name="prepare_data_node",
            ),
            node(
                func=split_data,
                inputs="data_prepared_for_modeling",
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="classifier",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["classifier", "X_test", "y_test"],
                outputs=None,
                name="evaluate_model_node",
            ),
    ])
