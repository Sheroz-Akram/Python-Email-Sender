import smtplib
from email.message import EmailMessage


class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        # Initialize the EmailSender with SMTP server details and authentication credentials.
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.recipients = []
        self.message = ""
        self.subject = ""

    def add_recipient(self, recipient):
        # Add a recipient's email address to the list.
        self.recipients.append(recipient)

    def set_message(self, message):
        # Set the email message content.
        self.message = message

    def set_subject(self, subject):
        # Set the email subject.
        self.subject = subject

    def send_email(self):
        # Send the email with the configured details.
        if not self.recipients:
            print("Error: No recipients specified.")
            return

        if not self.message:
            print("Error: Message is empty.")
            return

        if not self.subject:
            print("Error: Subject is empty.")
            return

        # Create the email message object.
        msg = EmailMessage()
        msg.set_content(self.message)
        msg['Subject'] = self.subject
        msg['From'] = self.username
        msg['To'] = ", ".join(self.recipients)

        try:
            # Connect to the SMTP server, authenticate, and send the message.
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.username, self.password)
                server.send_message(msg)
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")
