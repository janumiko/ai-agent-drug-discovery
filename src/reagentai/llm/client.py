import os
import logging
from typing import Type, TypeVar, Optional, List, Dict, Any

from pydantic_ai import Agent, Tool

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class LLMClient:
    def __init__(self, model_name: str = "google-gla:gemini-2.0-flash", tools: Optional[List[Tool]] = None):
        """
        Initializes the LLMClient with a specified model.

        Args:
            model_name (str): The name of the language model to use.
        """
        self.model_name = model_name
        self.tools = tools if tools is not None else []
        self.agent = Agent(model_name, tools=tools)
        self.result_history = None
        logger.info(f"LLMClient initialized with model: {model_name}")

    def change_model(self, model_name: str):
        """
        Changes the language model used by the client.

        Args:
            model_name (str): The name of the new language model.
        """
        self.model_name = model_name
        self.agent = Agent(model_name)
        logger.info(f"LLMClient model changed to: {model_name}")

    def get_token_usage(self) -> int:
        """
        Returns the token usage of the current agent.

        Returns:
            int: The number of tokens used.
        """
        if self.result_history is not None:
            return self.result_history.usage().total_tokens
        else:
            return 0

    def clear_history(self):
        """
        Clears the chat history of the agent.
        """
        # self.agent.clear_history()
        logger.info("LLMClient chat history cleared.")
        self.result_history = None

    def respond(
        self, user_query: str, **kwargs
    ) -> List[tuple]:
        """
        Responds to a user query and updates the chat history asynchronously.

        Args:
            user_query (str): The user's query.
            chat_history (List[tuple]): The current chat history.
            **kwargs: Additional keyword arguments to pass to the agent's run method.

        Returns:
            List[tuple]: Updated chat history with the bot's response.
        """
        if self.result_history is not None:
            message_history = self.result_history.all_messages()
        else:
            message_history = None

        result = self.agent.run_sync(
            user_query, message_history=message_history, **kwargs
        )
        self.result_history = result
        bot_message = result.output
        return bot_message
