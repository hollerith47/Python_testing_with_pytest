from pathlib import Path

import pytest


@pytest.fixture()
def hello_write(tmp_path):
    filename = tmp_path / "hello.txt"
    message = "Hello Hm!"
    with open(filename, "w") as f:
        f.write(message)
    return filename


@pytest.fixture()
def hello_read(hello_write):
    with open(hello_write, 'r') as f:
        text = f.read()
    return text


def test_hello_with_file(hello_write, hello_read):
    assert hello_read == "Hello Hm!"


def test_hello_write(tmp_path):
    filename = tmp_path / "hello_1.txt"
    message = "Hello Hm"
    
    with open(filename, 'w') as f:
        f.write("Hello Hm")
        
    with open(filename, 'r') as f:
        hm = f.read()
    
    assert hm == "Hello Hm"
