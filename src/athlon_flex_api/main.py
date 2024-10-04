import os

from athlon_flex_api.api import AthlonFlexApi

api = AthlonFlexApi(os.environ["USERNAME"], os.environ["PASSWORD"])

clusters = api.vehicle_clusters()
for cluster in clusters:
    vehicles = api.vehicles(cluster.make, cluster.model)
    print(vehicles)
