choice = 0
options: List[number] = []
def print_currently_selected_option():
    # Displays "D" followed by the selected dice value (e.g., "D6", "D20")
    basic.show_string("D" + str(options[choice]))
def d8():
    basic.show_number(randint(1, 8))

def on_button_pressed_a():
    global choice
    # Cycle positively through the options.
    # The % operator works similarly for wrapping around the array.
    choice = (choice + 1) % len(options)
    print_currently_selected_option()
input.on_button_pressed(Button.A, on_button_pressed_a)

def d100():
    basic.show_number(randint(1, 100))
def d6():
    basic.show_number(randint(1, 6))
def d4():
    basic.show_number(randint(1, 4))

def on_button_pressed_b():
    global choice
    # Cycle negatively through the options.
    # Adding options.length before % ensures a positive result for negative numbers.
    choice = (choice - 1 + len(options)) % len(options)
    print_currently_selected_option()
input.on_button_pressed(Button.B, on_button_pressed_b)

def d10():
    basic.show_number(randint(1, 10))

def on_gesture_shake():
    currentDiceValue = options[choice]
    # Get the value from the array
    if currentDiceValue == 4:
        d4()
    elif currentDiceValue == 6:
        d6()
    elif currentDiceValue == 8:
        d8()
    elif currentDiceValue == 10:
        d10()
    elif currentDiceValue == 12:
        d12()
    elif currentDiceValue == 20:
        d20()
    elif currentDiceValue == 100:
        d100()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def d20():
    basic.show_number(randint(1, 20))
def d12():
    basic.show_number(randint(1, 12))
# Initial setup when the Micro:bit starts
options = [4, 6, 8, 10, 12, 20, 100]
print_currently_selected_option()