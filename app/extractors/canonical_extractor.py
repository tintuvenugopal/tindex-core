from app.domain.entity import Entity
from app.domain.property import Property
from app.domain.observation import Observation
from datetime import datetime


class CanonicalExtractor:
    """
    Converts parsed markdown into canonical objects.
    """

    def extract(self, document: dict):
        company = document["Company"]
        financials = document["Financials"]

        entity = Entity.create(
            entity_type="Company",
            name=company["Name"],
        )

        revenue_property = Property.create(
            entity_type="Company",
            name="Revenue",
            data_type="Money",
        )

        revenue_observation = Observation.create(
            entity_id=entity.id,
            property_id=revenue_property.id,
            value=financials["Revenue"],
            observed_at=datetime.now(),
        )

        return {
            "entity": entity,
            "property": revenue_property,
            "observation": revenue_observation,
        }