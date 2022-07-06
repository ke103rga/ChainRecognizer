from file_manager import data_input, data_output
from transliterator import transliteration
from lexer import lexical, check_keywords
from syntax import syntax


def main():
    s = data_input("input.txt")

    symbols = transliteration(s)

    words = lexical(symbols)

    if words:
        checked_words = check_keywords(words)
        result = syntax(checked_words)
    else:
        result = False

    data_output(result, "output.txt")


def main_with_logs():

    input_chain = FileManager.data_input()

    translyator_chain = Transliterator.process_chain_to_lexems(chain=input_chain)

    with open("transliteratorLog.txt", "a") as file:
        file.write("\n")
        file.write(str(translyator_chain))
        file.write("\n")

    lexer_chain = Lexer.process_chain_to_lexems(chain_of_lexems=translyator_chain)

    with open("LexerLog.txt", "a") as file:
        file.write("\n")
        file.write(str(lexer_chain))
        file.write("\n")

    chain_detected = syntax.check_lexems(chain_of_lexems=lexer_chain)

    with open("SyntaxLog.txt", "a") as file:
        file.write("\n")
        file.write(str(chain_detected))
        file.write("\n")

    FileManager.return_output(chain_detected=chain_detected)


if __name__ == "__main__":
    main()
