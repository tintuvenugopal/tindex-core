from app.repositories.in_memory_entity_repository import (
    InMemoryEntityRepository,
)
from app.services.entity_service import EntityService


def test_create_entity():
    repository = InMemoryEntityRepository()
    service = EntityService(repository)

    entity = service.create(
        entity_type="Company",
        name="Apple Inc.",
    )

    assert repository.get_by_id(entity.id) == entity