from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

tavily_search = TavilySearchResults(    max_results=2,
    include_answer=True,
    include_raw_content=True,
    include_images=True)

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192"
)

tools = [
    Tool(
        name="Tavily Search",
        func=tavily_search.run,
        description="Use esta ferramenta para buscar informações na web. Forneça uma consulta descritiva."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    query = "qual time foi campeão doo brasileirão 2024?"
    print("\nExecutando consulta no agente...\n")
    response = agent.run(query)
    print("\nResposta do Agente:\n", response)

