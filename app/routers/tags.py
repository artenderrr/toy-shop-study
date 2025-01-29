from fastapi import APIRouter

router = APIRouter(prefix="/tags")

@router.get("/")
def get_tags() -> None:
    pass

@router.post("/{name}")
def add_tag(name: str) -> None:
    pass

@router.delete("/{name}")
def delete_tag(name: str) -> None:
    pass