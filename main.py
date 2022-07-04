from file_manager import FileManager
from transliterator import Transliterator
from lexer import Lexer
from syntax import syntax


if __name__ == '__main__':

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
