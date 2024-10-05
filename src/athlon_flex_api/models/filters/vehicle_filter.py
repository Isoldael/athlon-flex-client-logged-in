from __future__ import annotations

from athlon_flex_api.models.filters.filter import Filter
from athlon_flex_api.models.profile import Profile
from athlon_flex_api.models.vehicle import Vehicle


class VehicleFilter(Filter):
    """Filters for loading the Vehicle Clusters.

    Attributes:
        VehicleId: str | None
            Only used if the filter is used to load vehicle details.

    """

    Segment: str = "Cars"
    VehicleId: str | None = None
    Make: str | None = None
    Model: str | None = None
    IncludeTaxInPrices: bool | None = None
    NumberOfKmPerMonth: int | None = None
    IncludeMileageCostsInPricing: bool | None = None
    IncludeFuelCostsInPricing: bool | None = None
    SortBy: str = "PriceInEuro"
    MaxPricePerMonth: int | None = None
    ActualBudgetPerMonth: int | None = None

    @staticmethod
    def from_profile(make: str, model: str, profile: Profile) -> VehicleFilter:
        """Create a filter from a profile."""
        return VehicleFilter(
            Make=make,
            Model=model,
            IncludeTaxInPrices=profile.requiresIncludeTaxInPrices,
            NumberOfKmPerMonth=profile.numberOfKmPerMonth,
            IncludeMileageCostsInPricing=profile.includeMileageCostsInPricing,
            IncludeFuelCostsInPricing=profile.includeFuelCostsInPricing,
            MaxPricePerMonth=profile.budget.maxBudgetPerMonth,
            ActualBudgetPerMonth=profile.budget.actualBudgetPerMonth,
        )


class NoFilter(VehicleFilter):
    """Empty filter for loading all items."""

    pass
