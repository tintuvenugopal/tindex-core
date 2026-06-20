from app.repositories.in_memory_entity_repository import (
    InMemoryEntityRepository,
)
from app.services.entity_service import EntityService


def main():
    repository = InMemoryEntityRepository()
    service = EntityService(repository)

    apple = service.register_company("Apple Inc.")
    microsoft = service.register_company("Microsoft")

    print("\nCompanies\n")

    for company in service.list():
        print(company)


if __name__ == "__main__":
    main()