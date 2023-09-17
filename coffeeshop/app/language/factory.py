from .parser.en import EnParser


def create_parser(lang: str):
    if lang == "en":
        return EnParser()
    
    raise ValueError(f"Parser of language {lang} is not available.")