import pytest as pytest

from mbi import MBI


@pytest.mark.parametrize("tin,tex,err_count",
                         [("5dh4wn0fc40", True, 0), ("1h70nd1pd22", True, 0),
                          ("", False, 1), (None, False, 1), ("!!!!!!!!!!!", False, 11),
                          ("0h45w11mj38", False, 1), ("8h4a411mja8", False, 3)])
def test_mbi_validate(tin, tex, err_count):
    output, errors = MBI(tin).validate()
    assert tex == output
    assert len(errors) == err_count


@pytest.mark.run(order=1)
@pytest.mark.parametrize("count", range(100))
def test_mbi_generate(count):
    mbi = MBI.generate()
    status, errors = MBI(mbi).validate()
    assert status is True
