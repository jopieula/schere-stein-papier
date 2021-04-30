def on_gesture_shake():
    global Hand
    Hand = randint(1, 3)
    if Hand == 1:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
    elif Hand == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    else:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_long_pressed():
    basic.show_string("Du hast das Geheimnis gefunden!")
    for index in range(4):
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_icon(IconNames.DIAMOND)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

Hand = 0
basic.show_string("Hallo das ist")
basic.show_string("Schere")
basic.show_string("Stein")
basic.show_string("Papier")
basic.show_icon(IconNames.HAPPY)
music.play_melody("C5 B A G F E D C ", 130)