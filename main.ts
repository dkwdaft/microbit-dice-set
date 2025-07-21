function d8 () {
    basic.showNumber(randint(1, 8))
}
input.onButtonPressed(Button.A, function () {
	
})
function d100 () {
    basic.showNumber(randint(1, 100))
}
function d6 () {
    basic.showNumber(randint(1, 6))
}
function d4 () {
    basic.showNumber(randint(1, 4))
}
input.onButtonPressed(Button.B, function () {
	
})
function d10 () {
    basic.showNumber(randint(1, 10))
}
input.onGesture(Gesture.Shake, function () {
	
})
function d20 () {
    basic.showNumber(randint(1, 20))
}
function logic () {
	
}
function d12 () {
    basic.showNumber(randint(1, 12))
}
let choice = 0
let options = [
4,
6,
8,
10,
12,
20,
100
]
basic.showString("D" + options[choice])
