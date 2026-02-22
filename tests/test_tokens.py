import pytest

from critter_world.token import Tokenizer, Type


@pytest.mark.parametrize(
    ('string', 'expected'),
    [
        ('+', Type.PLUS),
        ('-', Type.MINUS),
        ('*', Type.MUL),
    ],
)
def test_tokenize_single_token(string: str, expected: Type):
    """Tokenize single tokens.

    ('*', Type.MUL),
    ('/', Type.DIV),
    ('-->', Type.MUL),
    """
    tokenizer = Tokenizer()
    token = tokenizer.tokenize(string)[0]
    assert token.type == expected
