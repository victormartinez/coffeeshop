from typing import List
from pathlib import Path

import asyncio


async def input_to_sentences(filepath: str) -> List[str]:
    sentences_path = Path(filepath)
    if not sentences_path.exists():
        raise ValueError("File not found.")

    content = await asyncio.to_thread(sentences_path.read_text)
    return [x.strip() for x in content.split('\n')]
