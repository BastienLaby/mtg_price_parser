from requests import Response
from typing import List

from requests_html import HTMLSession


def get_web_content(url='https://python.org/') -> Response:
    session = HTMLSession()
    response = session.get(url)
    return response


def element_to_float(element):
    return float(element.text.strip("€").replace(",", "."))


def get_prices_from_html(html) -> List[float]:
    prices = html.find('#tabContent-info', first=True).find('.col-6.col-xl-7')
    return {
        "availables": element_to_float(prices[4]),
        "from_price": element_to_float(prices[5]),
        "price_trend": element_to_float(prices[6]),
        "price_30": element_to_float(prices[7]),
        "price_7": element_to_float(prices[8]),
        "price_1": element_to_float(prices[9])
    }


if __name__ == "__main__":
    url = "https://www.cardmarket.com/en/Magic/Products/Singles/War-of-the-Spark/Liliana-Dreadhorde-General"
    response = get_web_content(url)
    prices = get_prices_from_html(response.html)

    # TODO: get foil content