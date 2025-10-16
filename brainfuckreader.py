import sys
import argparse
import tempfile
import os

"""My Original brainfuck reader from specific file"""
def exe_brainfuck(file_path):
    with open(file_path, 'r') as f:
       code = f.read() 

    mem = [0] * 10000
    pos = 0
    i = 0
    backup_stack = []
    
    # read code
    while i < len(code):
        match code[i]:
            case '>':
                pos += 1
            case '<':
                pos -= 1
            case '+':
                mem[pos] = (mem[pos] + 1) % 128
            case '-':
                mem[pos] = (mem[pos] - 1) % 128
            case '.':
                print(chr(mem[pos]), end='')
            case '[':
                if mem[pos] == 0:
                    open_brackets = 1
                    while open_brackets:
                        i += 1
                        if i >= len(code):
                            break
                        if code[i] == '[':
                            open_brackets += 1
                        elif code[i] == ']':
                            open_brackets -= 1
                else:
                    backup_stack.append(i)
            case ']':
                if mem[pos] != 0:
                    i = backup_stack[-1]
                else:
                    if backup_stack:
                        backup_stack.pop()
            case _:
                pass
        i += 1

"""Validation function"""
def validate_bf(code: str):
    #Return (ok, invalid_chars_set). Only '><+-.,[]' allowed; whitespace ignored.
    allowed = set('><+-.,[]')
    invalid = {c for c in code if not c.isspace() and c not in allowed}
    return (len(invalid) == 0, invalid)

"""Read from text function using os API. My source: https://docs.python.org/3/library/os.html"""
def exe_brainfuck_text(code_text: str):
    ok, bad = validate_bf(code_text)#my validation funcion
    if not ok:
        print(f"Error: not allowed characters found")
        sys.exit(2)#validation error
    #creating a temp file to use the original file reader function    
    with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8', suffix='.bf') as tmp:
        tmp.write(code_text)
        tmp_path = tmp.name
    try:
        exe_brainfuck(tmp_path)#my fun
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass

"""Read from file function suing os API. My source: https://docs.python.org/3/library/os.html"""
def run_file(path: str):
    if not os.path.isfile(path):
        print(f"Error: file not found: {path}")
        sys.exit(1)
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    ok, bad = validate_bf(code)#my validation funcion
    if not ok:
        print(f"Error: not allowed characters found")
        sys.exit(2)#validation error
    exe_brainfuck(path)#my fun

"""Main using argparse API to read command. My source https://docs.python.org/3/library/argparse.html"""
def main():
    parser = argparse.ArgumentParser(
        description="Simple Brainfuck runner: use --bf-text or --bf-file."
    )
    parser.add_argument("--bf-text", help="Run Brainfuck code passed as a string")
    parser.add_argument("--bf-file", help="Run Brainfuck code from a file path")
    args = parser.parse_args()

    if args.bf_text and args.bf_file:
        print("Error: choose either --bf-text or --bf-file, not both.")
        sys.exit(1)

    if args.bf_text:
        exe_brainfuck_text(args.bf_text)
    elif args.bf_file:
        run_file(args.bf_file)
    else:
        print("Error: no input provided. Use --bf-text or --bf-file (or --help).")
        sys.exit(1)

if __name__ == "__main__":
    main()