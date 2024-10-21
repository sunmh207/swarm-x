# README.md

- [English](README.md)
- [中文](README.zh-CN.md)

# Swarm-X

一个基于 [OpenAI Swarm](https://github.com/openai/swarm) 项目的轻量级多智能体编排框架，增加了对多个LLM供应商的支持。
目前仅支持 [OpenAI](https://openai.com) 和 [ZhipuAI](https://www.zhipuai.cn)。


### 1. 安装 & 配置环境

```
git clone https://github.com/sunmh207/swarm-x
cd swarm-x
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install "python-dotenv[cli]"
```

### 2. 配置变量

```
cp .env.dist .env
```

在 `.env` 中设置变量，例如 LLM 提供商、密钥等。

### 3. 运行示例

```
dotenv -f .env run python -m examples.basic.agent_handoff

dotenv -f .env run python -m examples.basic.function_calling

dotenv -f .env run python -m examples.airline.main
```

### 4. 如何为新的LLM供应商添加支持？

创建一个新的Python类实现 [BaseClient](swarm/custom/client/base.py)。