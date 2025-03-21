from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.chains import RetrievalQA
 
 
embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
)
 
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)
 
 
persisted_vectore_store = FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)
 
prompt_template = """
Human: Use the following pieces of context to provide a
concise answer to the question at the end but use at least summarize with
250 words with detailed explanations. If you don't know the answer,
just say that you don't know, don't try to make up an answer.
<context>
{context}
</context>
 
Question: {question}
 
Assistant:"""
 
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
 
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=persisted_vectore_store.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
answer = qa({"query": "give me aswika linkedin"})
 
print(answer['result'])
 