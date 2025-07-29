import ollama

from typing import Generator

from src.database import knowledge_base


def run_model(prompt: str) -> Generator[str, None, None]:
    contexts = knowledge_base.query_context_by_similarity(prompt)

    context_prompt = f"Contexts: {contexts} Ask: {prompt}"

    response = ollama.chat(
        model="gemma3:1b", stream=True, messages=[{"role": "user", "content": context_prompt}]
    )
    for chunk in response:
        yield chunk["message"]["content"]
