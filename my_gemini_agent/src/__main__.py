"""
Main entry point for the Gemini agent.
"""
import asyncio

from .agent import root_agent


async def async_main():
    """Run the Gemini agent."""
    response = await root_agent.invoke("Hello, how are you?")
    print(response)


def main():
    """Entry point for the script."""
    asyncio.run(async_main())


if __name__ == "__main__":
    main()