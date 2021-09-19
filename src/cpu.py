from typing import Any

from bus import BUS
from device import Device


class CPU:
    def __init__(self):
        self.__bus = None

        # registers
        self.accumulator = 0
        self.x_reg = 0
        self.y_reg = 0
        self.status = 0

        self.stack_pointer = 0
        self.program_counter = 0

    def connect_bus(self, bus: BUS):
        self.__bus = bus

    def __read(self, address: bytes) -> Any:
        return self.__bus.read(address)

    def __write(self, address: bytes, value: Any):
        self.__bus.read(address, value)
