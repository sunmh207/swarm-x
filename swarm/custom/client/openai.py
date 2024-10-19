import json
import os
from typing import Dict, List, Optional

from dotenv import load_dotenv
from openai import OpenAI

from swarm.custom.client.base import BaseClient
from swarm.custom.types import CompletionMessage, NotGiven, NOT_GIVEN, CompletionMessageToolCall, Function


class OpenAIClient(BaseClient):

    def __init__(self, api_key: str = None):
        if not os.getenv("OPENAI_API_KEY"):
            load_dotenv()
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Please provide it or set it in the environment variables.")

        self.client = OpenAI(api_key=api_key)
        self.default_model = "gpt-4o"

    def completions(self,
                    messages: List[Dict[str, str]],
                    model: Optional[str] | NotGiven = NOT_GIVEN,
                    tools: Optional[dict] = None,
                    tool_choice: str | NotGiven = NOT_GIVEN
                    ) -> CompletionMessage:
        model = model or self.default_model
        completion = self.client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice
        )
        message = completion.choices[0].message

        tool_calls = (
            [CompletionMessageToolCall(id=call.id,
                                       function=Function(name=call.function.name, arguments=call.function.arguments),
                                       type="function")
             for call in message.tool_calls]
            if message.tool_calls else None
        )

        return CompletionMessage(
            message=json.loads(message.model_dump_json()),
            role="assistant",
            tool_calls=tool_calls
        )
