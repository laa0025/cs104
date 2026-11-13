import sys
import random
from pathlib import Path
from PIL import Image

key = 0


def read_file(infile):
    with Image.open(infile) as img:
        return img.convert('RGB')


def encrypt_image(img):
    encrypted_img = Image.new("RGB", img.size)
    # Seed the random generator so the same key decrypts the image.
    rng = random.Random(key)
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            random_key = rng.randint(0, 255)
            encrypted_img.putpixel(
                (x, y),
                (r ^ random_key, g ^ random_key, b ^ random_key)
            )
    return encrypted_img


def main():
    global key
    if len(sys.argv) != 3:
        print('Usage: python image_encryption.py <infile.png> <key>')
        sys.exit(1)

    infile = Path(sys.argv[1])
    try:
        key = int(sys.argv[2])
        if not 0 <= key <= 255:
            raise ValueError
    except ValueError:
        print('Error: key must be an integer from 0 to 255.')
        sys.exit(1)

    if infile.suffix.lower() != '.png':
        print('Error: input must be a .png file.')
        sys.exit(1)

    try:
        img = read_file(infile)
        encrypted_img = encrypt_image(img)
        enc_file = infile.with_name('enc_' + infile.name)
        encrypted_img.save(enc_file)
        print('Saved:', enc_file)
    except (OSError, ValueError) as error:
        print('Error:', error)
        sys.exit(1)


if __name__ == '__main__':
    main()
