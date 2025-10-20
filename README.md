<p align="center">
  <img src="./assets/Workout Shortcut Logo.png" alt="iOS Workout Shortcut" width="200"/>
</p>

<h1>iOS Workout Shortcut</h1>
  This apple shortcut is meant to function as a replacement for a workout application. What it does is give you a random workout from a set of exercises that you have chosen, not allowing you to repeat an exercise until all of them have been used. It allows you to input information about each exercise like weight, reps, and notes for each set that you do. It keeps this information stored in a .txt file and displays the information from the last time you completed each exercise as you get them again.

<h2>Example</h2>
  <p align="center">
    <img src="./assets/example.gif" alt="example gif"/>
  </p>
  <p align="center">
    This example only goes through a couple of exercises with only one set each.
  </p>



  
<h2>Setup</h2>
  <h3>Download</h3>
    The sharelink to the shortcut is here: <a href="https://www.icloud.com/shortcuts/dced128b0c844339b60770d997948f39" target="_blank">Shortcut</a> 
    and the helper shortcut is here: <a href="https://www.icloud.com/shortcuts/c1da6a89488541788f95b134baab3db2" target="_blank">Helper</a>
  <h3>Folder Structure</h3>
    The default shortcut links to a folder called "Exercises" which inside has a .Gif file called "timer" which displays between your sets and two folders: "Data" and "GIFs".     Inside of the "Data" folder is two .txt files:      Exercise History.txt and Recent Exercises.txt. Lastly, the "GIFs" folder contains all of the .gif files of the exercises you wish to have available in your workout.
    <pre>
    Exercises
    ├─ GIFs
    │  ├─ pushup.gif
    │  ├─ squat.gif
    │  ├─ bicep curl.gif
    │  ├─ etc.
    ├─ Data
    │  ├─ Recent Exercises.txt
    │  ├─ Exercise History.txt
    timer.gif
    </pre>
    
  <h3>Exercise GIFs</h3>
    You can get any .gif file for any exercise you would like, but if you want a consistant style of gif like I did, I would recommend using <a href="https://github.com/ExerciseDB/exercisedb-api" target="_blank">ExerciseDB</a> and their <a href="https://www.exercisedb.dev/docs" target="_blank">V1 API Playground</a> to search for a gif of (mostly) any exercise.

  <h3>Timer GIF</h3>
    Originally, I wanted a timer of 20 seconds for my rest period. I found it difficult to find a timer for that amount of time, so I decided to write some Python code that would make the gif for me.
    
```python
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
    fontPath = "assets/Magic Vintage TTF.ttf",
    outputPath = "assets/timer.gif")

```

  The code allows you to set the time interval you would like for your rest period, a start and end color for the timer to transition between, and a font for the numbers. NOTE: If you don't provide a font, the default that PIL provides ends up being really small and almost defeats the purpose of having the text there to begin with.

<p align="center">
  <img src="./assets/timer.gif" alt="60 second timer gif" width="200"/>
</p>

<h2>Known Problems</h2>
  <ul>
      <li>Sometimes not all of the characters will be saved after entering data into the Set info popup. 
          I suggest clicking into another textbox when you're done putting in your last item. This is a problem on Apple's end.</li>
      <li>I don't claim that this shortcut is optimized at all, this was just a project I was working on as a proof of concept to teach myself how shortcuts work and what they are capable of.</li>
  </ul> 

<h2>Future</h2>
I recently discovered that I could display gif files straight from their url, so I would like to create a version that does not require downloading the files. Right now the ability to display the data from the last time an exercise was used works based on the fact that there are 15 exercises and each workout has 5 exercises, so it pulls data from the last 3 workouts. I could change this to taking the reverse order from Exercise History.txt, loop through the data from the latest workouts, pull the data from the first time the exercise was done and ignore all others. At some point I might combine all of these changes into another version of this shortcut that instead of being purely random from a set of exercises, it would allow the user to choose a muscle group to target and get a random exercise from that group. Similar, but completely changing the user experience.

<h2>Full Shortcut</h2>
  <img src="./assets/Full Shortcut.png" alt="Full Shortcut"/>
