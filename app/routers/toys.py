from typing import Annotated
from fastapi import APIRouter, Depends
from app.schemas import ToySchema
from app.services import ToyService
from app.dependencies import existing_toy_name


router = APIRouter(prefix="/toys")


@router.get("/")
def get_toys() -> list[ToySchema]:
    toys = ToyService.get_all()
    return toys

@router.get("/{name}")
def get_toy(name: Annotated[str, Depends(existing_toy_name)]) -> ToySchema:
    toy = ToyService.get(name)
    return toy

@router.post("/")
def add_toy() -> None:
    pass

@router.put("/{name}")
def update_toy(name: str) -> None:
    pass

@router.delete("/{name}")
def delete_toy(name: str) -> None:
    pass