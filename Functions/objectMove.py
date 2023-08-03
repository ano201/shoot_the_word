import time
from Functions import gameOver


gameOver = gameOver.gameOver


# Function to move the object
def objectMove(canvas, main, objects, xVelocity, yVelocity, text):
    while True:

        # Move the object by the specified velocity
        objects.Move(xVelocity, yVelocity)
        time.sleep(0.05)

        # Get the coordinates of the object and the main object
        coords = canvas.coords
        objCoords, mainCoords = objects.Coords(), coords(main)

        # Check if the coordinate lists are valid
        if objCoords is None or mainCoords is None:
            return

        # Check if the coordinate lists have the expected length
        # if len(objCoords) < 4 or len(mainCoords) < 2:
        #     # Handle the case where the coordinate lists do not have the expected length
        #     break

        # Check if the object has reached the canvas boundaries or collided with the main object
        if objCoords[2] >= canvas.winfo_width():
            xVelocity = -xVelocity
        elif objCoords[0] <= 0:
            xVelocity = -xVelocity
        elif objCoords[3] >= mainCoords[1]:
            # Game over condition
            gameOver(canvas, text)
            break
