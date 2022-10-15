# from machine import Pin
import time
import board
import keypad
import rotaryio
import digitalio
import usb_hid
from keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

print("yay")

# The keyboard object!  <_< <#<#<#<#<#<#<#123123456123
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
kb = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kb)  # We're in the US :)
consumer_control = ConsumerControl(usb_hid.devices)

# did you know you can put a rumble motor in a keyboard for haptic feedback?
# rumble = digitalio.DigitalInOut(board.GP17)
# rumble.direction = digitalio.Direction.OUTPUT

# or a shake detector to erase like an etchasketch?
# shake = digitalio.DigitalInOut(board.GP22)
# shake.direction = digitalio.Direction.INPUT
# shake.pull = digitalio.Pull.UP

# setup rotary encoders
updn = rotaryio.IncrementalEncoder(board.GP12, board.GP13)
lfri = rotaryio.IncrementalEncoder(board.GP14, board.GP15)

# blinky
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# key matrix setup
km = keypad.KeyMatrix(
    column_pins=(
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
    ),
    row_pins=(
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP28,
        board.GP27,
        board.GP26,
        board.GP22,
        board.GP21,
        board.GP20,
        board.GP19,
        board.GP18,
        board.GP17,
        board.GP16,
    ),
    columns_to_anodes=False,
    interval=0.025,
)

# define the main keymap
# special keys that do weird stuff defined else where are numbers > 500
# put +300 to press that key with shift
keys = (
    Keycode.ESCAPE,
    Keycode.TAB,
    502,  # quick
    Keycode.CONTROL,
    Keycode.Q,
    Keycode.A,
    Keycode.Z,
    Keycode.ALT,
    Keycode.W,
    Keycode.S,
    Keycode.X,
    606,  # FUNCTION SHIFT
    Keycode.E,  # othershift
    Keycode.D,
    Keycode.C,
    800,  # blank
    Keycode.R,
    Keycode.F,  # at some point i could make this another layer
    Keycode.V,  # refresh
    Keycode.LEFT_SHIFT,  # select all
    Keycode.T,
    Keycode.G,
    Keycode.B,
    Keycode.BACKSPACE,
    Keycode.KEYPAD_SEVEN,
    Keycode.KEYPAD_FOUR,
    Keycode.KEYPAD_ONE,
    Keycode.KEYPAD_ZERO,
    Keycode.KEYPAD_EIGHT,
    Keycode.KEYPAD_FIVE,
    Keycode.KEYPAD_TWO,
    613,  # fkeys
    Keycode.KEYPAD_NINE,
    Keycode.KEYPAD_SIX,
    Keycode.KEYPAD_THREE,
    700,  # mode
    Keycode.KEYPAD_ASTERISK,
    Keycode.EQUALS,
    Keycode.MINUS,
    606,  # super
    Keycode.Y,
    Keycode.H,
    Keycode.N,
    Keycode.SPACE,
    Keycode.U,
    Keycode.J,
    Keycode.M,
    Keycode.ENTER,
    Keycode.I,
    Keycode.K,
    Keycode.COMMA,
    606,  # FUNCTIONSHIFT
    Keycode.O,
    Keycode.L,
    Keycode.PERIOD,
    800,  # blank
    Keycode.P,
    Keycode.SEMICOLON,
    Keycode.FORWARD_SLASH,
    614,
    Keycode.DELETE,
    Keycode.QUOTE,
    Keycode.BACKSLASH,
    Keycode.WINDOWS,
)

