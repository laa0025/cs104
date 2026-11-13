import sys
from pathlib import Path

key = 0


def read_file(infile):
    with open(infile, 'r', encoding='utf-8', newline='') as f:
        return f.read()


def encrypt_text(content):
    # XOR each character with the key. Applying it twice reverses it.
    return ''.join(chr(ord(char) ^ key) for char in content)


def main():
    global key
    if len(sys.argv) != 3:
        print('Usage: python text_encryption.py <infile.txt> <key>')
        sys.exit(1)

    infile = Path(sys.argv[1])
    try:
        key = int(sys.argv[2])
        if not 0 <= key <= 255:
            raise ValueError
    except ValueError:
        print('Error: key must be an integer from 0 to 255.')
        sys.exit(1)

    if infile.suffix.lower() != '.txt':
        print('Error: input must be a .txt file.')
        sys.exit(1)

    try:
        content = read_file(infile)
        encrypted_content = encrypt_text(content)
        # Save in the same folder as the input file.
        enc_file = infile.with_name('enc_' + infile.name)
        with open(enc_file, 'w', encoding='utf-8', newline='') as f:
            f.write(encrypted_content)
        print('Saved:', enc_file)
    except (OSError, UnicodeError) as error:
        print('Error:', error)
        sys.exit(1)


if __name__ == '__main__':
    main()
