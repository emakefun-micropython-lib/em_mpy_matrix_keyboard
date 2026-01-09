from micropython import const
import struct

__version__ = "1.0.1"


class MatrixKeyboard:
    DEFAULT_I2C_ADDRESS: int = const(0x65)

    KEY_0: int = const(1 << 7)
    KEY_1: int = const(1 << 0)
    KEY_2: int = const(1 << 4)
    KEY_3: int = const(1 << 8)
    KEY_4: int = const(1 << 1)
    KEY_5: int = const(1 << 5)
    KEY_6: int = const(1 << 9)
    KEY_7: int = const(1 << 2)
    KEY_8: int = const(1 << 6)
    KEY_9: int = const(1 << 10)
    KEY_A: int = const(1 << 12)
    KEY_B: int = const(1 << 13)
    KEY_C: int = const(1 << 14)
    KEY_D: int = const(1 << 15)
    KEY_ASTERISK: int = const(1 << 3)
    KEY_NUMBER_SIGN: int = const(1 << 11)

    _KEY_VALUE_MAP = (
        (KEY_1, "1"),
        (KEY_2, "2"),
        (KEY_3, "3"),
        (KEY_A, "A"),
        (KEY_4, "4"),
        (KEY_5, "5"),
        (KEY_6, "6"),
        (KEY_B, "B"),
        (KEY_7, "7"),
        (KEY_8, "8"),
        (KEY_9, "9"),
        (KEY_C, "C"),
        (KEY_ASTERISK, "*"),
        (KEY_0, "0"),
        (KEY_NUMBER_SIGN, "#"),
        (KEY_D, "D"),
    )

    def __init__(self, i2c, i2c_address):
        self._i2c = i2c
        self._i2c_address = i2c_address
        self._key_states = 0
        self._last_key_states = 0

    def _read_key_states(self):
        return struct.unpack(
            "<H", self._i2c.readfrom(MatrixKeyboard.DEFAULT_I2C_ADDRESS, 2)
        )[0]

    def update(self):
        key_state = -1
        count: int = const(4)

        while key_state == -1:
            key_state = self._read_key_states()
            for i in range(count):
                if key_state != self._read_key_states():
                    key_state = -1
                    break

        self._last_key_states = self._key_states
        self._key_states = key_state

    def key_states(self):
        return self._key_states

    def pressed(self, key):
        return self._last_key_states & key == 0 and self._key_states & key != 0

    def pressing(self, key):
        return self._last_key_states & key != 0 and self._key_states & key != 0

    def released(self, key):
        return self._last_key_states & key != 0 and self._key_states & key == 0

    def get_pressed_key(self):
        for key_const, key_value in self._KEY_VALUE_MAP:
            if (
                self._last_key_states & key_const == 0
                and self._key_states & key_const != 0
            ):
                return key_value
        return ""
