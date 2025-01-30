from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field, BeforeValidator, AfterValidator
from app.models import TagModel
from app.dependencies.utils import tag_exists


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

def capitalize_toy_name(name: str) -> str:
    return name.capitalize()


class ToyBaseSchema(BaseModel):
    price: int = Field(gt=0)
    tags: Annotated[list[str], BeforeValidator(convert_tag_models_to_tag_names)]

class ToySchema(ToyBaseSchema):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

    name: Annotated[str, AfterValidator(capitalize_toy_name)]

class ToyUpdateFields(ToyBaseSchema):
    pass