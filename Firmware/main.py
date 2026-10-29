import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB          # Correct generic RGB library
from kmk.modules.layers import Layers       # Fixes the 'LT' layer tap error

keyboard = KMKKeyboard()

# Pin configuration for Seeed Studio XIAO RP2040
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.col_pins = (board.D4, board.D5, board.D6, board.D10, board.D9)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# Enable layers module
layers = Layers()
keyboard.modules.append(layers)

# Configure RGB lighting
rgb = RGB(
    pixel_pin=board.D8,    # Pin driving the LEDs
    num_pixels=20,         # Number of RGB LEDs
    hue_default=0,         # Default Hue (0 is Red)
    sat_default=255,       # Max saturation
    val_default=100,       # Initial brightness
)
keyboard.extensions.append(rgb)

# Two-layer keymap layout
keyboard.keymap = [
    # LAYER 0 (Default Base Layer)
    [
        KC.N1, KC.N2, KC.N3, KC.Q, KC.W,
        KC.N4, KC.N5, KC.N6, KC.E, KC.R,
        KC.N7, KC.N8, KC.N9, KC.A, KC.S,
        KC.LT(1, KC.N0), KC.LSHIFT, KC.LCTRL, KC.D, KC.SPACE,
    ],
    # LAYER 1 (Secondary Layer accessed via Layer Tap)
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ]
]

if __name__ == "__main__":
    keyboard.go()

