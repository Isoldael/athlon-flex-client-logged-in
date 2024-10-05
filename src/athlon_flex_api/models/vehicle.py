from __future__ import annotations

from pydantic import BaseModel

from athlon_flex_api.models.filters.filter import Filter
from athlon_flex_api.models.profile import Profile


class Vehicle(BaseModel):
    """Vehicle model.

    A Vehicle defines a specific vehicle configuration.
    For example one instance of the Opel Corsa E. It belongs to the VehicleCluster
    of its make and type.

    The class has a structure as defined by the API. Some details are optional,
    and only loaded when requested by the user (see DetailLevel).
    """

    class Details(BaseModel):
        """Vehicle details."""

        licensePlate: str
        color: str
        officialColor: str
        bodyType: str
        emission: float
        registrationDate: str
        registeredMileage: float
        transmissionType: str
        avgFuelConsumption: float
        typeSpareWheel: str
        additionPercentage: float

    class Pricing(BaseModel):
        """Vehicle pricing."""

        fiscalValueInEuro: float
        basePricePerMonthInEuro: float
        calculatedPricePerMonthInEuro: float
        pricePerKm: float
        fuelPricePerKm: float
        contributionInEuro: float
        expectedFuelCostPerMonthInEuro: float
        netCostPerMonthInEuro: float

    class Option(BaseModel):
        """Vehicle option."""

        id: str
        externalId: str
        optionName: str
        included: bool

    id: str
    make: str
    model: str
    type: str
    modelYear: int
    paintId: str | None = None
    externalPaintId: str | None = None
    priceInEuroPerMonth: float | None = None
    fiscalValueInEuro: float | None = None
    additionPercentage: float | None = None
    rangeInKm: int
    externalFuelTypeId: int
    externalTypeId: str
    imageUri: str
    isElectric: bool | None = None
    details: Details | None = None
    pricing: Pricing | None = None
    options: list[Option] | None = None

    def __str__(self) -> str:
        """Return the string representation of the vehicle."""
        return f"{self.make} {self.model} {self.type} {self.modelYear}"

    def details_request_params(self, profile: Profile) -> dict[str, str | int]:
        """Return the request parameters for loading the details."""
        bool_to_str = Filter.bool_to_str
        return {
            "Segment": "Cars",
            "VehicleId": self.id,
            "IncludeTaxInPrices": bool_to_str(profile.requiresIncludeTaxInPrices),
            "NumberOfKmPerMonth": profile.numberOfKmPerMonth,
            "IncludeMileageCostsInPricing": bool_to_str(
                profile.includeMileageCostsInPricing,
            ),
            "IncludeFuelCostsInPricing": bool_to_str(profile.includeFuelCostsInPricing),
            "ActualBudgetPerMonth": profile.budget.actualBudgetPerMonth,
        }
