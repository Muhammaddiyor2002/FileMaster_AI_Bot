from pydantic import BaseModel, Field


class ConvertRequest(BaseModel):
    source_path: str
    target_format: str


class CompressRequest(BaseModel):
    source_path: str


class MergeRequest(BaseModel):
    source_paths: list[str] = Field(min_length=2)


class SummaryRequest(BaseModel):
    text: str


class TranslateRequest(BaseModel):
    text: str
    target_lang: str = "uz"
