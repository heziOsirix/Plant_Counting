from PIL import Image

Image.MAX_IMAGE_PIXELS = 7199886165
def split_image(image_path, num_rows, num_cols):
    image = Image.open(image_path)
    img_width, img_height = image.size

    # Calculate dimensions of each piece
    piece_width = img_width // num_cols
    piece_height = img_height // num_rows

    pieces = []
    for row in range(num_rows):
        for col in range(num_cols):
            left = col * piece_width
            upper = row * piece_height
            right = left + piece_width
            lower = upper + piece_height
            piece = image.crop((left, upper, right, lower))
            pieces.append(piece)

    return pieces

# Example usage
image_path = "D:\\24_3\\merged images\\plot 18.tif"  # Replace with your image path
num_rows = 1000
num_cols = 1000

pieces = split_image(image_path, num_rows, num_cols)

# Save each piece
for i, piece in enumerate(pieces):
    piece.save(f"piece_{i}.tif")
