import sys
import smtplib
import getpass
print("+[+[+[+[+[[[[[let's Start.....]]]]+]+]+]+]")
def lets():
	try:
		print("[+[+[+[.....initializing program......]+]+]+]")
		target=input("enter target gmail")
		amount=500
		server='smtp.gmail.com'
		port=587
		fromadd=input("enter from address: ")
		pwd=getpass.getpass("Enter your password: ")
		subject=input("enter subject: ")
		msg=input("enter message: ")
		message= f'Subject: {subject}\n\n\n{msg}'
		s=smtplib.SMTP(server,port)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(fromadd,pwd)
		for i in range(amount+1):
			s.sendmail(fromadd,target,message)
			i+=1
			s.close()
			sys.exit(0)
	except Exception as e:
		print(e)
lets()




