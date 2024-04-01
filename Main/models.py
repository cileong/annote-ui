from typing_extensions import Annotated

from pydantic import (
    BaseModel,
    Field,
    AfterValidator,
    model_validator,
    field_validator,
    model_serializer,
)


def _to_lower(v: str) -> str:
    """ Convenience function """
    return v.lower()


class Bbox(BaseModel):
    x0: float = Field(ge=0)
    y0: float = Field(ge=0)
    x1: float = Field(le=1)
    y1: float = Field(le=1)

    @model_validator(mode="after")
    def verify_p1_ge_p0(self) -> "Bbox":
        if self.x1 <= self.x0 or self.y1 <= self.y0:
            raise ValueError(
                f"(x1, y1) must be greater than or equal to (x0, y0), but received {[(self.x0, self.y0), (self.x1, self.y1)]}."
            )
        return self


class Annotation(BaseModel):
    image_filename: str
    object_id: int = Field(ge=0)
    caption_all: list[Annotated[str, AfterValidator(_to_lower)]]
    caption_full: Annotated[str, AfterValidator(_to_lower)]
    caption_masked: list[Annotated[str, AfterValidator(_to_lower)]]
    bbox_human: list[Bbox]
    bbox_object: list[Bbox]

    @field_validator("caption_all")
    @classmethod
    def verify_caption_all_length(cls, v: list[str]) -> list[str]:
        if len(v) != 7:
            raise ValueError(f"caption_all must have length 7, but received {len(v)}.")
        return v

    @field_validator("caption_masked")
    @classmethod
    def verify_caption_masked_length(cls, v: list[str]) -> list[str]:
        if len(v) != 6:
            raise ValueError(
                f"caption_masked must have length 6, but received {len(v)}."
            )
        return v

    @model_validator(mode="after")
    def verify_bbox_list_length(self) -> "Annotation":
        if len(self.bbox_human) != len(self.bbox_object):
            raise ValueError(
                f"bbox_human and bbox_object must have equal length, but received {len(self.bbox_human)} != {len(self.bbox_object)}"
            )
        return self


class Dataset(BaseModel):
    annotations: list[Annotation]

    @model_serializer()
    def serialize_model(self) -> list[Annotation]:
        """ Use array as the top-level data structure. """
        return self.annotations