# define the other keymaps you can switch to
sup = (
    Keycode.ESCAPE,
    Keycode.TAB,
    502,  # quick
    Keycode.CONTROL,
    Keycode.ONE + 300,
    Keycode.TWO + 300,
    Keycode.FIVE + 300,
    Keycode.ALT,
    Keycode.SIX + 300,
    Keycode.FOUR + 300,
    Keycode.FIVE + 300,
    606,  # FUNCTION SHIFT
    Keycode.THREE + 300,  # othershift
    Keycode.SEVEN + 300,
    Keycode.EIGHT + 300,
    800,
    Keycode.LEFT_BRACKET,
    Keycode.LEFT_BRACKET + 300,
    Keycode.NINE + 300,
    Keycode.COMMA + 300,
    Keycode.RIGHT_BRACKET,
    Keycode.RIGHT_BRACKET + 300,
    Keycode.ZERO + 300,
    Keycode.PERIOD + 300,
    Keycode.SEVEN,
    Keycode.FOUR,
    Keycode.ONE,
    Keycode.ZERO,
    Keycode.EIGHT,
    Keycode.FIVE,
    Keycode.TWO,
    613,  # fkeys
    Keycode.NINE,
    Keycode.SIX,
    Keycode.THREE,
    700,  # mode
    608,  # screenshot
    504,  # notepad
    612,  # tasks
    606,  # super
    Keycode.PAGE_UP,
    Keycode.PAGE_DOWN,
    Keycode.N,
    Keycode.SPACE,
    Keycode.HOME,
    Keycode.LEFT_ARROW,
    Keycode.M,
    Keycode.ENTER,
    Keycode.UP_ARROW,
    Keycode.DOWN_ARROW,
    Keycode.COMMA,
    606,  # FUNCTIONSHIFT
    Keycode.END,
    Keycode.RIGHT_ARROW,
    Keycode.PERIOD,
    800,  # blank
    Keycode.P,
    Keycode.SEMICOLON,
    Keycode.FORWARD_SLASH,
    615,  # <3
    Keycode.INSERT,
    Keycode.GRAVE_ACCENT,
    Keycode.BACKSLASH,
    Keycode.WINDOWS,
)

fun = (
    Keycode.ESCAPE,
    Keycode.TAB,
    502,  # quick
    Keycode.CONTROL,
    Keycode.ONE + 300,
    Keycode.TWO + 300,
    Keycode.FIVE + 300,
    Keycode.ALT,
    Keycode.SIX + 300,
    Keycode.FOUR + 300,
    Keycode.FIVE + 300,
    606,  # FUNCTION SHIFT
    Keycode.THREE + 300,  # othershift
    Keycode.SEVEN + 300,
    Keycode.EIGHT + 300,
    800,
    Keycode.LEFT_BRACKET,
    Keycode.LEFT_BRACKET + 300,
    Keycode.NINE + 300,
    Keycode.COMMA + 300,
    Keycode.RIGHT_BRACKET,
    Keycode.RIGHT_BRACKET + 300,
    Keycode.ZERO + 300,
    Keycode.PERIOD + 300,
    Keycode.F7,
    Keycode.F4,
    Keycode.F1,
    Keycode.ZERO,
    Keycode.F8,
    Keycode.F5,
    Keycode.F2,
    613,  # fkeys
    Keycode.F9,
    Keycode.F6,
    Keycode.F3,
    700,  # mode
    Keycode.F10,
    Keycode.F11,
    Keycode.F12,
    606,  # super
    Keycode.PAGE_UP,
    Keycode.PAGE_DOWN,
    Keycode.N,
    Keycode.SPACE,
    Keycode.HOME,
    Keycode.LEFT_ARROW,
    Keycode.M,
    Keycode.ENTER,
    Keycode.UP_ARROW,
    Keycode.DOWN_ARROW,
    Keycode.COMMA,
    606,  # FUNCTIONSHIFT
    Keycode.END,
    Keycode.RIGHT_ARROW,
    Keycode.PERIOD,
    800,  # blank
    Keycode.P,
    Keycode.SEMICOLON,
    Keycode.FORWARD_SLASH,
    614,  # <_<
    Keycode.INSERT,
    Keycode.GRAVE_ACCENT,
    Keycode.BACKSLASH,
    Keycode.WINDOWS,
)

