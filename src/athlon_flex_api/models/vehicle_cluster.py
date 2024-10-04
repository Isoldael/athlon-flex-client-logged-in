from pydantic import BaseModel


class VehicleCluster(BaseModel):
    """Vehicle Cluster model.

    A Cluster defines a vehicle make and type. All registered
    cars belong to the cluster of its make and type.
    """

    firstVehicleId: str
    externalTypeId: str
    make: str
    model: str
    latestModelYear: int
    vehicleCount: int
    minPriceInEuroPerMonth: float
    fiscalValueInEuro: float
    additionPercentage: float
    externalFuelTypeId: int
    maxCO2Emission: int
    imageUri: str

    def __str__(self):
        """Return the string representation of the vehicle cluster."""
        return f"{self.make} {self.model}"


class VehicleClusters(BaseModel):
    """Collection of vehicle clusters."""

    vehicle_clusters: list[VehicleCluster]

    def __str__(self):
        """Return the string representation of the vehicle clusters."""
        msg = "Vehicle Clusters:"
        separator = "\n" + "-" * len(msg) + "\n"
        return f"{msg}{separator}{"\n".join(str(vehicle) for vehicle in self.vehicle_clusters)}"

    def __iter__(self):
        """Iterate over the vehicle clusters."""
        return iter(self.vehicle_clusters)

    def __getitem__(self, index):
        """Get the vehicle cluster at the given index."""
        return self.vehicle_clusters[index]
