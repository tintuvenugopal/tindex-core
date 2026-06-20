from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Evidence:
    """
    Canonical Evidence.

    Supports one or more Observations.
    """

    id: UUID
    observation_id: UUID
    source: str
    reference: str

    @staticmethod
    def create(
        observation_id: UUID,
        source: str,
        reference: str,
    ) -> "Evidence":
        return Evidence(
            id=uuid4(),
            observation_id=observation_id,
            source=source,
            reference=reference,
        )