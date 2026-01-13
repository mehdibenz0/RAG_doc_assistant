from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from core.config import settings
from core.exceptions import DocumentNotIndexedError

class RAGService:

    def __init__(self):
        self.qa_chain = None

    def initialize(self, vector_store):
        llm = ChatOpenAI(
            model=settings.LLM_MODEL,
            temperature=0
        )

        retriever = vector_store.as_retriever(
            search_kwargs={"k": settings.TOP_K_RETRIEVAL}
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=False
        )

    def ask(self, query: str) -> str:
        if self.qa_chain is None:
            raise DocumentNotIndexedError("No document indexed yet")

        return self.qa_chain(query)["result"]
