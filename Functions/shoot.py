# Function to handle shooting an object
def shoot(event, start, canvas, objectList, foundObject, tag):
    # Get the pressed key
    pressed_key = event.keysym

    # Check if there is a found object
    if foundObject:
        # Get the text of the found object
        nowObject_text = foundObject[0].GetText()

        # Check if the object text is a valid string and not empty
        if isinstance(nowObject_text, str) and nowObject_text:
            # Check if the pressed key matches the first character of the object text
            if pressed_key == nowObject_text[0]:
                # Delete the first character of the object text
                foundObject[0].DeleteText()

                # Check if the object text is now empty
                if len(nowObject_text) - 1 == 0:
                    # Delete the object from the canvas
                    canvas.delete(tag[0])

                    # Clear the found object and tag lists
                    foundObject.clear()
                    tag.clear()

                # Check if there are only 2 objects remaining on the canvas
                if len(canvas.find_all()) <= 2:
                    # Start a new wave of objects
                    start()
            else:
                # Display a message for wrong key press
                print("Wrong key")
    else:
        # Iterate over the object list
        for obj in objectList:
            # Get the text of the object
            object_text = obj.GetText()

            # Check if the object has a text and if the pressed key matches the first character of the text
            if object_text and pressed_key == object_text[0]:
                # Add the object to the found objects list
                foundObject.append(obj)
                tag.append(obj.GetText())

                # Delete the first character of the object text
                obj.DeleteText()
                break
