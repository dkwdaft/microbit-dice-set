function print_currently_selected_option() {
    basic.showString("D" + ("" + ("" + options[choice])))
}

function d8() {
    basic.showNumber(randint(1, 8))
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    //  cycle positively through the options and change the choice variable when cycling 
    
})
function d100() {
    basic.showNumber(randint(1, 100))
}

function d6() {
    basic.showNumber(randint(1, 6))
}

function d4() {
    basic.showNumber(randint(1, 4))
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    //  cycle negatively through the options and change the choice variable when cycling
    
})
function d10() {
    basic.showNumber(randint(1, 10))
}

input.onGesture(Gesture.Shake, function on_gesture_shake() {
    if (choice == 4) {
        d4()
    } else if (choice == 6) {
        d6()
    } else if (choice == 8) {
        d8()
    } else if (choice == 10) {
        d10()
    } else if (choice == 12) {
        d12()
    } else if (choice == 20) {
        d20()
    } else if (choice == 100) {
        d100()
    }
    
})
function d20() {
    basic.showNumber(randint(1, 20))
}

function d12() {
    basic.showNumber(randint(1, 12))
}

let choice = 0
let options : number[] = []
options = [4, 6, 8, 10, 12, 20, 100]
print_currently_selected_option()
