from app.domain.entity import Entity
from app.repositories.entity_repository import EntityRepository


class EntityService:
    """
    Application service responsible for Entity operations.
    """

    def __init__(self, repository: EntityRepository):
        self._repository = repository

    def register_company(self, name: str) -> Entity:
        entity = Entity.create(
            entity_type="Company",
            name=name,
        )

        self._repository.add(entity)

        return entity

    def get(self, entity_id):
        return self._repository.get_by_id(entity_id)

    def list(self):
        return self._repository.list()