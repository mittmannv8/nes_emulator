from abc import ABC, abstractmethod, abstractproperty
from typing import Any, Tuple


class Device(ABC):
    @abstractproperty
    def address_range() -> Tuple[bytes]:
        return ...

    @abstractmethod
    def read(cls, address: bytes) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def write(cls, address: bytes, value: Any):
        raise NotImplementedError()
