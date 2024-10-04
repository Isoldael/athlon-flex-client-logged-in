from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Awaitable, ClassVar, TypeVar

from aiohttp import ClientSession
from async_property import async_cached_property

from athlon_flex_api.models.filters.vehicle_cluster_filter import VehicleClusterFilter
from athlon_flex_api.models.filters.vehicle_filter import (
    VehicleFilter,
)
from athlon_flex_api.models.profile import Profile
from athlon_flex_api.models.vehicle import Vehicles
from athlon_flex_api.models.vehicle_cluster import VehicleClusters

T = TypeVar("T")


@dataclass
class AthlonFlexApi:
    """Athlon Flex API client."""

    email: str
    password: str
    session: ClientSession = field(init=False)

    BASE_URL: ClassVar[str] = "https://flex.athlon.com/api/v1"

    def __post_init__(self) -> None:
        """Initialize the API client.

        Create a new session and login to the API.
        """
        self.await_(self._init())

    async def _init(self) -> None:
        self.session = ClientSession()
        await self._login()

    async def _login(self) -> None:
        """Login to the Athlon Flex API.

        Uses username and password to login to the API.
        Connection details are stored in the session.
        """
        endpoint = "MemberLogin"

        response = await self.session.post(
            self._url(endpoint),
            json={"username": self.email, "password": self.password},
        )
        response.raise_for_status()

    def _url(self, endpoint: str) -> str:
        return f"{self.BASE_URL}/{endpoint}"

    @async_cached_property
    async def profile(self) -> Profile:
        """Get the profile of the user."""
        endpoint = "MemberProfile"

        response = await self.session.get(self._url(endpoint))
        response.raise_for_status()

        return Profile(**await response.json())

    async def vehicle_clusters(
        self,
        filter: VehicleClusterFilter | None = None,
    ) -> VehicleClusters:
        """Load all clusters that have at least one vehicle available.

        If a filter is not provided, result is filtered based on profile.
        If a filter is provided, result is filtered based on the filter.
            There exists a special NoFilter subclass to load all clusters.
        """
        filter = filter or VehicleClusterFilter.from_profile(await self.profile)
        endpoint = "VehicleCluster"
        response = await self.session.get(
            self._url(endpoint), params=filter.to_request_params()
        )
        response.raise_for_status()
        return VehicleClusters(vehicle_clusters=await response.json())

    async def vehicles_of_make_and_model(
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
        filter = filter or VehicleFilter.from_profile(make, model, await self.profile)
        endpoint = "VehicleVariation"
        response = await self.session.get(
            self._url(endpoint), params=filter.to_request_params()
        )
        response.raise_for_status()
        return Vehicles(make=make, model=model, vehicles=await response.json())

    async def vehicles(
        self,
        vehicle_cluster_filter: VehicleClusterFilter | None = None,
    ) -> list[Vehicles]:
        """Todo: Load all vehicles of all clusters.

        After loading the clusters, load all vehicles of each cluster in parallel.
        Use aiohttp instead of requests
        """
        clusters = await self.vehicle_clusters(vehicle_cluster_filter)
        vehicles = await asyncio.gather(
            *[
                self.vehicles_of_make_and_model(cluster.make, cluster.model)
                for cluster in clusters
            ]
        )
        return vehicles

    def await_(self, coro: Awaitable[T]) -> T:
        return asyncio.get_event_loop().run_until_complete(coro)

    def __del__(self):
        """Automatically close the session when the object is garbage collected."""
        self.await_(self.session.close())
