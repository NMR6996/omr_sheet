import re

opendosya = open("carmodel.txt", "r", encoding="utf8")
readdosya = opendosya.read()
writedosya = readdosya.split("\n")

newfile = open("carmodel+.txt", "w")

for row in writedosya:
    match1 = re.search(r'data-brand="([^"]+)"', row)
    match2 = re.search(r'">([^"]+)</option', row)

    brand = match1.group(1)
    model = match2.group(1)

    newfile.write("'")
    newfile.write(brand)
    newfile.write("':[")

    if brand == match1.group(1):
        newfile.write("'")
        newfile.write(model)
        newfile.write("'")
        newfile.write(", ")

    newfile.write("]")
    newfile.write("\n")
  
