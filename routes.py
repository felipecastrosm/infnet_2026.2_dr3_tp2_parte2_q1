from fastapi import APIRouter

from models import ChatRequest, ChatResponse, MessageResponse, QuestionsResponse
from services import get_answer, get_predefined_questions

router = APIRouter()


@router.get("/", response_model=MessageResponse)
def home():
    return MessageResponse(message="Fake LLM Chatbot API is running")


@router.get("/questions", response_model=QuestionsResponse)
def questions():
    return QuestionsResponse(questions=get_predefined_questions())


@router.post("/chat", response_model=ChatResponse)
def chat(data: ChatRequest):
    return ChatResponse(message=data.message, answer=get_answer(data.message))
