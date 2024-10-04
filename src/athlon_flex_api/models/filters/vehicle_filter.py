from __future__ import annotations

from athlon_flex_api.models.filters.filter import Filter
from athlon_flex_api.models.profile import Profile


class VehicleFilter(Filter):
    """Filters for loading the Vehicle Clusters."""

    Segment: str | None = "Cars"
    Make: str | None
    Model: str | None
    IncludeTaxInPrices: bool | None
    NumberOfKmPerMonth: int | None
    IncludeMileageCostsInPricing: bool | None
    IncludeFuelCostsInPricing: bool | None
    SortBy: str | None = "PriceInEuro"
    MaxPricePerMonth: int | None
    ActualBudgetPerMonth: int | None

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
