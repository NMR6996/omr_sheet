import re

openbrand = open("brand.html", "r", encoding="utf8")
readbrand = openbrand.read()
listbrand = readbrand.split("\n")

openmodel = open("model.html", "r", encoding="utf8")
readmodel = openmodel.read()
listmodel = readmodel.split("\n")

newfile = open("1.txt", "w", encoding="utf-8")

for row_brand in listbrand:
    match_brand_value = re.search(r'value="([^"]+)"', row_brand)
    match_value = match_brand_value.group(1)
    
    match_brand_name = re.search(r'">([^"]+)</option>', row_brand)
    match_value_22 = match_brand_name.group(1)

    newfile.write("]")
    newfile.write(",")
    newfile.write("\n")
    newfile.write("""'""")
    newfile.write(match_value_22)
    newfile.write("""'""")
    newfile.write(": [")

    for row_model in listmodel:
        match_model_value = re.search(r'class="([^"]+)"', row_model)
        match_value_1 = match_model_value.group(1)

        if match_value == match_value_1:
            match_model_name = re.search(r'">([^"]+)</option>', row_model)
            match_value_2 = match_model_name.group(1)
                    
            newfile.write("""'"""+match_value_2+"""'"""+",")
          
