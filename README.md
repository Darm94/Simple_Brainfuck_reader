# Brainfuck Runner (Python)

> A simple Brainfuck interpreter written in Python  
> It can execute Brainfuck code either from a file or directly from command-line text.

---

## Features

- Run Brainfuck code from a file (`--bf-file`)
- Run Brainfuck code directly from text (`--bf-text`)
- Validate code and reject not-allowed characters
- Uses `argparse` for command-line arguments
- Uses `tempfile` and `os` APIs to manage temporary files safely

---

## Usage

**Run from file**
```bash
python brainfuck.py --bf-file path/input_file.bf

Run from inline text

python brainfuck.py --bf-text "+++++[>++++++++<-]>+.+."

Ask for help

python brainfuck.py --help

```

---

## Functions Description

| Function                | Description                                      |
|-------------------------|--------------------------------------------------|
| `exe_brainfuck(file_path)`   | Executes Brainfuck code from a file              |
| `exe_brainfuck_text(text)`   | Runs Brainfuck text by creating a temporary file |
| `run_file(path)`             | Validates and runs an existing `.bf` file        |
| `validate_bf(code)`          | Checks for invalid characters                    |
| `main()`                     | Command-line interface using `argparse`          |

---

## Allowed Brainfuck Commands

< > + - . , [ ]

---

## Requirements

- Python 3.10 or higher (for `match/case` syntax)

---

## References

- [Python argparse documentation](https://docs.python.org/3/library/argparse.html)
- [Python os documentation](https://docs.python.org/3/library/os.html)
- [Python tempfile documentation](https://docs.python.org/3/library/tempfile.html)

