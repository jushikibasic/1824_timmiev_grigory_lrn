import requests
import sys


def send_request() -> requests.Response:
    response = requests.get(URL, timeout=2)
    if not response.ok:
        print(f'Запрос не успешен: {response.status_code}')
        sys.exit(0)
    return response


URL = 'https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'
