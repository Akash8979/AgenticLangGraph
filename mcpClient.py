from langchain_mcp_adapters import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"], ## Ensure correct absoute path
                "trasport":"stdio"
            },
            "weather":{
                "url":"http://localhost:8000/mcp",
                "trasport":"streamable_http"
            }
        }
    )
    import os  
    os.environ['GROQ_API_KEY'] = os.getegid("GROQ_API_KEY")
    tools = await client.get_tools()
    model= ChatGroq(model="openai/gpt-oss-120b")
    agent = create_agent(
        model,tools
    )
    math_response = await agent.invoke(
        {
            "messages":[{"role":"user","content":"what is (3+5)*12?"}]
        }
    )

    print("Math reponse:",math_response['message'][-1].content)

asyncio.run(main())