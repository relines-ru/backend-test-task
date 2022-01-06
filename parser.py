import json
import requests as rq
from icecream import ic
from config import cfg


def collect_data():

    res = rq.get(
        url=cfg.get('flask_restful', 'site'),
        headers={'user-agent': cfg.DEFAULT_HEADERS},
    )
    return res.text


ic(collect_data())
