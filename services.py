import re
from typing import Any

from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import FakeListLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

PREDEFINED_ANSWERS = {
    "hello": "Hello! I am a simple chatbot. How can I help you?",
    "what is your name": "My name is FakeBot, a chatbot powered by a Fake LLM.",
    "what is fastapi": "FastAPI is a modern and fast Python framework for building APIs.",
    "what is langchain": "LangChain is a framework for building applications powered by language models.",
    "what is a fake llm": "A Fake LLM returns predefined responses, which makes tests fast, free and deterministic.",
    "how can you help me": "I can answer a few predefined questions about FastAPI, LangChain and Fake LLMs.",
    "bye": "Goodbye! Have a nice day.",
}
DEFAULT_ANSWER = "Sorry, I don't know how to answer that yet. Try one of the predefined questions."


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", text.lower())).strip()


class PredefinedAnswersLLM(FakeListLLM):
    answers: dict[str, str]

    def _call(
        self,
        prompt: str,
        stop: list[str] | None = None,
        run_manager: CallbackManagerForLLMRun | None = None,
        **kwargs: Any,
    ) -> str:
        return self.answers.get(normalize(prompt), self.responses[0])


llm = PredefinedAnswersLLM(answers=PREDEFINED_ANSWERS, responses=[DEFAULT_ANSWER])
prompt = PromptTemplate.from_template("{message}")
chain = prompt | llm | StrOutputParser()


def get_answer(message: str) -> str:
    return chain.invoke({"message": message})


def get_predefined_questions() -> list[str]:
    return list(PREDEFINED_ANSWERS)
