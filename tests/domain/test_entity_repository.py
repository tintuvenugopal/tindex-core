from app.domain.entity import Entity
from app.repositories.in_memory_entity_repository import (
    InMemoryEntityRepository,
)


def test_add_and_get_entity():
    repo = InMemoryEntityRepository()

    entity = Entity.create(
        entity_type="Company",
        name="Apple Inc."
    )

    repo.add(entity)

    loaded = repo.get_by_id(entity.id)

    assert loaded == entity