from pydantic import BaseModel


class Profile(BaseModel):
    class RelationshipManager(BaseModel):
        name: str
        email: str
        phone: str

    class Budget(BaseModel):
        actualBudgetPerMonth: int
        maxBudgetPerMonth: int
        normBudgetPerMonth: int
        normBudgetGasolinePerMonth: int
        normBudgetElectricPerMonth: int
        maxBudgetGasolinePerMonth: int
        maxBudgetElectricPerMonth: int
        normUndershootPercentage: int
        maxNormUndershootPercentage: int
        savedBudget: int
        savedBudgetPayoutAllowed: bool
        holidayCarRaiseAllowed: bool

    class Address(BaseModel):
        street: str
        houseNumber: str
        houseNumberAddendum: str
        zipCode: str
        city: str

    class CurrentReservation(BaseModel):
        externalId: str
        startedAtUtc: str
        vehicleId: str
        vehicleExternalId: str
        hasLicenseCardAvailable: bool

    id: str
    initials: str
    firstName: str
    lastName: str
    phoneNumber: str
    email: str
    customerName: str
    isConsumer: bool
    flexPlus: bool
    relationshipManager: RelationshipManager
    requiresIncludeTaxInPrices: bool
    includeMileageCostsInPricing: bool
    includeFuelCostsInPricing: bool
    onlyShowNetMonthCosts: bool
    numberOfKmPerMonth: int
    remainingSwaps: int
    budget: Budget
    hideIntroPopup: bool
    chargingStationRequest: bool
    pendingCancelation: bool
    pendingBikeCancelation: bool
    pendingBudgetPayout: bool
    pendingHolidayCarRaise: bool
    deliveryAddress: Address
    officialAddress: Address
    currentReservation: CurrentReservation
    firstReservationAllowedFromUtc: str
    firstDeliveryAllowedFromUtc: str
    canOrderBike: bool
    canMakeReservation: bool
    canMakeReservationFromUtc: str
    canMakePickup: bool
    canMakeBikeReservation: bool
    canMakeBikePickup: bool
    canMakeFirstReservation: bool
    canDecline: bool
    canDeclineBike: bool
