import smtplib


def sendEmail(to, content):
    try:
       
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        server.login('senderemail@gmail.com', 'your_password')  

      
        from_email = 'senderemail@gmail.com'
        subject = "Subject of the email"
        body = content
        message = f"Subject: {subject}\n\n{body}"


        server.sendmail(from_email, to, message)
        print("Email sent successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
     
        server.quit()

to = input("Enter the email of the recipient: \n")
content = input("Enter the content for the email: \n")


sendEmail(to, content)