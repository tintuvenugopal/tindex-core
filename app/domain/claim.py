from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Claim:
    """
    Canonical Claim.

    Represents a conclusion derived from one or more observations
    supported by evidence.
    """

    id: UUID
    statement: str

    @staticmethod
    def create(statement: str) -> "Claim":
        return Claim(
            id=uuid4(),
            statement=statement,
        )