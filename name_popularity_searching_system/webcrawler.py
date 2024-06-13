"""
File: webcrawler.py
Name: Dorinda
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}

        response = requests.get(url, headers=header)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        # ----- Write your code below this line ----- #
        tags = soup.find("tbody").text
        tag = tags.split()
        male_total = 0
        female_total = 0
        for i in range(1000):
            if i % 5 == 2:
                n = "".join(tag[i].split(","))
                male_total += int(n)
            if i % 5 == 4:
                n = "".join(tag[i].split(","))
                female_total += int(n)
        print(f"Male Number: {male_total}")
        print(f"Female Number: {female_total}")


if __name__ == '__main__':
    main()
