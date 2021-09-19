from typing import Any

from .device import Device


class RAM(Device):
    address_range = (b"\0x0000", b"\0xffff")

    def __init__(self):
        self.data = {}

    def read(self, address: bytes) -> Any:
        return self.data[address]

    def write(self, address: bytes, value: Any):
        self.data[address] = value
