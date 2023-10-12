def test_tmp_path(tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("Hello Hmak")
    assert file.read_text() == "Hello Hmak"
    

def test_tmp_path_factory(tmp_path_factory):
    path = tmp_path_factory.mktemp("sub")
    file = path / "file.txt"
    file.write_text("Hello Hm")
    assert file.read_text() == "Hello Hm"
    