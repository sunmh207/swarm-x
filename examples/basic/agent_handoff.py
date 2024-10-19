from swarm.core import Swarm
from swarm.types import Agent

client = Swarm()

english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",
)

chinese_agent = Agent(
    name="中文 Agent",
    instructions="你只说中文.",
)


def transfer_to_chinese_agent():
    """转交中文Agent."""
    return chinese_agent


english_agent.functions.append(transfer_to_chinese_agent)

messages = [{"role": "user", "content": "你好."}]
response = client.run(agent=english_agent, messages=messages, debug=True)

print(response.messages[-1]["content"])
