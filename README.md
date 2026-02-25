[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22865549&assignment_repo_type=AssignmentRepo)

### CS140A11 - Compilation Process: From Source to Executable

> Practice the 4 stages of C++ compilation: <br>
> **Preprocessor** → **Compiler** → **Assembler** → **Linker**

### Compilation Steps

> 1. Preprocess: `g++ -E main.cpp -o main.i` <br>
> 2. Compile to assembly: `g++ -S main.cpp -o main.s` <br>
> 3. Assemble to object: `g++ -c main.cpp -o main.o` <br>
> 4. Link to executable: `g++ main.o -o a.out` <br>
> 5. Run: `./a.out`

## You can test your program by typing the command

> data/run.sh <br>
> pytest -rP

### Do not change any test files

> if you want to restore all files, just clone again with this assignment link.
