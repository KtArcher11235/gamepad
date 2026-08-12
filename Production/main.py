# ai code completion was used


import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_rgb_matrix import RGBMatrix


keyboard = KMKKeyboard()

keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.col_pins = (board.D4, board.D5, board.D6, board.D10, board.D9)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

rgb = RGBMatrix(
    led_pin=board.D8,
    led_count=20,
    brightness=0.3,
)
keyboard.extensions.append(rgb)

keyboard.keymap = [
        KC.N1, KC.N2, KC.N3, KC.Q,  KC.W,
        KC.N4, KC.N5, KC.N6, KC.E,  KC.R,
        KC.N7, KC.N8, KC.N9, KC.A,  KC.S,
        KC.LT(1, KC.N0), KC.LSHIFT, KC.LCTRL, KC.D, KC.SPACE,
]


if __name__ == "__main__":
    keyboard.go()