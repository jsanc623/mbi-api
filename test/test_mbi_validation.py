import pytest as pytest

from mbi_validation import is_alpha, is_alphanumeric, is_numeric


@pytest.mark.parametrize("tin,tex", [("1", True), ("0", True), ("A", False)])
def test_is_numeric(tin, tex):
    assert is_numeric(tin) == tex


@pytest.mark.parametrize("tin,tex", [("a", True), ("A", True), ("0", False), ("Z", False)])
def test_is_alpha(tin, tex):
    assert is_alpha(tin) == tex


@pytest.mark.parametrize("tin,tex", [("1", True), ("0", True), ("A", True), ("a", True), ("Z", False)])
def test_is_alphanumeric(tin, tex):
    assert is_alphanumeric(tin) == tex
