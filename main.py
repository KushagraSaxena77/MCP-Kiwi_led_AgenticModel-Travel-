import asyncio
from langchain.messages import HumanMessage
from agent import build_Agent

async def main():

    print("Starting Travel Agent...")

    agent = await build_Agent()

    config = {"configurable": {"thread_id" :"1"}}

    while True:
        
        question = input("State your query: ")

        if question.lower() in ["exit","quit"]:break

        question_message = HumanMessage(content = question)

        print("Calling Agent...")

        response = await agent.ainvoke(
            {"messages": [question_message]},
            config
        )

        print('Agent Responded!')

        final_response = response["messages"][-1].text

        print(final_response)

if __name__ == '__main__':
    asyncio.run(main())





