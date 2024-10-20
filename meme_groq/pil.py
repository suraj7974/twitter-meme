# meme_generator.py

from PIL import Image, ImageDraw, ImageFont


def create_meme(text):
    # Create a blank white image
    img = Image.new('RGB', (500, 500), color='white')

    # Add text to the image
    draw = ImageDraw.Draw(img)
    # Make sure the font file is accessible
    font = ImageFont.truetype("arial.ttf", 20)

    # Wrap text for long strings
    if len(text) > 50:
        text = text[:50] + "\n" + text[50:]

    draw.text((50, 250), text, font=font, fill=(0, 0, 0))

    # Save the meme as a file
    img.save('meme.png')


if __name__ == "__main__":
    create_meme("Your career can be more trending than #Cricket!")
