import pytest

from k_butler.filesbo import FileBo


@pytest.mark.parametrize(
    "fullpath, parts",
    [
        pytest.param("/foo/bar", ('/foo', 'bar', '')),
        pytest.param("/foo/bar/alfa.pdf", ('/foo/bar', 'alfa', 'pdf')),
    ]
)
def test_parts(fullpath: str, parts: tuple[str, str, str]) -> None:
    filebo = FileBo(fullpath)
    assert filebo.parts == parts
    assert filebo.stem == parts[1].split('.')[0]
