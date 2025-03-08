from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate

# Define the LLM
llm = ChatOllama(
    model="deepseek-r1",
    temperature=0,
)

# Define a simple tool
@tool
def check_gibberish(text: str) -> str:
    """Check if the given text contains gibberish words."""
    return "Use this tool to analyze if text contains gibberish words"

# Create the agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are expert in identifying gibberish words in a sentence. If a sentence contains gibberish return response as 'Not eligible'"),
    ("human", "{input}")
])

agent = create_react_agent(
    llm=llm,
    tools=[check_gibberish],
    prompt=prompt
)

# Run the agent
result = agent.invoke({"input": "good morning"})
print("\nresult:", result)