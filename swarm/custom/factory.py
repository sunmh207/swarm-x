import os

from dotenv import load_dotenv

from swarm.custom.client.base import BaseClient
from swarm.custom.client.openai import OpenAIClient
from swarm.custom.client.zhipuai import ZhipuAIClient
from swarm.util import debug_print


class Factory:
    @staticmethod
    def getClient(provider: str = None) -> BaseClient:
        load_dotenv()
        debug = os.getenv("DEBUG", "false").lower() in ("true", "1")
        provider = provider or os.getenv("LLM_PROVIDER", "openai")
        debug_print(debug, "The LLM provider is :", provider)
        chat_model_providers = {
            'zhipuai': lambda: ZhipuAIClient(),
            'openai': lambda: OpenAIClient()
        }

        provider_func = chat_model_providers.get(provider)
        if provider_func:
            return provider_func()
        else:
            raise Exception(f'Unknown chat model provider: {provider}')
