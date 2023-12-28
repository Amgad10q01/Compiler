import re

class SyntaxError(Exception):
    pass

class RecursiveDescentParser:
    def __init__(self, input_string):
        self.tokens = self.tokenize(input_string)
        self.current_token = None
        self.index = 0
        print(self.tokens)

    def tokenize(self, input_string):
        # A simple tokenizer for the arithmetic expression language
        input_string = input_string.replace(' ', '').replace('\t', '')
        print(input_string)
        return re.findall(r'\d+|\S', input_string)
    def get_next_token(self):
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
            self.index += 1
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.get_next_token()
        else:
            raise SyntaxError(f"Expected {expected_token}, but found {self.current_token}")

    def factor(self):
        if self.current_token.isdigit():
            value = int(self.current_token)
            self.match(self.current_token)
            return value
        elif self.current_token == '(':
            self.match('(')
            result = self.expr()
            self.match(')')
            return result
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

    def term(self):
        result = self.factor()
        while self.current_token in {'*', '/'}:
            if self.current_token == '*':
                self.match('*')
                result *= self.factor()
            elif self.current_token == '/':
                self.match('/')
                result /= self.factor()
        return result

    def expr(self):
        result = self.term()
        while self.current_token in {'+', '-'}:
            if self.current_token == '+':
                self.match('+')
                result += self.term()
            elif self.current_token == '-':
                self.match('-')
                result -= self.term()
        return result

    def parse(self):
        self.get_next_token()
        result = self.expr()
        if self.current_token is not None:
            raise SyntaxError(f"Unexpected token at the end: {self.current_token}")
        return result


# Example usage:
input_expr = "3 + 4 * (2 - 1)"
parser = RecursiveDescentParser(input_expr)

try:
    result = parser.parse()
    print(f"Result: {result}")
except SyntaxError as e:
    print(f"Syntax Error: {e}")