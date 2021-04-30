input.onGesture(Gesture.Shake, function () {
    Hand = randint(1, 3)
    if (Hand == 1) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    } else if (Hand == 2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    }
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    basic.showString("Du hast das Geheimnis gefunden!")
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Chessboard)
        basic.showIcon(IconNames.Diamond)
        basic.showIcon(IconNames.SmallDiamond)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    }
})
let Hand = 0
basic.showString("Hallo das ist")
basic.showString("Schere")
basic.showString("Stein")
basic.showString("Papier")
basic.showIcon(IconNames.Happy)
music.playMelody("C5 B A G F E D C ", 130)
