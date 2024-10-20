import os  # Add this import to handle folder creation
import requests
from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
from io import BytesIO
import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_meme_template():
    # Get a random meme template from Imgflip API
    response = requests.get("https://api.imgflip.com/get_memes")
    memes = response.json()['data']['memes']
    template = random.choice(memes)
    return template['url'], template['width'], template['height']


def generate_meme_text_with_groq(trend, company_theme="Resume Building"):
    prompt = f"""
    Create a funny meme text related to the trending topic "{trend}" and the theme of "{company_theme}".
    The meme should be witty and relate to job searching or resume building.
    Format the response as two lines of text:
    Top text of the meme
    Bottom text of the meme
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.7,
        max_tokens=100,
    )

    # Ensure that you only take the first two lines from the generated text
    response_text = chat_completion.choices[0].message.content.strip()
    lines = response_text.split('\n')

    # Return only the first two lines (or empty strings if not enough lines)
    top_text = lines[0] if len(lines) > 0 else ""
    bottom_text = lines[1] if len(lines) > 1 else ""

    return top_text, bottom_text


def create_meme(trend, company_theme="Resume Building"):
    # Create the 'memes' directory if it doesn't exist
    if not os.path.exists("memes"):
        os.makedirs("memes")

    # Get meme template
    template_url, width, height = get_meme_template()

    # Download the template image
    response = requests.get(template_url)
    img = Image.open(BytesIO(response.content))

    # Prepare to draw on the image
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)

    # Generate meme text using Groq
    top_text, bottom_text = generate_meme_text_with_groq(trend, company_theme)

    # Function to wrap text
    def wrap_text(text, font, max_width):
        lines = textwrap.wrap(text, width=max_width)
        return lines  # Return the list of lines

    # Add top text
    top_lines = wrap_text(top_text, font, img.width // 20)
    for i, line in enumerate(top_lines):
        draw.text((10, 10 + i * 50), line, font=font, fill="white",
                  stroke_width=2, stroke_fill="black")

    # Add bottom text
    bottom_lines = wrap_text(bottom_text, font, img.width // 20)
    bottom_height = sum(draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox(
        (0, 0), line, font=font)[1] for line in bottom_lines)  # Calculate total height for bottom text

    for i, line in enumerate(bottom_lines):
        draw.text((10, height - bottom_height - 10 + i * 50), line,
                  font=font, fill="white", stroke_width=2, stroke_fill="black")

    # Save the meme in the 'memes' folder
    filename = f"memes/meme_{trend.split()[0].replace(' ', '_')}.png"
    img.save(filename)
    print(f"Meme saved as {filename}")


def main():
    company_theme = "Resume Building"

    # Load trending topics from JSON file
    with open('trending_topics.json', 'r') as f:
        trending_topics = json.load(f)

    print("Generating memes...")
    for topic in trending_topics[:5]:  # Create memes for top 5 topics
        create_meme(topic, company_theme)


if __name__ == "__main__":
    main()
