#btw this whole thing is a bunch of vibecoded slop. whatever.
# -------------------------------------------------------------
# STEP 1: IMPORT THE INGREDIENTS
# We need to bring in the tools required to make the keyboard work.
# -------------------------------------------------------------
import board  # Gives us access to the physical pin names on the XIAO chip
from kmk.kmk_keyboard import KMKKeyboard  # The core keyboard logic engine
from kmk.keys import KC  # The master list of all key codes (like letters, symbols)
from kmk.scanners import DiodeOrientation  # Tells the code how the diodes are pointing

# This brings in the special software package needed to control NeoPixel LEDs
from kmk.extensions.peg_rgb_matrix import RGBMatrix

# -------------------------------------------------------------
# STEP 2: INITIALIZE THE KEYBOARD
# This sets up our main keyboard object which holds all our settings.
# -------------------------------------------------------------
keyboard = KMKKeyboard()

# -------------------------------------------------------------
# STEP 3: PIN CONFIGURATION (MATCHING YOUR SCHEMATIC)
# This maps the code to the exact physical holes on your Seeed Studio XIAO.
# -------------------------------------------------------------

# These are your 4 rows. They match r1, r2, r3, r4 on your schematic drawing.
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)

# These are your 5 columns. They match c1, c2, c3, c4, c5 on your schematic drawing.
# Notice how we put D10 and D9 at the end to match your specific drawing lines!
keyboard.col_pins = (board.D4, board.D5, board.D6, board.D10, board.D9)

# ROW2COL means the electricity flows from the Row pin, through the diode, into the Column pin.
# This matches your exact schematic without having to desolder or turn anything around.
keyboard.diode_orientation = DiodeOrientation.ROW2COL 

# -------------------------------------------------------------
# STEP 4: RGB LIGHTING SETUP
# This tells the brain how many lights you have, where they are, and how bright to be.
# -------------------------------------------------------------
rgb_ext = RGBMatrix(
    led_pin=board.D8,  # You wired 'din' to Pin D8, so we tell the code to send data there.
    led_count=20,     # You have exactly 20 NeoPixels chained together.
    brightness=0.3,   # 30% brightness. Keeps the board safe from pulling too much power.
)
# This line actually activates the lighting software inside the keyboard system.
keyboard.extensions.append(rgb_ext)

# -------------------------------------------------------------
# STEP 5: KEYMAPS AND LAYERS
# This is where we define what happens when you press a button.
# -------------------------------------------------------------
keyboard.keymap = [
    
    # --- LAYER 0: YOUR STANDARD TYPING LAYER ---
    # This is what your keyboard types normally when you just plug it in.
    [
        # ROW 1 (r1)
        KC.N1, KC.N2, KC.N3, KC.Q,  KC.W,       
        # ROW 2 (r2)
        KC.N4, KC.N5, KC.N6, KC.E,  KC.R,       
        # ROW 3 (r3)
        KC.N7, KC.N8, KC.N9, KC.A,  KC.S,       
        # ROW 4 (r4)
        # KC.LT(1, KC.N0) means: TAP quickly to type the number "0", 
        # or HOLD it down to temporarily switch to your secret RGB adjustments (Layer 1).
        KC.LT(1, KC.N0), KC.LSHIFT, KC.LCTRL, KC.D, KC.SPACE, 
    ],
    
    # --- LAYER 1: YOUR SECRET RGB ADJUSTMENT LAYER ---
    # This layer is ONLY active while you are holding down the bottom-left key.
    [
        # Pressing the top row keys while holding down your 0 key allows you to modify the lights:
        KC.RGB_TOG,     # Key 1: Turns the lights completely On/Off
        KC.RGB_ANI,     # Key 2: Changes the pattern (Static -> Rainbow -> Breathing)
        KC.RGB_M_MOD,   # Key 3: Changes direction/speed behavior
        KC.TRNS,        # Key Q: Does nothing extra, falls back to normal typing
        KC.TRNS,        # Key W: Does nothing extra, falls back to normal typing
        
        # Row 2 (Does nothing extra, falls back to normal typing)
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # Row 3 (Does nothing extra, falls back to normal typing)
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # Row 4 (Does nothing extra, falls back to normal typing)
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    ]
]

# -------------------------------------------------------------
# STEP 6: START THE KEYBOARD LOOP
# This infinite loop checks if buttons are pressed over and over forever.
# -------------------------------------------------------------
if __name__ == "__main__":
    keyboard.go()
