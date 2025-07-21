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
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def d20():
    basic.show_number(randint(1, 20))
def logic():
    pass
def d12():
    basic.show_number(randint(1, 12))
choice = 0
options = [4, 6, 8, 10, 12, 20, 100]
basic.show_string("D" + str(options[choice]))