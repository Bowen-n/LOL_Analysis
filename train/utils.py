import lxml
import requests
from lxml import etree


URL = 'https://www.op.gg/champion/statistics'
C_N_PATTERN = ".//div[@class='champion-index__champion-item__name']//text()"


def get_champion_names():
    response = etree.HTML(requests.get(url=URL).text)
    champions = response.xpath(C_N_PATTERN)
    return champions