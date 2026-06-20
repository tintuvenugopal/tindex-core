from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Validation:
    """
    Canonical Validation.

    Represents the evaluation of a Claim.
    """

    id: UUID
    claim_id: UUID
    status: str
    rationale: str

    @staticmethod
    def create(
        claim_id: UUID,
        status: str,
        rationale: str,
    ) -> "Validation":
        return Validation(
            id=uuid4(),
            claim_id=claim_id,
            status=status,
            rationale=rationale,
        )