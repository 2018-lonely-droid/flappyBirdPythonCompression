from PIL import Image
import os


def downsample_image(input_image_path, output_image_path, factor=2):
    """
    Downsamples an image by averaging pixel values in blocks of pixels.
    
    Parameters:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the downsampled image.
        factor (int): Downsampling factor (e.g., factor=2 reduces image resolution by half).
    """
    input_image = Image.open(input_image_path)
    width, height = input_image.size
    new_width = width // factor
    new_height = height // factor
    output_image = Image.new('RGB', (new_width, new_height))

    for y in range(new_height):
        for x in range(new_width):
            # Calculate average pixel value in a block of pixels
            block_sum = [0, 0, 0]
            for dy in range(factor):
                for dx in range(factor):
                    pixel = input_image.getpixel((x * factor + dx, y * factor + dy))
                    block_sum[0] += (pixel >> 16) & 0xFF  # Red channel
                    block_sum[1] += (pixel >> 8) & 0xFF   # Green channel
                    block_sum[2] += pixel & 0xFF          # Blue channel
            num_pixels = factor * factor
            avg_pixel = ((block_sum[0] // num_pixels) << 16) + ((block_sum[1] // num_pixels) << 8) + (block_sum[2] // num_pixels)
            output_image.putpixel((x, y), avg_pixel)

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    # Save the downsampled image
    output_image.save(output_image_path)


# Example usage:
input_image_path = os.path.abspath("Flappy-bird-python/assets/sprites/pipe-green.png")
output_image_path = os.path.abspath("Flappy-bird-python-compressed/assets/sprites/pipe-green.png")

# Delete a previous compressed image if exists
if os.path.exists(output_image_path):
    os.remove(output_image_path)

# Compress image with downsample_image algorithm
downsample_image(input_image_path, output_image_path, factor=2)


