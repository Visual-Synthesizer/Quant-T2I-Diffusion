from PIL import Image, ImageDraw, ImageFont
import os

def create_image_grid(folder_path, output_path, rows=24, columns=4, image_size=(256, 256), margin=20):
    """
    Creates a grid image from individual images in a folder.
    
    Args:
        folder_path (str): Path to the folder containing images.
        output_path (str): Path to save the generated grid image.
        rows (int): Number of rows in the grid.
        columns (int): Number of columns in the grid.
        image_size (tuple): Size of each image in the grid (width, height).
        margin (int): Margin between images and text.
    
    Returns:
        Image: A grid image composed of the individual images.
    """
    # List and sort all the image files in the folder
    image_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

    # Create a new image with enough space for the grid and text
    grid_image = Image.new('RGB', (image_size[0] * columns, image_size[1] * rows + margin * (rows + 1)))

    # Load default font for text
    font = ImageFont.load_default()

    # Draw the folder name at the top of the grid image
    draw = ImageDraw.Draw(grid_image)
    folder_name = os.path.basename(folder_path)
    draw.text((10, margin//2), folder_name, font=font, fill=(255, 255, 255))

    for idx, filename in enumerate(image_files):
        # Open the image
        img = Image.open(os.path.join(folder_path, filename))

        # Resize the image to the specified size
        img = img.resize(image_size)

        # Calculate the position of the image in the grid
        x = (idx % columns) * image_size[0]
        y = (idx // columns) * image_size[1] + margin * ((idx // columns) + 1)

        # Paste the image into the grid at the calculated position
        grid_image.paste(img, (x, y + margin))

        # Write prompt text for each new row of images
        if idx % columns == 0:
            prompt_number = idx // columns + 1
            draw.text((10, y + margin//2), f"Prompt {prompt_number}", font=font, fill=(255, 255, 255))

    # Save the grid image to the specified output path
    grid_image.save(output_path)

# Example usage
folder_path = '/path/to/your/folder'  # Replace with the path to your folder containing images
output_path = '/path/to/save/grid_image.png'  # Replace with the path where you want to save the grid image
grid = create_image_grid(folder_path, output_path)
# grid.show()  # Display the grid image if needed
