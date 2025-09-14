def matchingwords(words):
    ctr=0
    list=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr=ctr+1 
            list.append(word)
    print("list of word with first and last charater scene\n",list)
    return ctr
count=matchingwords(["abc","bcb","zuz","1221"])
print('number of words having first and last character same ',count)