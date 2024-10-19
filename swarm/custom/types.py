from typing import Optional, List, Literal

from pydantic import BaseModel
from typing_extensions import override


class NotGiven:
    """
    A sentinel singleton class used to distinguish omitted keyword arguments
    from those passed in with the value None (which may have different behavior).

    For example:

    ```py
    def get(timeout: Union[int, NotGiven, None] = NotGiven()) -> Response: ...


    get(timeout=1)  # 1s timeout
    get(timeout=None)  # No timeout
    get()  # Default timeout behavior, which may not be statically known at the method definition.
    ```
    """

    def __bool__(self) -> Literal[False]:
        return False

    @override
    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()


class Function(BaseModel):
    arguments: str
    name: str


class CompletionMessageToolCall(BaseModel):
    id: str
    function: Function
    type: Literal["function"]


class CompletionMessage(BaseModel):
    """
    {
    "content": "None",
    "refusal": "None",
    "role": "assistant",
    "function_call": "None",
    "tool_calls": [{"id": "call_g89r3wk3vcoacr7kB8Y4W2CA",
    "function": {"arguments": "{\"location\":\"New York City NY\"}", "name": "get_weather"}, "type": "function"}], "sender": "Agent"
    }
    """
    message: dict
    role: str
    tool_calls: Optional[List[CompletionMessageToolCall]] = None
