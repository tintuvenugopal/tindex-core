from uuid import UUID

from app.domain.property import Property
from app.repositories.property_repository import PropertyRepository


class InMemoryPropertyRepository(PropertyRepository):

    def __init__(self):
        self._properties: dict[UUID, Property] = {}

    def add(self, property: Property) -> None:
        self._properties[property.id] = property

    def get_by_id(self, property_id: UUID):
        return self._properties.get(property_id)

    def list(self) -> list[Property]:
        return list(self._properties.values())