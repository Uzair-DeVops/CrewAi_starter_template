from crewai import Agent
from textwrap import dedent
from crewai import LLM

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools




"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:

Captain/Manager/Boss:

Employees/Experts to hire:



Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = LLM(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = LLM(model_name="gpt-4", temperature=0.7)
        self.Ollama = LLM(model="openhermes")



                    # Instantiate tools
        self.search_tool = SearchTools()
        self.calculator_tool = CalculatorTools()


    def agent_1_name(self):
        return Agent(
            role="Define agent 1 role here",
            backstory=dedent(f"""Define agent 1 backstory here"""),
            goal=dedent(f"""Define agent 1 goal here"""),
            # tools=[tool_1, tool_2],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def agent_2_name(self):
        return Agent(
            role="Define agent 2 role here",
            backstory=dedent(f"""Define agent 2 backstory here"""),
            goal=dedent(f"""Define agent 2 goal here"""),
            # tools=[tool_1, tool_2],
            verbose=True,
            llm=self.OpenAIGPT35,
        )
