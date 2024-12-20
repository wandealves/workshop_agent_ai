from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType, tool,Tool

ollama_llm = OllamaLLM(
    model="qwen2.5:3b",
    base_url="http://localhost:11434",
)

@tool
def calculator_tool(input: str) -> str:
    """Realiza cálculos matemáticos básicos. Input deve ser uma operação, como '2 + 2'."""
    try:
        result = eval(input)
        return f"O resultado de {input} é {result}."
    except Exception as e:
        return f"Erro ao calcular: {str(e)}"
    
tools = [
    Tool(
        name="Calculador",
        func=calculator_tool,
        description="Use esta ferramenta para o calculo matematico."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=ollama_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    query = "Quanto é 10 * 15 + 20?"
    print("\nExecutando consulta no agente...\n")
    response = agent.run(query)
    print("\nResposta do Agente:\n", response)