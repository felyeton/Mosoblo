import requests

from datetime import datetime as dt, timedelta


class ParseMO:
    start_time = None
    end_time = None

    def __init__(self, date: str):
        self.calc_time(date)

    def calc_time(self, date: str):
        self.start_time = int(dt.timestamp(dt.fromisoformat(date)) * 1000)
        self.end_time = int(dt.timestamp(dt.fromisoformat(date) + timedelta(days=1)) * 1000 - 1)
        print(int(self.start_time), int(self.end_time))

    def parse(self):
        response = requests.get(
            f'https://nopowersupply.mosoblenergo.ru/back/api/otklyuchenies?populate[uzel_podklyucheniya][populate][uliczas]=true'
            f'&populate[uzel_podklyucheniya][populate][gorod]=true'
            f'&filters[$or][0][$and][0][begin][$gte]={self.start_time}'
            f'&filters[$or][0][$and][1][begin][$lte]={self.end_time}'
            f'&filters[$or][1][$and][0][end][$gte]={self.start_time}'
            f'&filters[$or][1][$and][1][end][$lte]={self.end_time}'
            f'&pagination[pageSize]=100000',
            # headers=headers,
        )
        print(response.json())
        print(self.start_time, self.end_time)

    def __read_json(self):
        pass


# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Connection': 'keep-alive',
#     'Origin': 'https://mosoblenergo.ru',
#     'Referer': 'https://mosoblenergo.ru/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }


def main():
    a = ParseMO("2023-12-05").parse()


if __name__ == "__main__":
    main()
