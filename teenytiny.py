from lex import Lexer, Token, TokenType

def test1():
	input = "LET foobar = 123"
	lexer = Lexer(input)

	while lexer.peek() != '\0':
		print(lexer.curChar)
		lexer.nextChar()


def test2():
    input = "+- */"
    lexer = Lexer(input)

    token = lexer.getToken()
    print(token)
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


test2()


