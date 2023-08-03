import random, threading
from Functions import objectMove


objectMove = objectMove.objectMove


# Function to create a new wave of objects
def newWave(canvas, main, Objects, textList, objectList):
    # Get the canvas width
    canvasWidth = canvas.winfo_width()

    # Iterate over the text list to create objects
    b = 0
    while b < len(textList):
        text = textList[b]

        # Create a new object
        objects = Objects(canvas, 0, 12, "salmon", text)
        objectList.append(objects)

        # Generate random position, speed in X and Y directions for the object
        randPosition = random.randint(0, canvasWidth - objects.Coords()[2])
        randSpeedX = random.randint(0, 1)
        randSpeedY = random.randint(1, 2)

        # Move the object to the initial position
        objects.Move(randPosition, 0)
        b += 1

        # Start a new thread to move the object
        arguments = (canvas, main, objects,
                     randSpeedX, randSpeedY,
                     text)
        thread = threading.Thread(target=objectMove, args=arguments)
        thread.daemon = True
        thread.start()
