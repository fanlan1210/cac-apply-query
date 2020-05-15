from bs4 import BeautifulSoup
import os
import glob
target = glob.glob("pages/*.html")
target.sort(key=os.path.getctime)
for t in target:
    print(t)
    with open(t, encoding="utf-8") as page:
        soup = BeautifulSoup(page, "html.parser")
        items = soup.find_all("tr",{"bgcolor":["#DEDEDC","#FFFFFF"]})
        
        data = open("output.html", "a", encoding="utf-8")

        for i in items:
        #    print(i)
            data.write(str(i))