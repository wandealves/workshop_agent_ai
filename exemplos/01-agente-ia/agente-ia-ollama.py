from langchain_ollama import OllamaLLM
from langchain_community.tools import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv

load_dotenv()

search_tool = TavilySearchResults(
    max_results=5,
    include_answer=True,
    include_raw_content=True,
    include_images=True
)

llm = OllamaLLM(model="gemma2:2b")

tools = [search_tool]
agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

response = agent.run("Quem ganhou o campeonato brasileiro de 2024?")
print(response)