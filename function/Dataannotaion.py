import requests
from bs4 import BeautifulSoup

def print_secret_message(doc_url):
    """
    Takes the URL of a published Google Doc containing a table of
    (x-coordinate, character, y-coordinate) and prints the grid of
    characters, revealing a secret message in uppercase letters.
    """
    response = requests.get(doc_url)
    response.raise_for_status()
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")

    coordinates = []
    max_x = 0
    max_y = 0

    for row in rows[1:]:
        cells = row.find_all("td")
        if len(cells) != 3:
            continue

        x_text = cells[0].get_text(strip=True)
        char = cells[1].get_text(strip=True)
        y_text = cells[2].get_text(strip=True)

        if x_text == "" or y_text == "":
            continue

        x = int(x_text)
        y = int(y_text)

        coordinates.append((x, y, char))
        max_x = max(max_x, x)
        max_y = max(max_y, y)


    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in coordinates:
        grid[y][x] = char

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    print_secret_message("https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub")