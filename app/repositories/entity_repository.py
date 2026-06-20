from abc import ABC, abstractmethod

from app.domain.entity import Entity


class EntityRepository(ABC):
    """
    Repository interface for Entity persistence.
    """

    @abstractmethod
    def add(self, entity: Entity) -> None:
        pass

    @abstractmethod
    def get_by_id(self, entity_id):
        pass

    @abstractmethod
    def list(self) -> list[Entity]:
        pass