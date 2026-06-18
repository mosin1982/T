from abc import ABC, abstractmethod

class TPlugin(ABC):
    name: str = "unnamed"
    version: str = "0.1.0"

    @abstractmethod
    def run(self, context: dict) -> dict:
        raise NotImplementedError
