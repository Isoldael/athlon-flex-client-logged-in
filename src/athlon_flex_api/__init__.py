from logging import StreamHandler, getLogger

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

logger = getLogger(__name__)
logger.setLevel("DEBUG")
logger.addHandler(StreamHandler())
