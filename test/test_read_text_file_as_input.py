from src.read_text import File
def test_read_text_file_as_input():
    read = File()

    assert read.text_file() == "read"   