from PIL import Image, ImageDraw, ImageFont

# Create a blank white image
img = Image.new("RGB", (600, 200), color="white")
draw = ImageDraw.Draw(img)

# Text settings
text = "EMIPredict Pro"
font = ImageFont.load_default()

# Get text dimensions using textbbox (new Pillow method)
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Center position
position = ((600 - text_width) // 2, (200 - text_height) // 2)

# Draw the text
draw.text(position, text, fill="black", font=font)

# Save logo
img.save("assets/logo.png")

print("Logo successfully created at assets/logo.png")
