import pytest

from critter_world.token import Tokenizer, Type


@pytest.mark.parametrize(
    ('string', 'expected'),
    [
        ('+', Type.PLUS),
        ('-', Type.MINUS),
        ('*', Type.MUL),
        ('%unknown_token$', Type.UNKNOWN),
        ('7', Type.NUMBER),
        ('13', Type.NUMBER),
    ],
)
def test_tokenizes_single_token(string: str, expected: Type):
    """Tokenize single tokens."""
    tokenizer = Tokenizer()
    token = tokenizer.tokenize(string)[0]
    assert token.type == expected


def test_ignores_surrounding_whitespace():
    """Ignores surrounding whitespace."""
    tokenizer = Tokenizer()
    token = tokenizer.tokenize(' + ')[0]
    assert token.type == Type.PLUS
