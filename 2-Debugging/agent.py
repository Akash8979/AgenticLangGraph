from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import END,START
from langgraph.graph.state import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import tools_condition
from IPython.display import Image,display
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ['LANGSMITH_TRACING'] = "true"
# os.environ['LANGSMITH_ENDPOINT'] = "https://api.smith.langchain.com"
LANGSMITH_PROJECT="TEST_PROJECT"

class State(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


llm = init_chat_model(model="openai/gpt-oss-120b",model_provider="groq")





def make_tool_graph():
    @tool
    def add(a:float,b:float):
        """Add Two numbers"""
        return a+b


    tools = [add]
    tool_node = ToolNode(tools)
    llm_with_tools = llm.bind_tools(tools)

    def call_llm_model(state:State):
        return {"messages":[llm_with_tools.invoke(state['messages'])]}
    


    ## Graph

    builder = StateGraph(State)
    builder.add_node("tools_calling_llm",call_llm_model)
    builder.add_node("tools",tool_node)

    #add edges
    builder.add_edge(START,"tools_calling_llm")
    builder.add_conditional_edges("tools_calling_llm",tools_condition)

    builder.add_edge("tools",END)

    #Compile The graph

    graph = builder.compile()



    display(Image(graph.get_graph().draw_mermaid_png()))
    return graph

tool_agent = make_tool_graph()
