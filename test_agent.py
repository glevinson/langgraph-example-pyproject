#!/usr/bin/env python3
"""
Simple test script for your LangGraph agent.
This bypasses the Studio compatibility issues and lets you test your agent directly.
"""

from my_agent.agent import graph


def test_agent():
    """Test the LangGraph agent with a simple conversation."""

    print("🤖 Testing your LangGraph Agent...")
    print("=" * 50)

    # Test message
    user_message = "Hello! Can you search for information about Python programming?"

    print(f"👤 User: {user_message}")
    print("🤖 Agent: Processing...")

    try:
        # Create initial state
        initial_state = {"messages": [{"role": "user", "content": user_message}]}

        # Run the graph
        result = graph.invoke(initial_state)

        # Get the final response
        final_messages = result["messages"]
        if final_messages:
            last_message = final_messages[-1]
            print(f"🤖 Agent: {last_message.content}")
        else:
            print("🤖 Agent: No response generated")

        print("\n✅ Agent test completed successfully!")

    except Exception as e:
        print(f"❌ Error testing agent: {e}")
        print("💡 Make sure your API keys are set in environment variables")


if __name__ == "__main__":
    test_agent()
