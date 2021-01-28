# Remove_Aditional_Spaces

def Remove_Aditional_Spaces(a):
    a=list(a)
    count=0
    b=[]
    for i,x in enumerate(a):
        if a[i]==' ' and a[i+1]==' ':
            pass
        else:
            b.append(x)
    b=''.join(b)
    print(b)
    
    
# Count_Total_words_withoute_Space    
    
def Count_Total_words_withoute_Space(a):
    count=0
    for i,x in enumerate(a):
        if a[i]==' ':    
            pass
        else:
            count+=1
    print(count)
    
    
# Total Length Of String    
def Total_Length_Of_String(a):
    count=0
    for i,x in enumerate(a):
        if a[i]==' ':    
            count+=1
        else:
            count+=1
    print(count)

    
    
    
# Word Searching and Replace word
def Word_Searching_and_Replace_word(a,para,replaceWord):
    count=0
    lengthOfParameter=len(a)
    for i,x in enumerate(para):
        if(para[i:i+len(a)]==a):
            count+=1
    print("\nrepeate '{1}' {0} times in this paragraph:{0}".format(count,a),para) 
    replacParagraph=para.replace(a,replaceWord)
    print(replacParagraph)
    
# Count And Remove Punctuations    
def Count_And_Remove_Punctuations(para):
    punctuations='!#$%&()*+, -./:;<=>?@[\]^_`{|}~'
    count=0
    for i,x in enumerate(para):
        if x in punctuations:
            count+=1
            para=para.replace(x,'')

    print(f'total punctuation is :{count}')
    print(para)