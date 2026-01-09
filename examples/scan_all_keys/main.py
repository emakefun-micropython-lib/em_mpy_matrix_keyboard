from matrix_keyboard import MatrixKeyboard
import machine

print("setup")

i2c = machine.I2C(0, scl=22, sda=21, freq=400000)

matrix_keyboard = MatrixKeyboard(i2c, i2c_address=MatrixKeyboard.DEFAULT_I2C_ADDRESS)

keys_dict = {
    MatrixKeyboard.KEY_1: "key 1",
    MatrixKeyboard.KEY_2: "key 2",
    MatrixKeyboard.KEY_3: "key 3",
    MatrixKeyboard.KEY_A: "key A",
    MatrixKeyboard.KEY_4: "key 4",
    MatrixKeyboard.KEY_5: "key 5",
    MatrixKeyboard.KEY_6: "key 6",
    MatrixKeyboard.KEY_B: "key B",
    MatrixKeyboard.KEY_7: "key 7",
    MatrixKeyboard.KEY_8: "key 8",
    MatrixKeyboard.KEY_9: "key 9",
    MatrixKeyboard.KEY_C: "key C",
    MatrixKeyboard.KEY_ASTERISK: "key *",
    MatrixKeyboard.KEY_0: "key 0",
    MatrixKeyboard.KEY_NUMBER_SIGN: "key #",
    MatrixKeyboard.KEY_D: "key D",
}

print("loop")

while True:
    matrix_keyboard.update()
    for key, value in keys_dict.items():
        if matrix_keyboard.pressed(key):
            print(value, "pressed")
        if matrix_keyboard.pressing(key):
            print(value, "pressing")
        if matrix_keyboard.released(key):
            print(value, "released")
