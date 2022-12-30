# tutor2
# Import modules
from pitop.pma import Button

# Set up the button on port D1 of the foundation plate
button = Button("D5")

# Loop until the button is pressed
while not button.is_pressed:
    pass

# Print to the console
print("Button Pressed")
  
