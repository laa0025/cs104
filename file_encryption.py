import sys
from pathlib import Path
import text_encryption
import image_encryption


def main():
    if len(sys.argv) != 3:
        print('Usage: python file_encryption.py <infile> <key>')
        sys.exit(1)

    infile = Path(sys.argv[1])
    try:
        key = int(sys.argv[2])
        if not 0 <= key <= 255:
            raise ValueError
    except ValueError:
        print('Error: key must be an integer from 0 to 255.')
        sys.exit(1)

    suffix = infile.suffix.lower()
    if suffix not in ('.txt', '.png'):
        print('Error: input must be a .txt or .png file.')
        sys.exit(1)

    if not infile.is_file():
        print('Error: file does not exist:', infile)
        sys.exit(1)

    enc_file = infile.with_name('enc_' + infile.name)
    try:
        # Send the file to the correct encryption module.
        if suffix == '.txt':
            text_encryption.key = key
            content = text_encryption.read_file(infile)
            encrypted_content = text_encryption.encrypt_text(content)
            with open(enc_file, 'w', encoding='utf-8', newline='') as f:
                f.write(encrypted_content)
        elif suffix == '.png':
            image_encryption.key = key
            img = image_encryption.read_file(infile)
            encrypted_img = image_encryption.encrypt_image(img)
            encrypted_img.save(enc_file)
        print('Saved:', enc_file)
    except (OSError, ValueError) as error:
        print('Error:', error)
        sys.exit(1)


if __name__ == '__main__':
    main()
