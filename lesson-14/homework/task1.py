from pathlib import Path
from bs4 import BeautifulSoup

text = ""

current_dir = Path(__file__).resolve().parent

with open(current_dir / "weather.html","r") as file:
    for line in file.readlines():
        text += line
    
soup = BeautifulSoup(text,"html.parser")

days = soup.find_all("tr")

for day in days:
    s = day.text.split("\n")
    print(" ".join(s[1:-1]))

highest = -10**9
sunny_day = None
sum = 0

for day in days[1:]:
    s = day.text.split("\n")
    weather = int(s[2][:-2])
    if weather>highest:
        highest = weather
        d = s[1]
    if s[3]=="Sunny":
        sunny_day = s[1]
    sum += weather
    
print(f"The day with highest weather is {d} {highest}°C")
print(f"Sunny day: {sunny_day}")
print(f"Average temperature: {sum/(len(days)-1)}°C")
