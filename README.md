# Swarm-X

A lightweight multi-agent orchestration framework that is based on the [OpenAI Swarm](https://github.com/openai/swarm) project and adds support for
multiple LLM vendors.
Currently only supports [OpenAI](https://openai.com) and [ZhipuAI](https://www.zhipuai.cn).


### 1. Install & Configure environment

```
git clone https://github.com/sunmh207/swarm-x
cd swarm-x
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install "python-dotenv[cli]"
```

### 2. Configure variables

```
cp .env.dist .env
```

Set variables in `.env`, such as LLM provider, keys, etc.

### 3. Run examples

```
dotenv -f .env run python -m examples.basic.agent_handoff

dotenv -f .env run python -m examples.basic.function_calling

dotenv -f .env run python -m examples.airline.main
```

### 4. How to add support for new LLM providers?

Create a new Python class to implement the BaseClient class in the swarm/custom/client/base.py file.