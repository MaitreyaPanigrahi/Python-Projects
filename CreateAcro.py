

def acronym():
    userInput = input("Please Provide a phrase to turn it into acronym: ")

    wordArr = userInput.split(" ")

    for words in wordArr:
        if words == 'and' or words == 'of' :
            wordArr.remove(words)
    
            
    # print (wordArr)


    acronym = ""
    for word in wordArr:
        if(word != ""):
            acronym += word[0]
    acronym = acronym.upper()
    print(f"The acronym is {acronym}")
if __name__ == "__main__":
    while True:
        acronym()

        