# Import necessary modules from MicroPython for the Micro:bit
from microbit import *
import random
import speech # Import the speech module for text-to-speech

# Global variables
# 'choice' will store the index of the currently selected dice type in the 'options' list.
# It starts at 0, corresponding to the first item in the 'options' list (d4).
choice = 0

# 'options' is a list containing the maximum values for each type of die.
# This list defines the available dice: d4, d6, d8, d10, d12, d20, d100.
options = [4, 6, 8, 10, 12, 20, 100]

def print_currently_selected_option():
    """
    Displays the currently selected dice type on the Micro:bit's LED display.
    For example, if 'choice' is 0, it will display "D4".
    Also, uses speech to announce the selected die type.
    """
    # Access the value from the 'options' list using the 'choice' index.
    current_die_sides = options[choice]
    display_string = "D" + str(current_die_sides)

    # Clear display before showing new string to prevent ghosting
    display.clear()
    # Display on LEDs using display.scroll for better visibility of longer strings/numbers
    display.scroll(display_string)

    # Speak the selected option
    speech.say(display_string)
    # Add a small pause after speech to allow the Micro:bit to process
    sleep(200) # Increased sleep duration

def d4():
    """
    Rolls a 4-sided die and displays the result.
    Also, uses speech to announce the result.
    """
    result = random.randint(1, 4)
    display.clear() # Clear display before showing new number
    display.scroll(result) # Use display.scroll for numbers
    speech.say(str(result))
    sleep(200) # Increased sleep duration

def d6():
    """
    Rolls a 6-sided die and displays the result.
    Also, uses speech to announce the result.
    """
    result = random.randint(1, 6)
    display.clear()
    display.scroll(result)
    speech.say(str(result))
    sleep(200) # Increased sleep duration

def d8():
    """
    Rolls an 8-sided die and displays the result.
    Also, uses speech to announce the result.
    """
    result = random.randint(1, 8)
    display.clear()
    display.scroll(result)
    speech.say(str(result))
    sleep(200) # Increased sleep duration

def d10():
    """
    Rolls a 10-sided die and displays the result.
    Also, uses speech to announce the result.
    """
    result = random.randint(1, 10)
    display.clear()
    display.scroll(result)
    speech.say(str(result))
    sleep(200) # Increased sleep duration

def d12():
    """
    Rolls a 12-sided die and displays the result.
    Also, uses speech to announce the result.
    """
    result = random.randint(1, 12)
    display.clear()
    display.scroll(result)
    speech.say(str(result))
    sleep(200) # Increased sleep duration

def d20():
    """
    Rolls a 20-sided die and displays the result.
    Also, uses speech to announce the result.
    """
    result = random.randint(1, 20)
    display.clear()
    display.scroll(result)
    speech.say(str(result))
    sleep(200) # Increased sleep duration

def d100():
    """
    Rolls a 100-sided die and displays the result.
    Also, uses speech to announce the result.
    """
    result = random.randint(1, 100)
    display.clear()
    display.scroll(result)
    speech.say(str(result))
    sleep(200) # Increased sleep duration

def on_button_pressed_a():
    """
    Handles the event when button A is pressed.
    Cycles positively through the 'options' list to select the next die type.
    """
    # Declare 'choice' as global to modify the global variable.
    global choice
    # Increment 'choice' and use the modulo operator (%) to wrap around
    # to the beginning of the list if the end is reached.
    # len(options) gives the total number of items in the list.
    choice = (choice + 1) % len(options)
    # Display and speak the newly selected option.
    print_currently_selected_option()

def on_button_pressed_b():
    """
    Handles the event when button B is pressed.
    Cycles negatively through the 'options' list to select the previous die type.
    """
    # Declare 'choice' as global to modify the global variable.
    global choice
    # Decrement 'choice'. To handle wrapping from the first item to the last,
    # we add len(options) before the modulo operation. This ensures the result
    # is always positive before taking the remainder.
    choice = (choice - 1 + len(options)) % len(options)
    # Display and speak the newly selected option.
    print_currently_selected_option()

def on_gesture_shake():
    """
    Handles the event when the Micro:bit is shaken.
    Rolls the currently selected type of die.
    """
    # Get the actual numeric value of the selected die from the 'options' list.
    current_dice_value = options[choice]

    # Use if/elif statements to call the correct dice rolling function
    # based on the 'current_dice_value'.
    if current_dice_value == 4:
        d4()
    elif current_dice_value == 6:
        d6()
    elif current_dice_value == 8:
        d8()
    elif current_dice_value == 10:
        d10()
    elif current_dice_value == 12:
        d12()
    elif current_dice_value == 20:
        d20()
    elif current_dice_value == 100:
        d100()

    # Clear the display after the roll and speech to ensure it's ready for the next interaction.
    display.clear()

# Initial call to display and speak the default selected option (D4) when the Micro:bit starts up.
print_currently_selected_option()

while True:
    if button_a.is_pressed():
        on_button_pressed_a()
    elif button_b.is_pressed():
        on_button_pressed_b()
    elif accelerometer.was_gesture('shake'):
        on_gesture_shake()
