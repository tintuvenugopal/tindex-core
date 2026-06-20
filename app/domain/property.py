from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Property:
    """
    Canonical Property.

    Represents a characteristic that belongs to an Entity.
    """

    id: UUID
    entity_type: str
    name: str
    data_type: str

    @staticmethod
    def create(
        entity_type: str,
        name: str,
        data_type: str,
    ) -> "Property":
        return Property(
            id=uuid4(),
            entity_type=entity_type,
            name=name,
            data_type=data_type,
        )