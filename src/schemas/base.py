from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

__all__ = [
    "DTO",
]


class DTO(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        populate_by_name=True,
        use_enum_values=True,
        from_attributes=True,
        alias_generator=to_camel,
        allow_inf_nan=False,
        ser_json_timedelta="float",
        ser_json_bytes="utf8",
        validate_default=True,
        validate_return=True,
        regex_engine="python-re",
    )
