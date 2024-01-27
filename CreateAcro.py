def acronym():
    userInput = input("Please Provide a phrase to turn it into acronym: ")

    exclusions = userInput.replace('and' , "")
    exclusions = userInput.replace('of' , "")

    wordArr = exclusions.split(" ")

    acronym = " "
    for word in wordArr:
        if(word != ""):
            acronym = acronym + word[0]
    acronym = acronym.upper()
    print(f"The acronym is {acronym}")
if __name__ == "__main__":
    while True:
        acronym()