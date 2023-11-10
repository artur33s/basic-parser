import pandas as pd
import requests

proxies = {
    'http': 'http://6512432-all-country-DE:u6nmt8jjx@89.39.106.148:13462',
}

def get_items():
    url = 'https://recom.wb.ru/personal/ru/common/v4/search?TestGroup=sim_goods_srch_infra&TestID=323&appType=1&curr=rub&dest=-1257786&page=1&query=0&resultset=catalog&spp=25&suppressSpellcheck=false'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,ru-RU;q=0.9,ru;q=0.8',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.get(url, headers, proxies=proxies)
    return response.json()


def prepare_items(response):
    products = []

    products_raw = response.get('data', {}).get('products', None)

    if products_raw != None and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                'brand': product.get('brand', None),
                'brandId': product.get('brandId', None),
                'id': product.get('id', None),
                'name': product.get('name', None),
                'reviewRating': product.get('reviewRating', None),
                'pics': product.get('pics', None),
                'price': product.get('priceU', None),
            })

    return products


def main():
    response = get_items()
    products = prepare_items(response)

    pd.DataFrame(products).to_csv(f'{id(products)}products.csv', index=False)


if __name__ == '__main__':
    main()
