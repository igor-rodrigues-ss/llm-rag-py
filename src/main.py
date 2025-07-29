import argparse

from src.model import ai


def main(prompt: str):
    response = ai.run_model(prompt)

    for chunk in response:
        print(chunk, flush=True, end="")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Assistant with Knowledge Base")

    parser.add_argument("prompt", type=str, help="Input prompt for the AI model")

    args = parser.parse_args()

    main(args.prompt)
