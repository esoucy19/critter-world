from enum import Enum, auto


class Type(Enum):
    """Token types for the critter language."""

    # rule
    THEN = auto()
    SEMICOLON = auto()
    # update
    ASSIGN = auto()
    # action
    WAIT = auto()
    FORWARD = auto()
    BACKWARD = auto()
    LEFT = auto()
    RIGHT = auto()
    EAT = auto()
    ATTACK = auto()
    GROW = auto()
    BUD = auto()
    SERVE = auto()
    # condition
    OR = auto()
    # conjunction
    AND = auto()
    # rel
    LESS = auto()
    LESS_EQUAL = auto()
    EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    NOT_EQUAL = auto()
    # factor
    NUMBER = auto()
    MEM = auto()
    # sensor
    NEARBY = auto()
    AHEAD = auto()
    RANDOM = auto()
    SMELL = auto()
    # addop
    PLUS = auto()
    MINUS = auto()
    # mulop
    MUL = auto()
    DIV = auto()
    MOD = auto()
    # grouping
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    # abbreviation
    MEMSIZE = auto()
    DEFENSE = auto()
    OFFENSE = auto()
    SIZE = auto()
    ENERGY = auto()
    PASS = auto()
    POSTURE = auto()
    # comment
    COMMENT = auto()
    # misc
    STRING = auto()


class Token:
    """A token of the critter_world grammar."""

    def __init__(self, typ: Type):
        """Makes a new token.

        PARAMETERS:
            type: The token's type.
        """
        self.type = typ


class Tokenizer:
    """This class tokenizes strings."""

    def tokenize(self, string: str) -> list[Token]:
        """Tokenize a string.

        PARAMETERS:
            string: The string to tokenize.

        RETURN:
            list[Token]: The resulting tokens.
        """
        if string == '+':
            return [Token(Type.PLUS)]
        if string == '-':
            return [Token(Type.MINUS)]
        return [Token(Type.MUL)]
