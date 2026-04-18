import requests
from bs4 import BeautifulSoup

class CharPos:
    def __init__(self, x: int, y: int, char: str):
        self.x: int = x
        self.y: int = y
        self.char: str = char

def fetch_and_parse(url: str) -> list[CharPos]:
    response: requests.Response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch url")
        return []

    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    table_rows = soup.find_all('tr')

    char_pos_list: list[CharPos] = []

    for row in table_rows:
        cols = row.find_all('td')

        if len(cols) == 3:
            try:
                x :int = int(cols[0].get_text(strip=True))
                char :str = cols[1].get_text(strip=True)
                y :int = int(cols[2].get_text(strip=True))

                char_pos_list.append(CharPos(x, y, char))

            except ValueError:
                continue

    return char_pos_list

def print_char_list(char_pos_list: list[CharPos]) -> None:
    if not char_pos_list:
        print("No characters to display")
        return

    max_x: int = max(char.x for char in char_pos_list)
    max_y: int = max(char.y for char in char_pos_list)

    grid: list[list[str]] = [
        [" " for _ in range(max_x + 1)]
        for _ in range(max_y + 1)
    ]

    for char in char_pos_list:
        grid[char.y][char.x] = char.char

    for row in grid:
        print("".join(row))

get_url: str =input("Enter URL: ")
get_char_pos_list = fetch_and_parse(get_url)
print_char_list(get_char_pos_list)