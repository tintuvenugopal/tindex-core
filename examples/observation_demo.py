from datetime import datetime

from app.domain.entity import Entity
from app.domain.property import Property
from app.domain.observation import Observation


def main():
    company = Entity.create(
        entity_type="Company",
        name="Apple Inc."
    )

    revenue = Property.create(
        entity_type="Company",
        name="Revenue",
        data_type="decimal",
    )

    observation = Observation.create(
        entity_id=company.id,
        property_id=revenue.id,
        value="391000000000",
        observed_at=datetime.now(),
    )

    print("\n=== Entity ===")
    print(company)

    print("\n=== Property ===")
    print(revenue)

    print("\n=== Observation ===")
    print(observation)


if __name__ == "__main__":
    main()