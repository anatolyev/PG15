from reverse import reverse
import pytest

def test_reverse():
    assert reverse('123') == '321'

def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(42)
