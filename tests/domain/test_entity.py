from app.domain.entity import Entity


def test_create_entity():
    entity = Entity.create(
        entity_type="Company",
        name="Apple Inc."
    )

    assert entity.type == "Company"
    assert entity.name == "Apple Inc."
    assert entity.id is not None