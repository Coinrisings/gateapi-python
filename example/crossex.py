# !/usr/bin/env python
# coding: utf-8
import logging
from decimal import Decimal as D

from gate_api import ApiClient, Configuration, CrossExApi

from config import RunConfig

logger = logging.getLogger(__name__)


def crossex_demo(run_config):
    # Initialize API client
    # Setting host is optional. It defaults to https://api.gateio.ws/api/v4
    config = Configuration(
        key=run_config.api_key, secret=run_config.api_secret, host=run_config.host_used)
    crooss_api = CrossExApi(ApiClient(config))
    res1 = crooss_api.get_crossex_account()
    print(res1)
    res2 = crooss_api.list_crossex_positions()
    print(res2)