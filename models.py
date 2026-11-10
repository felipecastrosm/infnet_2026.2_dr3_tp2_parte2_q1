from pydantic import BaseModel, ConfigDict, Field


class MessageResponse(BaseModel):
    message: str


class ChatRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    message: str = Field(min_length=1, max_length=500, examples=["What is LangChain?"])


class ChatResponse(BaseModel):
    message: str
    answer: str


class QuestionsResponse(BaseModel):
    questions: list[str]
