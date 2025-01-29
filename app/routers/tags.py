from typing import Annotated
from fastapi import APIRouter, Depends
from app.services import TagService
from app.dependencies import vacant_tag_name, existing_tag_name


router = APIRouter(prefix="/tags")


@router.get("/")
def get_tags() -> list[str]:
    tags = TagService.get_all()
    return tags

@router.post("/{name}", status_code=201)
def add_tag(name: Annotated[str, Depends(vacant_tag_name)]) -> list[str]:
    TagService.add(name)
    return [name]

@router.delete("/{name}", status_code=204)
def delete_tag(name: Annotated[str, Depends(existing_tag_name)]) -> None:
    TagService.delete(name)