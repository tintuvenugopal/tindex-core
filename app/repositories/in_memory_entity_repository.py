from uuid import UUID

from app.domain.entity import Entity
from app.repositories.entity_repository import EntityRepository


class InMemoryEntityRepository(EntityRepository):
    def __init__(self):
        self._entities: dict[UUID, Entity] = {}

    def add(self, entity: Entity) -> None:
        self._entities[entity.id] = entity

    def get_by_id(self, entity_id: UUID):
        return self._entities.get(entity_id)

    def list(self) -> list[Entity]:
        return list(self._entities.values())