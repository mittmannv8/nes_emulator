from typing import Any

from .device import Device


class BUS:
    def __init__(self) -> None:
        self.devices = dict()

    def add_device(self, device: Device):
        self.devices[device.address_range] = device

    def remove_device(self, device: Device):
        del self.devices[device.address_range]

    def _get_device_by_range(self, address) -> Device:
        key = next((k for k in self.devices.keys() if k[0] <= address <= k[1]), None)
        if not key:
            raise ValueError("Address not found")
        return self.devices[key]

    def read(self, address: bytes) -> Any:
        device = self._get_device_by_range(address)
        return device.read(address)

    def write(self, address: bytes, value: Any) -> None:
        device = self._get_device_by_range(address)
        return device.write(address, value)
