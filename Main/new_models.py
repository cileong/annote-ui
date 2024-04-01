### HOIDTC Data Model ###

import io
import collections.abc

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_validator,
    model_serializer,
)


class PromptGranularityFlags(BaseModel):

    """
    A part-prompt is granular if it is more specific.
    e.g. "man wearing a red shirt" instead of "human".
    """

    model_config = ConfigDict(frozen=True, populate_by_name=True)

    human: bool
    object_: bool = Field(alias="object")
    interaction: bool


class Prompt(BaseModel):

    model_config = ConfigDict(
        str_to_lower=True,
        str_strip_whitespace=True,
        str_min_length=1,
        frozen=True,
        populate_by_name=True,
    )

    human: str
    object_: str = Field(alias="object")
    interaction: str
    is_granular: PromptGranularityFlags


class Bbox(BaseModel):

    model_config = ConfigDict(frozen=True)

    x0: float = Field(ge=0)
    y0: float = Field(ge=0)
    x1: float = Field(ge=0)
    y1: float = Field(ge=0)

    @model_validator(mode="after")
    def p1_ge_p2(self) -> "Bbox":
        if self.x0 > self.x1 or self.y0 > self.y1:
            raise ValueError(f"invalid bbox: {(self.x0, self.y0)} > {(self.x1, self.y1)}")
        return self

    @model_serializer()
    def serialize_model(self) -> list[float]:
        return [self.x0, self.y0, self.x1, self.y1]


class Annotation(BaseModel):

    model_config = ConfigDict(frozen=True)

    annotation_id: int = Field(ge=0)
    image_filename: str
    object_id: int = Field(ge=0)
    prompt: Prompt
    bbox_human: list[Bbox]
    bbox_object: list[Bbox]


class Dataset(collections.abc.Sequence, BaseModel):

    model_config = ConfigDict(frozen=True)

    annotations: list[Annotation]
    
    @staticmethod
    def from_file(fp: io.TextIOBase) -> "Dataset":
        data = f'{{ "annotations": {fp.read()} }}'
        return Dataset.model_validate_json(data)

    @model_serializer()
    def serialize_model(self) -> list[Annotation]:
        return self.annotations
    
    def __getitem__(self, index: int) -> Annotation:
        return self.annotations[index]

    def __len__(self) -> int:
        return len(self.annotations)
