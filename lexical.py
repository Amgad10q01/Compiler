import re

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"

class LexicalAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_position = 0
        self.current_char = self.input_string[self.current_position]

    def advance(self):
        self.current_position += 1
        if self.current_position < len(self.input_string):
            self.current_char = self.input_string[self.current_position]
        else:
            self.current_char = None

    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit():
                tokens.append(self.extract_number())
            elif self.current_char in {'+', '-', '*', '/'}:
                tokens.append(Token(self.current_char, self.current_char))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token('LPAREN', '('))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token('RPAREN', ')'))
                self.advance()
            else:
                raise ValueError(f"Invalid character: {self.current_char}")

        return tokens

    def extract_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token('INTEGER', int(result))

# Example usage:
input_expr = "3 + 4 * (2 - 1)"
lexer = LexicalAnalyzer(input_expr)

try:
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)
except ValueError as e:
    print(f"Lexical Error: {e}")
