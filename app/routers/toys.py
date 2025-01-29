from fastapi import APIRouter

router = APIRouter(prefix="/toys")

@router.get("/")
def get_toys() -> None:
    pass

@router.get("/{name}")
def get_toy(name: str) -> None:
    pass

@router.post("/")
def add_toy() -> None:
    pass

@router.put("/{name}")
def update_toy(name: str) -> None:
    pass

@router.delete("/{name}")
def delete_toy(name: str) -> None:
    pass