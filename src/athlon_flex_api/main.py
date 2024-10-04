import os

from athlon_flex_api.api import AthlonFlexApi

api = AthlonFlexApi(os.environ["USERNAME"], os.environ["PASSWORD"])
vehicles_clusters = api.await_(api.vehicles())
for vehicles in vehicles_clusters:
    print(vehicles)
