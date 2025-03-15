from langchain_ollama import ChatOllama
from langchain_community.agent_toolkits import FileManagementToolkit
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool
from tools import DocxFileLoad
 
#LLM
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)
 
# Tools
file_tool = FileManagementToolkit(
    #current working directory
    root_dir=str(os.getcwd()),
    selected_tools=["read_file","file_search"],
).get_tools()
 
 
tools = file_tool + [DocxFileLoad()]
 
#Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are best in answering questions related to the file content. "
        "Search the file by file_search tool and read the content by read_file tool."
        "Use docx_file_load tool to read the content of docx file"
        ""
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)
 
 
#Agent
agent = create_tool_calling_agent(llm, tools, prompt)
 
 
#Executor
agent_executor = AgentExecutor(agent=agent,tools=tools,return_intermediate_steps=True)
 
#Run
result=agent_executor.invoke({"input": "What is the M.A (Tamil) of passing in SureshResume.docx  present in this directory?"})
 
 
 
print(result)
 