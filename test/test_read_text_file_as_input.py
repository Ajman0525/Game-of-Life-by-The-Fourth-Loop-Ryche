def test_read_text_file_as_input():
    read = text_file()

    assert read.input() is True