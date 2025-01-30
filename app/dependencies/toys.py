from typing import Annotated
from fastapi import Depends, HTTPException
from app.schemas import ToySchema
from app.dependencies.utils import toy_exists


def name_capitalized(name: str) -> str:
    return name.capitalize()

def existing_toy_name(name: Annotated[str, Depends(name_capitalized)]) -> str:
    if not toy_exists(name):
        raise HTTPException(status_code=404, detail="Toy with provided name doesn't exist")
    return name

def toy_with_vacant_name(toy: ToySchema) -> ToySchema:
    if toy_exists(toy.name):
        raise HTTPException(status_code=409, detail="Toy with provided name already exists")
    return toy