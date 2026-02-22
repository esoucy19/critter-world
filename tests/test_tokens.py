from critter_world.token import Tokenizer, Type


def test_tokenize_token_plus():
    """Tokenize '+'.

    ["+", Type.PLUS]
    ["-", Type.MINUS]
    ["*", Type.MUL]
    ["/", Type.DIV]
    ["+", Type.PLUS]
    ["-->", Type.THEN]
    """
    tokenizer = Tokenizer()
    token = tokenizer.tokenize('+')[0]
    assert token.type == Type.PLUS


def test_tokenize_token_minus():
    """Tokenize '-'."""
    tokenizer = Tokenizer()
    token = tokenizer.tokenize('-')[0]
    assert token.type == Type.MINUS
