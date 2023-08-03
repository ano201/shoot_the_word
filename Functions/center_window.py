# Function to center the window
def center_window(window,canvas):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Get the canvas width and height
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (canvas_width // 2)
    y = (screen_height // 2) - (canvas_height // 2)

    # Set the window's position
    window.geometry(f"{canvas_width}x{canvas_height}+{x}+{y-20}")