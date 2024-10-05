import os

from athlon_flex_api import logger
from athlon_flex_api.api import AthlonFlexApi

api = AthlonFlexApi(
    email=os.environ["USERNAME"],
    password=os.environ["PASSWORD"],
    gross_yearly_income=100000,
    apply_loonheffingskorting=True,
)
vehicles_clusters = api.await_(api.vehicle_clusters())
logger.info(vehicles_clusters)
