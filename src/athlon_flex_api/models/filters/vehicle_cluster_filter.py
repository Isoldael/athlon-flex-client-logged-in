from __future__ import annotations

from athlon_flex_api.models.filters.filter import Filter


class VehicleClusterFilter(Filter):
    """Filters for loading the Vehicle Clusters."""

    Segment: str | None = "Cars"
    IncludeTaxInPrices: bool | None
    NumberOfKmPerMonth: int | None
    IncludeMileageCostsInPricing: bool | None
    IncludeFuelCostsInPricing: bool | None

    @staticmethod
    def from_profile(profile) -> VehicleClusterFilter:
        """Create a filter from a profile."""
        return VehicleClusterFilter(
            IncludeTaxInPrices=profile.requiresIncludeTaxInPrices,
            NumberOfKmPerMonth=profile.numberOfKmPerMonth,
            IncludeMileageCostsInPricing=profile.includeMileageCostsInPricing,
            IncludeFuelCostsInPricing=profile.includeFuelCostsInPricing,
        )


class NoFilter(VehicleClusterFilter):
    """Empty filter for loading all items."""

    pass
