from typing import Annotated
from fastapi import Depends, HTTPException
from app.dependencies.utils import tag_exists


def name_in_lowercase(name: str) -> str:
    return name.lower()

def vacant_tag_name(name: Annotated[str, Depends(name_in_lowercase)]) -> str:
    if tag_exists(name):
        raise HTTPException(status_code=409, detail="Tag with provided name already exists")
    return name

def existing_tag_name(name: Annotated[str, Depends(name_in_lowercase)]) -> str:
    if not tag_exists(name):
        raise HTTPException(status_code=404, detail="Tag with provided name doesn't exist")
    return name