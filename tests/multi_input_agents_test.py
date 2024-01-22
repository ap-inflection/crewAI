from crewai import Agent, Task
from langchain.tools import tool
from langchain_community.agent_toolkits import FileManagementToolkit


def test_multi_input_agents():
    @tool
    def multiplier(a: int, b: int) -> float:
        """Useful for when you need to multiply two numbers together. The input is two numbers and the output is the
        result of the multiplication."""

        return a * b

    tools = FileManagementToolkit(
        root_dir="./output"
    ).get_tools()

    task = Task(
        agent=Agent(
            verbose=True,
            tools=tools + [multiplier],
            allow_delegation=True,
            description="You're a helpful assistant.",
            role="Helpful assistant",
            goal="Create a file with the right result.",
            backstory="Helpful assistant",
        ),
        verbose=True,
        description="""
                First run the multiplier tool with 100x100 and then create a file with the result.

                The file path is: test_file.txt
                """,
    )

    result = task.execute()
    print(result)