game = (
    Keycode.ESCAPE,
    Keycode.TAB,
    Keycode.Z,
    Keycode.CONTROL,  #
    Keycode.T,
    Keycode.LEFT_SHIFT,
    Keycode.CONTROL,
    Keycode.ALT,
    Keycode.Q,
    Keycode.A,
    Keycode.B,
    606,  # FUNCTION SHIFT
    Keycode.W,  # othershift
    Keycode.S,
    Keycode.V,
    800,  # blank
    Keycode.E,
    Keycode.D,  # at some point i could make this another layer
    Keycode.ALT,  # refresh
    Keycode.C,  # select all
    Keycode.R,
    Keycode.F,
    Keycode.X,
    Keycode.SPACE,
    Keycode.SEVEN,
    Keycode.FOUR,
    Keycode.ONE,
    Keycode.ZERO,
    Keycode.EIGHT,
    Keycode.FIVE,
    Keycode.TWO,
    613,  # fkeys
    Keycode.NINE,
    Keycode.SIX,
    Keycode.THREE,
    700,  # mode
    Keycode.KEYPAD_ASTERISK,
    Keycode.EQUALS,
    Keycode.MINUS,
    606,  # super
    Keycode.Y,
    Keycode.H,
    Keycode.N,
    Keycode.SPACE,
    Keycode.U,
    Keycode.J,
    Keycode.M,
    Keycode.ENTER,
    Keycode.I,
    Keycode.K,
    Keycode.COMMA,
    606,  # FUNCTIONSHIFT
    Keycode.O,
    Keycode.L,
    Keycode.PERIOD,
    800,  # blank
    Keycode.P,
    Keycode.SEMICOLON,
    Keycode.FORWARD_SLASH,
    614,
    Keycode.DELETE,
    Keycode.QUOTE,
    Keycode.BACKSLASH,
    Keycode.WINDOWS,
)


# shook = None


def Tap(key):
    kb.press(key)
    time.sleep(0.0001)
    kb.release(key)


def vTap(key):
    consumer_control.press(key)
    time.sleep(0.0001)
    consumer_control.release()


tim = 0
base = keys
layer = base
# pulse = 0
elapse = 0
# dopulse = False
rpress = False
lpress = False

mode = 0
booter = 1

