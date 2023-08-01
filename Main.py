# Our Class that will be used to Emails
import EmailSender

# This is the Main Demo
if __name__ == "__main__":

    # Add Your Email Configuration
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    username = 'your_username'
    password = 'your_password'

    # Choose to select configure on runtime
    configureOption = int(input("Configure Server Details? (1/0): "))
    if configureOption == 1:
        smtp_server = str(input("Enter SMTP Server: "))
        smtp_port = str(input("Enter SMTP Port: "))
        username = str(input("Enter username: "))
        password = str(input("Enter password: "))

    # Create an instance of EmailSender with your mail server details
    email_sender = EmailSender(smtp_server, smtp_port, username, password)

    # Set the email subject and message
    subject = str(input("Enter Subject of Email: "))
    message = str(input("Enter the Message: "))

    email_sender.set_subject(subject)
    email_sender.set_message(message)

    # Add recipients
    while (1):

        # Add a single Recipent
        receiver = str(input("Enter Receiver Email Address: "))

        # Option to Add another recipent
        contReceiver = int(input("Do you want to Add another? (1/0): "))
        if contReceiver == 0:
            break

    # Send the email
    email_sender.send_email()

    print("The Email is sended!")
