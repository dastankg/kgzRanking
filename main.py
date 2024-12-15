from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_kyrgyzstan_standings():
    # Problem columns
    Problem = ['rank', 'Team', '=',
               'penalty']

    # URL of the page
    url = "https://nerc.itmo.ru/archive/2024/standings.html"

    try:
        # Load the page
        response = requests.get(url)
        response.encoding = 'cp1251'
        response.raise_for_status()  # Check request success

        # Create BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")  # Or specify table with a class

        # Extract table rows
        rows = table.find_all("tr")

        # Store standings
        standings = []

        # Process each row
        for row in rows:

            cells = row.find_all("td")
            data = [cell.get_text(strip=True) for cell in cells]
            data1 = [cell for cell in cells]
            d = {}
            # Filter for Kyrgyzstan locations

            if len(data) > 0 and any(location in data[1] for location in ['AUCA', 'UCA', 'Kyrgyz STU', 'KRSU']):
                for i in range(len(Problem)):
                    if i <= 1:
                        d[Problem[i]] = data[i]
                    elif i >= len(Problem) - 2:
                        d[Problem[i]] = data[i]
                    else:
                        a = str(data1[i])
                        a = a.replace('<td><i>', '')
                        a = a.replace('<s><br/>', ' ')
                        a = a.replace('</s></i></td>', '')
                        a, b = a.split()
                        d[Problem[i]] = a + '\n\n' + b
                standings.append(d)
        return Problem, standings

    except Exception as e:
        print(f"An error occurred: {e}")
        return Problem, []


@app.route('/')
def index():
    columns, data = get_kyrgyzstan_standings()
    return render_template('standings.html', columns=columns, standings=data)


if __name__ == '__main__':
    app.run(debug=True)
