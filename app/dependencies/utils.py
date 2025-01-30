from app.database import Session
from app.models import TagModel, ToyModel

def tag_exists(name: str) -> bool:
    with Session() as session:
        if session.get(TagModel, name):
            return True
    return False

def toy_exists(name: str) -> bool:
    with Session() as session:
        if session.get(ToyModel, name):
            return True
    return False