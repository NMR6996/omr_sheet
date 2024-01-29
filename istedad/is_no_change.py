opendosya = open("9.txt", "r")

readdosya = opendosya.read()
writedosya = readdosya.split("\n")

newfile = open("9+.txt", "w")
x = 100000

def is_no(a,b,c,d):
    for i in range(len(writedosya)):
        x += 1
        newfile.write(writedosya[i][a:b])
        newfile.write(str(x))
        newfile.write(",")
        newfile.write(writedosya[i][c:d])
        newfile.write(",")
        newfile.write("\n")
    return True

    
#is_no(0,26,33,157) # buraxilis10-11 a,b,c,d 0,26,33,157
#is_no(0,42,50,?) # blok11 a,b,c,d 0,42,50,son
#is_no(0,43,50,?) # blok9-10 a,b,c,d 0,43,51,son
#is_no(0,39,46,184) # asagisinif5-8 a,b,c,d 0,39,46,184
