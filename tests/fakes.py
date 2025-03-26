from langchain_core.language_models import BaseLanguageModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import Generation, LLMResult
from typing import Any, List, Optional
from langchain_core.runnables import RunnableConfig
from langchain_core.embeddings import Embeddings


class FakeLLM(BaseLanguageModel):
    def _call(self, prompt: str, **kwargs: Any) -> str:
        return "mocked result"

    def invoke(self, input: Any, config: RunnableConfig = None) -> AIMessage:
        return AIMessage(content="mocked result")

    @property
    def _llm_type(self) -> str:
        return "fake"

    # Required for LangChain internal usage
    def predict(self, text: str, **kwargs: Any) -> str:
        return "mocked result"

    def generate_prompt(
        self, prompts: List[str], stop: Optional[List[str]] = None, **kwargs
    ) -> LLMResult:
        generations = [[Generation(text="mocked result") for _ in prompts]]
        return LLMResult(generations=generations)

    def predict_messages(self, messages, **kwargs):
        return AIMessage(content="mocked result")

    def generate(
        self, prompts: List[str], stop: Optional[List[str]] = None, **kwargs
    ) -> LLMResult:
        generations = [[Generation(text="mocked result") for _ in prompts]]
        return LLMResult(generations=generations)

    # Async versions
    async def apredict(self, text: str, **kwargs: Any) -> str:
        return self.predict(text, **kwargs)

    async def agenerate_prompt(
        self, prompts: List[str], stop: Optional[List[str]] = None, **kwargs
    ) -> LLMResult:
        return self.generate_prompt(prompts, stop, **kwargs)

    async def apredict_messages(self, messages, **kwargs):
        return self.predict_messages(messages, **kwargs)


class FakeEmbeddings(Embeddings):
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [[0.0] * 384 for _ in texts]

    def embed_query(self, text: str) -> List[float]:
        return [0.0] * 384
