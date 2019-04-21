import random
from io import BytesIO

from PIL import Image, ImageDraw

originalDimension = 1500

r = lambda: random.randint(50, 215)
rc = lambda: (r(), r(), r())

listSymbols = []


def createSquare(border, draw, randomColor, element, size):
    if element == int(size / 2):
        draw.rectangle(border, randomColor)
    elif len(listSymbols) == element + 1:
        draw.rectangle(border, listSymbols.pop())
    else:
        listSymbols.append(randomColor)
        draw.rectangle(border, randomColor)


def createInvader(border, draw, size):
    x0, y0, x1, y1 = border
    squareSize = (x1 - x0) / size
    randomColors = [rc(), rc(), rc(), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
    i = 1

    for y in range(0, size):
        i *= -1
        element = 0
        for x in range(0, size):
            topLeftX = x * squareSize + x0
            topLeftY = y * squareSize + y0
            bottomRightX = topLeftX + squareSize
            bottomRightY = topLeftY + squareSize

            createSquare((topLeftX, topLeftY, bottomRightX, bottomRightY), draw, random.choice(randomColors), element,
                         size)
            if element == int(size / 2) or element == 0:
                i *= -1
            element += i


def spriteGenerator(size, invaders, imageSize):
    originalDimension = imageSize
    originalImage = Image.new('RGB', (originalDimension, originalDimension))
    draw = ImageDraw.Draw(originalImage)

    invaderSize = originalDimension / invaders
    padding = invaderSize / size

    for x in range(0, invaders):
        for y in range(0, invaders):
            topLeftX = x * invaderSize + padding / 2
            topLeftY = y * invaderSize + padding / 2
            bottomRightX = topLeftX + invaderSize - padding
            bottomRightY = topLeftY + invaderSize - padding

            createInvader((topLeftX, topLeftY, bottomRightX, bottomRightY), draw, size)

    # originalImage.save(
    #     "Examples/Example-" + str(size) + "x" + str(size) + "-" + str(invaders) + "-" + str(imageSize) + ".jpg")
    output = BytesIO()
    originalImage.save(output, format='JPEG')
    return output.getvalue()
