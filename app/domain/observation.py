from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Observation:
    """
    Canonical Observation.

    Records the observed value of a Property for an Entity.
    """

    id: UUID
    entity_id: UUID
    property_id: UUID
    value: str
    observed_at: datetime

    @staticmethod
    def create(
        entity_id: UUID,
        property_id: UUID,
        value: str,
        observed_at: datetime,
    ) -> "Observation":
        return Observation(
            id=uuid4(),
            entity_id=entity_id,
            property_id=property_id,
            value=value,
            observed_at=observed_at,
        )