from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property
from typing import ClassVar

from requests import Session

from athlon_flex_api.models.filters.vehicle_cluster_filter import VehicleClusterFilter
from athlon_flex_api.models.filters.vehicle_filter import (
    VehicleFilter,
)
from athlon_flex_api.models.profile import Profile
from athlon_flex_api.models.vehicle import Vehicles
from athlon_flex_api.models.vehicle_cluster import VehicleClusters


@dataclass
class AthlonFlexApi:
    """Athlon Flex API client."""

    email: str
    password: str
    session: Session = field(init=False)

    BASE_URL: ClassVar[str] = "https://flex.athlon.com/api/v1"

    def __post_init__(self) -> None:
        """Initialize the API client.

        Create a new session and login to the API.
        """
        self.session = Session()
        self._login()

    def _login(self) -> None:
        """Login to the Athlon Flex API.

        Uses username and password to login to the API.
        Connection details are stored in the session.
        """
        endpoint = "MemberLogin"

        response = self.session.post(
            self._url(endpoint),
            json={"username": self.email, "password": self.password},
        )
        response.raise_for_status()

    def _url(self, endpoint: str) -> str:
        return f"{self.BASE_URL}/{endpoint}"

    @cached_property
    def profile(self) -> Profile:
        """Get the profile of the user."""
        endpoint = "MemberProfile"

        response = self.session.get(self._url(endpoint))
        response.raise_for_status()

        return Profile(**response.json())

    def vehicle_clusters(
        self,
        filter: VehicleClusterFilter | None = None,
    ) -> VehicleClusters:
        """Load all clusters that have at least one vehicle available.

        If a filter is not provided, result is filtered based on profile.
        If a filter is provided, result is filtered based on the filter.
            There exists a special NoFilter subclass to load all clusters.
        """
        filter = filter or VehicleClusterFilter.from_profile(self.profile)
        endpoint = "VehicleCluster"
        response = self.session.get(
            self._url(endpoint), params=filter.to_request_params()
        )
        response.raise_for_status()
        return VehicleClusters(vehicle_clusters=response.json())

    def vehicles(
        self,
        make: str,
        model: str,
        filter: VehicleFilter | None = None,
    ) -> Vehicles:
        """Load all available vehicles of a specific make and model (ie a cluster).

        If a filter is not provided, result is filtered based on profile.
        If a filter is provided, result is filtered based on the filter.
            There exists a special NoFilter subclass to load all vehicles.
        """
        filter = filter or VehicleFilter.from_profile(make, model, self.profile)
        endpoint = "VehicleVariation"
        response = self.session.get(
            self._url(endpoint), params=filter.to_request_params()
        )
        response.raise_for_status()
        return Vehicles(make=make, model=model, vehicles=response.json())

    def all_vehicles(
        self,
        vehicle_cluster_filter: VehicleClusterFilter,
        vehicle_filter: VehicleFilter,
    ) -> Vehicles:
        """Todo: Load all vehicles of all clusters.

        After loading the clusters, load all vehicles of each cluster in parallel.
        Use aiohttp instead of requests
        """
        pass
