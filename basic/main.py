from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

llm = ChatOllama(
    model="deepseek-r1",
    temperature=0,
)

messages = [
    (
        "system",
        "You are expert in identifying gibberish words in a sentence. If a sentence contains gibberish return response as 'Not eligible'",
    ),
    ("human", "good morning"),
]
ai_msg = llm.invoke(messages)

print("\nresult \n",ai_msg)

print("\nresult ",ai_msg.content)