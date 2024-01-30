import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()

ob.login('l.29.maitreya@gmail.com','iakk serr qwjs ewlp')
subject = input("Enter the Subject: ")
body = input("Enter the body: ")
message = f"subject:{subject}\n\n {body}"
listadd = ['maitreyapani10@gmail.com', 'rituchhandapanigrahi@gmail.com']

ob.sendmail('l.29.maitreya@gmail.com',listadd,message)
print("Message Sent")
ob.quit()