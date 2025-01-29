from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field, BeforeValidator
from app.models import TagModel
from app.dependencies import tag_exists


def convert_tag_models_to_tag_names(tags: list[TagModel | str]) -> list[str]:
    if not isinstance(tags, list):
        raise ValueError("Tags should be represented as list")
    tag_names = []
    for tag in tags:
        if isinstance(tag, TagModel):
            tag_names.append(tag.name)
        elif isinstance(tag, str):
            if not tag_exists(tag):
                raise ValueError("Assigned tag doesn't exist")
            tag_names.append(tag)
    return tag_names


class ToySchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

    name: str
    price: int = Field(gt=0)

    tags: Annotated[list[str], BeforeValidator(convert_tag_models_to_tag_names)]