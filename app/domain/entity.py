from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Entity:
    """
    Canonical Entity.

    Represents a uniquely identifiable object within the Tindex domain.
    """

    id: UUID
    type: str
    name: str

    @staticmethod
    def create(entity_type: str, name: str) -> "Entity":
        return Entity(
            id=uuid4(),
            type=entity_type,
            name=name,
        )