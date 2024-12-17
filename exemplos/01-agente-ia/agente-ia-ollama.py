from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_community.llms import Ollama

load_dotenv()

tavily_search = TavilySearchResults(    max_results=2,
    include_answer=True,
    include_raw_content=True,
    include_images=True)

ollama_llm = Ollama(
    model="qwen2.5:3b",
    base_url="http://localhost:11434",
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
    llm=ollama_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Tipo de agente
    verbose=True
)

if __name__ == "__main__":
    query = "qual time foi campeão doo brasileirão 2024?"
    print("\nExecutando consulta no agente...\n")
    response = agent.run(query)
    print("\nResposta do Agente:\n", response)
