from PIL import Image
import colour_helper
def grayscale(pixel:tuple):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average =(red + green + blue) /3
    if average>=128:
        return True
    else:
        return False



# Test?
light_pixel = (255, 255, 255)
light_gray = (128, 128, 128)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)

print(colour_helper.is_light(light_pixel))  # True
print(colour_helper.is_light(light_gray))  # True
print(colour_helper.is_light(dark_gray))  # False
print(colour_helper.is_light(dark_pixel))  # False
# starting at the top and working our way down
    # visit the pixels from left to right
with Image.open("./images/catto.png") as im:
    image_height = im.height
    image_width = im.width

    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))
            if colour_helper.is_light(pixel):
                im.putpixel((x,y), light_pixel)
            elif colour_helper.is_gray(pixel):
                im.putpixel((x,y), light_gray)
            elif colour_helper.is_dark_gray(pixel):
                im.putpixel((x,y), dark_gray)
            else:
                im.putpixel((x,y), dark_pixel)


    im.save("./Images/binarized.jpg")
