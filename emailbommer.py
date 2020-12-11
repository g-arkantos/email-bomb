import sys
import smtplib
print("+[+[+[+[+[[[[[let's Start....+]+]+]+]+]]]]]")
def lets():
	try:
		print("[+[+[+[.....initializing program......]+]+]+]")
		target=input("enter target gmail")
		amout=500
		server='smtp.gmail.com'
		port=587
		fromadd=input("enter from address")
		pwd=input("enter your password")
		subject=input("enter subject")
		message=input("enter message")
		msg=(target,subject,message)
		s=smtplib.SMTP(server,port)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(fromadd,pwd)
		for i in range(amount+1):
			s.sendmail(fromadd,target,msg)
			c+=1
			s.close()
			sys.exit(0)
	except Exception as e:
		print(e)
lets()




