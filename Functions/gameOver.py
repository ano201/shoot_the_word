# Function to handle game over
def gameOver(canvas, tag):
    # Delete the object from the canvas
    canvas.delete(tag)

    canvas.delete("all")

    # Display game over message
    canvas_width = canvas.winfo_width()
    text1 = canvas.create_text(
        canvas_width // 2,
        200,
        text="You really did Pretty",
        font=("Ink Free", 25, "bold"),
        fill="coral"
    )
    text2 = canvas.create_text(
        canvas_width // 2,
        260,
        text="Pretty Bad!",
        font=("Ink Free", 25, "bold"),
        fill="coral4"
    )
