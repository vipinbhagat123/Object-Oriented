import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    sender_email = input("Enter your email: ")
    password = input("Enter your email password: ") # Be cautious about hardcoding or directly inputting passwords in production code. Consider environment variables or more secure methods.
    reciever_email = input("Enter receiver's email: ")
    subject = input("Enter subject: ")
    message_body = input("Enter your message: ")

    # set up the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = reciever_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'plain'))

    try:
        # sending email through Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Corrected SMTP server address
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())
        print("Email sent successfully!")
        server.quit()
    except Exception as e:
        print(f"Error: {e}")

# Call the function to send an email
send_email()