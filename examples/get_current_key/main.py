from matrix_keyboard import MatrixKeyboard
import machine
import time

print("setup")

i2c = machine.I2C(0, scl=22, sda=21, freq=400000)

matrix_keyboard = MatrixKeyboard(i2c, i2c_address=MatrixKeyboard.DEFAULT_I2C_ADDRESS)

print("loop")

while True:
    matrix_keyboard.update()
    current_key = matrix_keyboard.get_pressed_key()
    if current_key:
        print("Current pressed key: ", current_key)
    time.sleep_ms(100)
