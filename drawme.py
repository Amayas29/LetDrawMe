from PIL import Image
import sys

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width):
    """
    Resize image according to a new width
    """
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))


def grayify(image):
    """
    convert each pixel to grayscale
    """
    return image.convert("L")


def pixels_to_ascii(image):
    """
    convert pixels to a string of ascii characters
    """
    pixels = image.getdata()
    return "".join([ASCII_CHARS[pixel//25] for pixel in pixels])


def main():

    try:
        path = sys.argv[1]
        output = sys.argv[2]
        new_width = int(sys.argv[3])
    except:
        print(f"Usage : ${sys.argv[0]} image_path filename_output new_width")
        exit(1)

    new_width = 100 if new_width < 50 else new_width

    try:
        image = Image.open(path)
    except:
        print(f"{path} does not exist")
        exit(1)

    data = pixels_to_ascii(grayify(resize_image(image, new_width)))

    pixel_count = len(data)
    ascii_image = "\n".join([data[i:(i+new_width)]
                             for i in range(0, pixel_count, new_width)])

    with open(output, "w") as f:
        f.write(ascii_image)


main()
