__author__ = "Spitter Team"
__email__ = "spitter@spitter.com"
__version__ = "0.0.0"

import logging
import logging.config


logging.config.fileConfig("logging.ini")

logger = logging.getLogger(__name__)
