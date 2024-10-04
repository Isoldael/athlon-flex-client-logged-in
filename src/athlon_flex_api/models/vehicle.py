from pydantic import BaseModel


class Vehicle(BaseModel):
    """Vehicle model.

    A Vehicle defines a specific vehicle configuration.
    For example one instance of the Opel Corsa E.
    It belongs to the VehicleCluster of its make and type.
    """

    id: str
    make: str
    model: str
    type: str
    modelYear: int
    paintId: str
    priceInEuroPerMonth: float
    fiscalValueInEuro: float
    additionPercentage: float
    rangeInKm: int
    externalFuelTypeId: int
    externalTypeId: str
    imageUri: str

    def __str__(self):
        """Return the string representation of the vehicle."""
        return f"{self.make} {self.model} {self.type} {self.modelYear}"


# todo: include vehicles in VehicleClusters instead
class Vehicles(BaseModel):
    """Collection of vehicles of a specific make and model."""

    vehicles: list[Vehicle]

    def __str__(self):
        """Return the string representation of the vehicles."""
        msg = "Vehicles:"
        separator = "\n" + "-" * len(msg) + "\n"
        return f"{msg}{separator}{"\n".join(str(vehicle) for vehicle in self.vehicles)}"

    def __iter__(self):
        """Iterate over the vehicles."""
        return iter(self.vehicles)