while True:
    st = time.monotonic()

    # if shook != shake.value:
    #     print(shake.value)
    #     kb.send(Keycode.BACKSPACE)
    # shook = shake.value
    if mode == 1:
        base = game
    if mode == 0:
        base = keys

    if updn.position < 0:
        Tap(Keycode.UP_ARROW)
    if updn.position > 0:
        Tap(Keycode.DOWN_ARROW)
    updn.position = 0

    if lfri.position > 0:
        if rpress:
            vTap(ConsumerControlCode.VOLUME_INCREMENT)
        else:
            Tap(Keycode.RIGHT_ARROW)
    if lfri.position < 0:
        if rpress:
            vTap(ConsumerControlCode.VOLUME_DECREMENT)
        else:
            Tap(Keycode.LEFT_ARROW)
    lfri.position = 0

    event = km.events.get()
    if event:
        if layer[event.key_number] < 300:  # normal key event
            if event.pressed:
                print(event.key_number)
                kb.press(layer[event.key_number])

            if event.released:
                kb.release(layer[event.key_number])
        elif layer[event.key_number] < 500:  # shift event = +300 key
            if event.pressed:
                kb.press(Keycode.LEFT_SHIFT)
                kb.press(layer[event.key_number] - 300)

            if event.released:
                kb.release(layer[event.key_number] - 300)
                kb.release(Keycode.LEFT_SHIFT)
        else:  # special numbered keys
            if layer[event.key_number] == 700:
                if event.pressed:
                    mode += 1
                    if mode > 1:
                        mode = 0
                if mode == 1:
                    layer = game
                if mode == 0:
                    layer = keys
            if layer[event.key_number] == 614:  # <_<
                if event.pressed:
                    kb.press(Keycode.LEFT_SHIFT)
                    kb.press(Keycode.COMMA)
                    kb.release(Keycode.COMMA)
                    kb.press(Keycode.MINUS)
                    kb.press(Keycode.COMMA)
                    kb.release_all()
            if layer[event.key_number] == 615:  # <3
                if event.pressed:
                    kb.press(Keycode.LEFT_SHIFT)
                    kb.press(Keycode.COMMA)
                    kb.release(Keycode.COMMA)
                    kb.release(Keycode.LEFT_SHIFT)
                    kb.press(Keycode.THREE)
                    kb.release_all()
            if layer[event.key_number] == 502:  # quicksave
                if event.pressed:
                    kb.press(Keycode.CONTROL)
                    kb.press(Keycode.K)
                    kb.release(Keycode.K)
                    kb.press(Keycode.D)
                    kb.release(Keycode.D)
                    kb.press(Keycode.LEFT_SHIFT)
                    kb.press(Keycode.S)
                    kb.release_all()
            if layer[event.key_number] == 501:  # alttab
                if event.pressed:
                    kb.press(Keycode.ALT)
                    kb.press(Keycode.TAB)
                    kb.release(Keycode.ALT)
                    kb.release(Keycode.TAB)
            if layer[event.key_number] == 500:  # ctltab
                if event.pressed:
                    kb.press(Keycode.CONTROL)
                    kb.press(Keycode.TAB)
                    kb.release(Keycode.CONTROL)
                    kb.release(Keycode.TAB)
            if layer[event.key_number] == 506:  # rotary pushbuttons
                if event.pressed:
                    rpress = True
                elif event.released:
                    rpress = False
            if layer[event.key_number] == 507:
                if event.pressed:
                    lpress = True
                elif event.released:
                    lpress = False
            if layer[event.key_number] == 613:  # fun
                if event.pressed:
                    layer = fun
                elif event.released:
                    layer = base
                    kb.release_all()
            if layer[event.key_number] == 606:
                # super layer switch
                if event.pressed:
                    layer = sup
                elif event.released:
                    layer = base
                    kb.release_all()
            if layer[event.key_number] == 602:  # cut
                if event.pressed:
                    kb.press(Keycode.CONTROL)
                    kb.press(Keycode.X)
                    kb.release(Keycode.CONTROL)
                    kb.release(Keycode.X)
            if layer[event.key_number] == 603:  # copy
                if event.pressed:
                    kb.press(Keycode.CONTROL)
                    kb.press(Keycode.C)
                    kb.release(Keycode.CONTROL)
                    kb.release(Keycode.C)
            if layer[event.key_number] == 607:  # paste
                if event.pressed:
                    kb.press(Keycode.CONTROL)
                    kb.press(Keycode.V)
                    kb.release(Keycode.CONTROL)
                    kb.release(Keycode.V)
            if layer[event.key_number] == 609:  # undo
                if event.pressed:
                    kb.press(Keycode.CONTROL)
                    kb.press(Keycode.Z)
                    kb.release(Keycode.CONTROL)
                    kb.release(Keycode.Z)
            if layer[event.key_number] == 604:  # redo
                if event.pressed:
                    kb.press(Keycode.CONTROL)
                    kb.press(Keycode.Y)
                    kb.release(Keycode.CONTROL)
                    kb.release(Keycode.Y)
            if layer[event.key_number] == 612:  # tasks
                if event.pressed:
                    kb.press(Keycode.CONTROL)
                    kb.press(Keycode.SHIFT)
                    kb.press(Keycode.ESCAPE)
                    kb.release_all()
            if layer[event.key_number] == 608:  # screenshot
                if event.pressed:
                    kb.press(Keycode.WINDOWS)
                    kb.press(Keycode.SHIFT)
                    kb.press(Keycode.S)
                    kb.release_all()
            if layer[event.key_number] == 611:  # select all
                if event.pressed:
                    kb.press(Keycode.CONTROL)
                    kb.press(Keycode.A)
                    kb.release_all()
            if layer[event.key_number] == 504:  # run notepad
                if event.pressed:
                    kb.press(Keycode.WINDOWS)
                    kb.press(Keycode.R)
                    kb.release(Keycode.WINDOWS)
                    kb.release(Keycode.R)
                    time.sleep(0.1)
                    kb.send(
                        Keycode.N, Keycode.O, Keycode.T, Keycode.E, Keycode.P, Keycode.A
                    )
                    kb.send(Keycode.D, Keycode.PERIOD, Keycode.E, Keycode.X)
                    kb.send(Keycode.E)
                    time.sleep(0.1)
                    kb.send(Keycode.ENTER)

    elapse = time.monotonic() - st

    #  if pulse > 0:
    #      pulse -= elapse
    #      rumble.value = True
    # else:
    #     rumble.value = False

    # led readout for mode switching
    # and pulse the led at startup so we know its working right
    tim += elapse
    if mode == 0:
        if booter > 0:
            booter -= elapse
            if tim > 0.05:
                tim = 0
                led.value = not led.value
        else:
            led.value = False
    if mode == 1 and tim > 0.2:
        tim = 0
        led.value = not led.value
