from app.repositories.in_memory_entity_repository import (
    InMemoryEntityRepository,
)
from app.services.entity_service import EntityService


def main():
    repository = InMemoryEntityRepository()
    service = EntityService(repository)

    entity = service.create(
        entity_type="Company",
        name="Apple Inc.",
    )

    print("Entity created")
    print(entity)

    print()
    print("Repository contents")
    print(repository.list())


if __name__ == "__main__":
    main()