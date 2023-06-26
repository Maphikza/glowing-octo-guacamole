from PIL import Image


def black_to_white(image_path: str):
    """
    Functions that converts an image to grayscale.
    :param image_path: The path where the image is located.
    :return: None
    """
    # Convert the image to grayscale
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Define the threshold value to determine which pixels to convert to white
    threshold = 128

    # Define the desired color
    desired_color = (255, 255, 255)  # RGB values of white

    # Create a new image with transparency
    modified_image = Image.new('RGBA', grayscale_image.size)

    # Iterate over each pixel in the grayscale image
    width, height = grayscale_image.size
    for x in range(width):
        for y in range(height):
            pixel_value = grayscale_image.getpixel((x, y))

            # Check if the pixel value is below the threshold
            if pixel_value < threshold:
                # Convert the pixel to white
                modified_image.putpixel((x, y), desired_color)
            else:
                # Copy the pixel value from the original image
                modified_image.putpixel((x, y), image.getpixel((x, y)))

    # Save the modified image
    modified_image.save('modified_image.png')
