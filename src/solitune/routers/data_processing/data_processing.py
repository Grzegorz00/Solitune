from fastapi import APIRouter, Depends
from kedro.pipeline import Pipeline
from solitune.dependencies.dependencies import encode_categorical_pipeline, reorder_dataset_pipeline
from kedro.io import DataCatalog
from kedro.runner import SequentialRunner
from typing import Any
from solitune.schemas.schemas import Employee

router = APIRouter()

@router.get("/")
def main(pipeline: Pipeline = Depends(encode_categorical_pipeline)) -> dict[str, Any]:
    runner = SequentialRunner()
    catalog = DataCatalog()
    return runner.run(pipeline=pipeline, catalog=catalog)

@router.post("/encode_categorical_values")
def encode_categorical_values(
    employee: list[Employee],
    pipeline: Pipeline = Depends(encode_categorical_pipeline)) -> list[Employee]:
    runner = SequentialRunner()
    catalog = DataCatalog(feed_dict={"employee": employee})
    return runner.run(pipeline=pipeline, catalog=catalog)["employee_encoded"]


@router.get("/reorder_dataset")
def reorder_dataset(
    pipeline: Pipeline = Depends(reorder_dataset_pipeline)) -> dict[str, Any]:
    runner = SequentialRunner()
    catalog = DataCatalog()
    return runner.run(pipeline=pipeline, catalog=catalog)