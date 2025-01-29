from sqlalchemy import select
from app.database import Session
from app.models import TagModel, ToyModel
from app.schemas import ToySchema


class TagService:
    @staticmethod
    def get_all() -> list[str]:
        with Session() as session:
            models = session.execute(select(TagModel)).scalars()
            tags = [model.name for model in models]
        return tags
    
    @staticmethod
    def add(name: str) -> None:
        with Session() as session:
            model = TagModel(name=name)
            session.add(model)
            session.commit()

    @staticmethod
    def delete(name: str) -> None:
        with Session() as session:
            model = session.get(TagModel, name)
            session.delete(model)
            session.commit()

class ToyService:
    @staticmethod
    def get_all() -> list[ToySchema]:
        with Session() as session:
            models = session.execute(select(ToyModel)).scalars()
            toys = [ToySchema.model_validate(model) for model in models]
        return toys
    
    @staticmethod
    def get(name: str) -> ToySchema:
        with Session() as session:
            model = session.get(ToyModel, name)
            toy = ToySchema.model_validate(model)
        return toy