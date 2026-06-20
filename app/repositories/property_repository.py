from abc import ABC, abstractmethod

from app.domain.property import Property


class PropertyRepository(ABC):

    @abstractmethod
    def add(self, property: Property) -> None:
        pass

    @abstractmethod
    def get_by_id(self, property_id):
        pass

    @abstractmethod
    def list(self) -> list[Property]:
        pass