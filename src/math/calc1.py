# Token Types
#
# EOF (End-of-file) token is used to indicate that
# there is no more input left on the file
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'
OPERATORS = [(MINUS, '-', 'MINUS'), (PLUS, '+', 'PLUS')]


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        text = self.text

        if self.pos > len(text) - 1:
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char.isspace():
            self.pos += 1
            if self.pos < len(text):
                current_char = text[self.pos]
            else:
                return Token(EOF, None)

        if current_char.isdigit():
            digits = ""
            digits += current_char
            self.pos += 1
            if self.pos < len(text):
                next_char = text[self.pos]
                if next_char.isdigit():
                    digits += next_char
                    self.pos += 1
            return Token(INTEGER, int(digits))

        for operator in OPERATORS:
            if operator[1] == current_char:
                self.pos += 1
                return Token(operator[0], current_char)

        self.error()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(op.type)

        right = self.current_token
        self.eat(INTEGER)

        if op.value == '+':
            return left.value + right.value
        else:
            return left.value - right.value


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break

        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()

        print(result)


if __name__ == '__main__':
    main()