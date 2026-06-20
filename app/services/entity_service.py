from app.domain.entity import Entity
from app.repositories.entity_repository import EntityRepository


class EntityService:
    """
    Application service responsible for Entity operations.
    """

    def __init__(self, repository: EntityRepository):
        self._repository = repository

    def create(self, entity_type: str, name: str) -> Entity:
        entity = Entity.create(
            entity_type=entity_type,
            name=name,
        )

        self._repository.add(entity)

        return entity