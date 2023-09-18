import pytest

from coffeeshop.app.factory import create_ai_service


@pytest.mark.parametrize(
    "sentence_file,expected_file",
    [
        ("sentences_1.txt", "expected_1.txt"),
        ("sentences_2.txt", "expected_2.txt"),
        ("sentences_3.txt", "expected_3.txt"),
    ],
)
@pytest.mark.asyncio
async def test_ai_service(sentence_file, expected_file, row_reader, content_reader):
    conversation = []
    ai_service = await create_ai_service()
    # TODO: should not need to strip/split by \n
    for guest_row in row_reader(sentence_file):
        conversation.append(guest_row.strip("\n"))
        replied_msg = await ai_service.reply(guest_row)
        conversation.append(replied_msg)

    expected_rows = [row for row in content_reader(expected_file).split("\n") if row]
    assert conversation == expected_rows
