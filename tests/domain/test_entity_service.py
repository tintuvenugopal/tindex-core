from app.repositories.in_memory_entity_repository import (
    InMemoryEntityRepository,
)
from app.services.entity_service import EntityService


def test_register_company():
    repository = InMemoryEntityRepository()
    service = EntityService(repository)

    entity = service.register_company("Apple Inc.")

    assert repository.get_by_id(entity.id) == entity
    assert entity.type == "Company"
    assert entity.name == "Apple Inc."