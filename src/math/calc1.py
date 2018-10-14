# Token Types
#
# EOF (End-of-file) token is used to indicate that
# there is no more input left on the file
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token ({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        PLUS = '+'
        text = self.text

        if self.pos > len(text) -1:
            return Token(EOF, None)

        current_char = text[self.pos]


        if current_char.isDigit():
            token = Token(INTEGER, int(current_char))
            self.pos +=1
            return token

        if current_char == PLUS:
            token = Token(PLUS, current_char)
            self.pos +=1
            return token

        self.error()

