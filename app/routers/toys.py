from typing import Annotated
from fastapi import APIRouter, Depends
from app.schemas import ToySchema
from app.services import ToyService
from app.dependencies.toys import existing_toy_name, toy_with_vacant_name


router = APIRouter(prefix="/toys")


@router.get("/")
def get_toys() -> list[ToySchema]:
    toys = ToyService.get_all()
    return toys

@router.get("/{name}")
def get_toy(name: Annotated[str, Depends(existing_toy_name)]) -> ToySchema:
    toy = ToyService.get(name)
    return toy

@router.post("/", status_code=201)
def add_toy(toy: Annotated[ToySchema, Depends(toy_with_vacant_name)]) -> ToySchema:
    ToyService.add(toy)
    return toy

@router.put("/{name}")
def update_toy(name: str) -> None:
    pass

@router.delete("/{name}", status_code=204)
def delete_toy(name: Annotated[str, Depends(existing_toy_name)]) -> None:
    ToyService.delete(name)