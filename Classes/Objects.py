class Objects:
    def __init__(self, canvas, axis, radius, color, text):
        self.canvas = canvas

        # Create an oval object with the specified properties
        self.oval = canvas.create_oval(
            axis,
            axis,
            radius,
            radius,
            fill=color,
            tag=text
        )

        # Create a text object with the specified properties
        self.textObj = canvas.create_text(
            (axis+15),
            (axis+5),
            text=text,
            font=("Times", 15),
            anchor="w",
            fill="white",
            tag=text
        )

        # Helper function to create a rounded rectangle shape
        def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
            points = [
                x1 + radius, y1,
                x1 + radius, y1,
                x2 - radius, y1,
                x2 - radius, y1,
                x2, y1,
                x2, y1 + radius,
                x2, y1 + radius,
                x2, y2 - radius,
                x2, y2 - radius,
                x2, y2,
                x2 - radius, y2,
                x2 - radius, y2,
                x1 + radius, y2,
                x1 + radius, y2,
                x1, y2,
                x1, y2 - radius,
                x1, y2 - radius,
                x1, y1 + radius,
                x1, y1 + radius,
                x1, y1
            ]
            return canvas.create_polygon(points, **kwargs, smooth=True)

        # Create a rounded rectangle shape behind the text
        bbox = canvas.bbox(self.textObj)
        width = bbox[2] - bbox[0]
        self.rectangle = create_rounded_rectangle(canvas,
                                                  (axis+8),
                                                  (axis-8),
                                                  (width//4)+width+15,
                                                  (axis+20),
                                                  radius=10,
                                                  fill="black",
                                                  outline=color,
                                                  tag=text
                                                  )

        # Raise the text object above the oval object
        canvas.tag_raise(self.textObj, self.oval)

        # Lower the rectangle shape below the text and oval objects
        canvas.tag_lower(self.rectangle)

    def Move(self, xVel, yVel):
        # Move the oval, text, and rectangle objects by the specified velocity
        self.canvas.move(self.oval, xVel, yVel)
        self.canvas.move(self.textObj, xVel, yVel)
        self.canvas.move(self.rectangle, xVel, yVel)

    def Coords(self):
        # Return the bounding box coordinates of the rectangle object
        return self.canvas.bbox(self.rectangle)

    def GetText(self):
        # Get the text associated with the text object
        return self.canvas.itemcget(self.textObj, "text")

    def DeleteText(self):
        # Delete the first letter of the text associated with the text object
        current_text = self.GetText()
        if current_text:
            new_text = current_text[1:]  # Remove the first letter
            self.canvas.itemconfig(self.textObj, text=new_text)
