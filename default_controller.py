

import os
import os.path
import sys
import re
import json
import datetime
import logging
import requests
from connexion import NoContent

SERVICE_NAME = "sample-api"
VERSION_PATH = 'version.env'

# Setup logging
logger = logging.getLogger(__name__)
if not logger.handlers:
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)



def get_version():
    """ Describe this microservice
    Returns:
        (obj): name, api version
    """
    if os.path.exists(VERSION_PATH):
        with open(VERSION_PATH, 'r') as f:
            lines = f.readlines()
        # Retrieve only the version number from the file
        version_reg = re.compile(r'(\d).(\d).(\d)')
        version_match = re.search(version_reg, lines[0])
        if not version_match:
            logger.error("Invalid version definition (3-tuple of integers): %s", lines[0])
            version = "(unknown)"
        else:
            version = version_match.group()
    else:
        logger.error("Version file %s was not found.", VERSION_PATH)
        version = "(unknown)"

    return {"name": SERVICE_NAME, "version": version}


def health_check():
    """ Check the microservice health
    Returns:
        200 - healthly
        500 - not
    """
    return {'health':'ok'}, 200

def readiness_check():
    """ Check if the microservice can accept requests
    Returns:
        200 - service is ready
        500 - out of service
    """
    return {'ready':'up'}, 200

