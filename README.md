# Python Email Send (Bulk Mail Sender)

This repository contains a Python class called EmailSender that enables users to send emails via an SMTP (Simple Mail Transfer Protocol) server with configurable recipients. Additionally, it includes a function to read email configuration from a config.txt file, making it easy for users to set up their email server details and credentials.

## Purpose

The purpose of this project is to provide a reusable and easy-to-use Python class for sending emails using an SMTP server. By encapsulating the email sending functionality within the EmailSender class, users can quickly integrate email functionality into their Python projects. The class allows users to set the recipients, subject, and message for the email and provides a method to send the email using a provided SMTP server.

The added function, read_email_config, further simplifies the email configuration process. Instead of hardcoding the SMTP server details and credentials within the Python script, users can store them in a separate config.txt file. The function reads the configuration from the file and returns the relevant values as a tuple, providing a cleaner and more organized approach to handle email configuration.

## Getting Started

To use the EmailSender class, follow these steps:

1. Clone this GitHub repository or download the Python script containing the EmailSender class.

2. Update the config.txt file with your SMTP server details and email credentials.

3. Import the EmailSender class into your Python script.

4. Use the EmailSender class to send emails by adding recipients, setting the subject and message, and calling the send_email method.

For detailed usage examples, refer to the demo provided in the Python script.
