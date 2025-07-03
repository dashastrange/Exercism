from smolagents import LiteLLMModel, GoogleSearchTool
from smolagents import (
    ToolCallingAgent,
    VisitWebpageTool,
)

model = LiteLLMModel(model_id="google/tapas-mini-finetuned-sqa")
llmModel = LiteLLMModel()


agent = ToolCallingAgent(
    tools=[GoogleSearchTool(), VisitWebpageTool()],
    model=llmModel,
    add_base_tools=True
)

agent.run("fetch the share price of google from 2020 to 2024, and create a line graph from it?")
