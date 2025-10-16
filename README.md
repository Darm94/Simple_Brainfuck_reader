 --------------------------
||Brainfuck Runner (Python)||
 --------------------------

A simple Brainfuck interpreter written in Python.
It can execute Brainfuck code either from a file or directly from command-line text.
----------------------------------------------------------------------------------------
FEATURES

Run Brainfuck code from a file (--bf-file)
Run Brainfuck code directly from text (--bf-text)
Validate code and reject not-allowed characters

Uses argparse for command-line arguments
Uses tempfile and os APIs to manage temporary files safely
----------------------------------------------------------------------------------------
USAGE

Run from file:
python brainfuck.py --bf-file path/input_file.bf (or .txt)

Run from inline text:
python brainfuck.py --bf-text "+++++[>++++++++<-]>+.+."

Ask help:
python brainfuck.py --help
----------------------------------------------------------------------------------------
FUNCTIONs DESCRIPTION

exe_brainfuck(file_path) -> executes Brainfuck code from a file
exe_brainfuck_text(text) -> runs Brainfuck text by creating a temporary file
run_file(path) -> validates and runs an existing .bf file
validate_bf(code) -> checks for invalid characters
main() -> command-line interface using argparse
----------------------------------------------------------------------------------------
ALLOWED BRAINFUCK COMMANDS

< + - . , [ ]
----------------------------------------------------------------------------------------
REQUIREMENTS

Only Python 3.10 or higher (for match/case syntax)
----------------------------------------------------------------------------------------
REFERENCES

Python argparse docs : https://docs.python.org/3/library/argparse.html
Python os docs : https://docs.python.org/3/library/os.html
Python tempfile docs : https://docs.python.org/3/library/tempfile.html
