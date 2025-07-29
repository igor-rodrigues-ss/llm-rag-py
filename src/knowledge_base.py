import argparse

from pypdf import PdfReader

from src.database import knowledge_base


def main(pdf_path: str):
    reader = PdfReader(pdf_path)

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            knowledge_base.insert(page_number=page_number, text=text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Knowledge Base Loader")

    parser.add_argument("--path", type=str, help="Path to the PDF file to load")

    args = parser.parse_args()

    main(args.path)
