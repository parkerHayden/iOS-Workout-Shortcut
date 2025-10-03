from PIL import Image, ImageDraw, ImageFont
import math
import numpy

def makeGradient(startColor, endColor, colorSteps):
    gradient = numpy.linspace(startColor,endColor,num= colorSteps,dtype=int)
    return gradient

def makeTimer(time, size, startColor, endColor, fontPath, outputPath):
    frames = []
    center = size // 2
    gradient = makeGradient(startColor, endColor, time)
    angleSteps = 360 / time
    if fontPath is None:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(fontPath, size // 2)
    for i in range(time):
        color = tuple(gradient[i])
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        d = ImageDraw.Draw(img)
        margin = 15
        bbox = (margin, margin, size - margin, size - margin)

        angleSteps = 360 / time

        startAngle = 0
        endAngle = 360 - (angleSteps * (i))
        d.arc(bbox, startAngle, endAngle, fill = color, width = 15)

        timeText = str(time - i)
        textBbox = draw.textbbox((0,0), timeText, font = font)
        draw.text((center, center), timeText, font=font, fill=color, anchor="mm")

        frames.append(img)

    frames[0].save(
        outputPath,
        save_all=True,
        append_images=frames[1:],
        duration=1000,  # 1 sec per frame
        loop=0,
        disposal=2
    )

makeTimer(
    time = 60, 
    size = 800, 
    startColor = (0,200,0),
    endColor = (200,0,0), 
    fontPath = "Magic Vintage TTF.ttf",
    outputPath = "assets/timer.gif")
