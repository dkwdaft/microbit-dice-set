def print_currently_selected_option():
 
    basic.show_string("D" + ("" + str(options[choice])))
def d8():
    basic.show_number(randint(1, 8))

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def d100():
    basic.show_number(randint(1, 100))
def d6():
    basic.show_number(randint(1, 6))
def d4():
    basic.show_number(randint(1, 4))

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def d10():
    basic.show_number(randint(1, 10))

def on_gesture_shake():
    if choice == 4:
        d4()
    elif choice == 6:
        d6()
    elif choice == 8:
        d8()
    elif choice == 10:
        d10()
    elif choice == 12:
        d12()
    elif choice == 20:
        d20()
    elif choice == 100:
        d100()

input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def d20():
    basic.show_number(randint(1, 20))
def d12():
    basic.show_number(randint(1, 12))
options: List[number] = []
options = [4, 6, 8, 10, 12, 20, 100]
choice = 0
print_currently_selected_option()