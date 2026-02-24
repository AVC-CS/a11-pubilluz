import pytest
import os
import subprocess


@pytest.mark.T1
def test_preprocessed_file():
    """T1: main.i exists, headers expanded, no #include remaining"""
    assert os.path.exists('main.i'), "main.i not found — run: g++ -E main.cpp -o main.i"
    print("PASS: main.i exists")

    with open('main.i', 'r') as f:
        content = f.read()

    # Preprocessed file should be much larger than source (headers expanded)
    assert len(content) > 1000, \
        f"main.i is too small ({len(content)} bytes) — headers not expanded"
    print(f"PASS: main.i is {len(content)} bytes (headers expanded)")

    # Should contain expanded header content (extern, namespace, etc.)
    has_extern = 'extern' in content
    has_namespace = 'namespace' in content
    assert has_extern or has_namespace, \
        "main.i should contain 'extern' or 'namespace' from expanded headers"
    print("PASS: main.i contains expanded header content (extern/namespace)")

    # Should NOT have unexpanded #include directives
    lines = content.split('\n')
    includes = [l for l in lines if l.strip().startswith('#include')]
    assert len(includes) == 0, \
        f"main.i still has #include directives — preprocessing incomplete: {includes}"
    print("PASS: no #include directives remaining — preprocessing complete")


@pytest.mark.T2
def test_assembly_file():
    """T2: main.s exists, contains real assembly directives"""
    assert os.path.exists('main.s'), "main.s not found — run: g++ -S main.cpp -o main.s"
    print("PASS: main.s exists")

    with open('main.s', 'r') as f:
        content = f.read()

    # Should contain assembly directives or instructions
    has_text = '.text' in content
    has_globl = '.globl' in content or '.global' in content
    has_section = '.section' in content
    assert has_text or has_globl or has_section, \
        "main.s should contain assembly directives like .text, .globl, or .section"
    print("PASS: main.s contains assembly directives (.text/.globl/.section)")

    # Should contain the string literal from source
    assert 'Hello' in content or 'hello' in content, \
        "main.s should contain the 'Hello' string literal"
    print("PASS: main.s contains 'Hello' string literal")


@pytest.mark.T3
def test_object_file():
    """T3: main.o exists, is binary, contains Hello string"""
    assert os.path.exists('main.o'), "main.o not found — run: g++ -c main.cpp -o main.o"
    print("PASS: main.o exists")

    # Object file should not be empty
    size = os.path.getsize('main.o')
    assert size > 100, f"main.o is too small ({size} bytes)"
    print(f"PASS: main.o is {size} bytes (valid object file)")

    # Use strings command to find the string literal in binary
    result = subprocess.run(['strings', 'main.o'], capture_output=True, text=True)
    assert 'Hello' in result.stdout or 'hello' in result.stdout, \
        "main.o should contain 'Hello' string — was the correct source assembled?"
    print("PASS: main.o contains 'Hello' string literal in binary")


@pytest.mark.T4
def test_executable_output():
    """T4: a.out exists, output contains Hello world"""
    assert os.path.exists('result.txt'), "result.txt not found — run: ./a.out > result.txt"
    print("PASS: result.txt exists")

    with open('result.txt', 'r') as f:
        lines = f.readlines()
    print(f"Output: {lines}")
    lines = [line.strip() for line in lines]

    found = any('Hello' in line for line in lines)
    assert found, "Expected 'Hello' in program output"
    print("PASS: program output contains 'Hello' — linking successful")
