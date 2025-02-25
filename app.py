from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_kyrgyzstan_standings():
    # Problem columns
    Problem = ['rank', 'Team', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', '=',
               'penalty']

    # URL of the page
    url = "https://nerc.itmo.ru/archive/2024/standings.html"

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
    top_standings = []

    # Process each row
    for row in rows:

        cells = row.find_all("td")
        data = [cell.get_text(strip=True) for cell in cells]
        data1 = [cell for cell in cells]
        d = {}
        # Filter for Kyrgyzstan locations
        myTeam = ['AUCA', 'UCA', 'Kyrgyz STU', 'KRSU']
        if len(data) > 0 and (any(location in data[1] for location in myTeam)):
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
                    a = a.replace('<td><i', '')
                    a = a.replace('class="first-to-solve">', '')
                    a = a.split()
                    if len(a) == 1:
                        a = a[0]
                        a = str(a).replace('<td><b>', '')
                        a = str(a).replace('</b></td>', '')
                        a = str(a).replace('<td>', '')
                        a = str(a).replace('</td>', '')
                        d[Problem[i]] = a
                    else:
                        a, b = a[0], a[1]

                        d[Problem[i]] = a + '<br>' + b
            standings.append(d)

    for ind, row in enumerate(rows):
        if ind == 0:
            t = str(row.find_all('p')[0]).replace('<p>', '').replace('<br/>status:  running</p>', '')
            t = t.replace(' of ', ' ')
            print(t)

        if ind >= 2:
            cells = row.find_all("td")
            data = [cell.get_text(strip=True) for cell in cells]
            data1 = [cell for cell in cells]
            d = {}
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
                    a = a.replace('<td><i', '')
                    a = a.replace('class="first-to-solve">', '')
                    a = a.split()
                    if len(a) == 1:
                        d[Problem[i]] = '.'
                    else:
                        a, b = a[0], a[1]

                        d[Problem[i]] = a + '<br>' + b
            top_standings.append(d)
            if len(top_standings) >= 12:
                break

    return Problem, standings, top_standings, t.split()[0]


@app.route('/')
def index():
    columns, data, top_12, t = get_kyrgyzstan_standings()
    return render_template('standings.html', columns=columns, standings=data, top_12=top_12, t=t)


if __name__ == '__main__':
    app.run(debug=True)
