email = input("Enter the email address: ")  #g@g.in
k = 0
j = 0
d = 0
# min 6 characters,No upper case letter,first alphabet,1 time @,no space
if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@') == 1):
            if (email[-3] == '.' ) ^ (email[-4] == '.'):
                for i in email:
                    if i == i.isspace():
                        k=1
                        
                    elif i.isalpha():
                        if i == i.upper():
                            j=1
                    elif i.isdigit():
                        continue

                    elif i == "_" or i=="." or i=="@":
                        continue
                    else:
                        d = 1
                if k==1 or j==1 or d==1:
                    print("InValid Email Address")
                else:
                    print("Valid Email")
            else:
                print("InValid Email Address")
        else:
            print("InValid Email Address")
    else:
        print("InValid Email Address")
else:
    print("InValid Email Address")
