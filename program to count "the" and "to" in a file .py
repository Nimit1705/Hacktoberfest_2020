def counter():
    f= open("Poem.txt","r")
    c=0
    line=f.read()
    word=line.split()
    for w in word:
        c += w.count('to')
    print(c)
    f.close()    
counter()            
