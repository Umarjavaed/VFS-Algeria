from mailtm import Email

# Listener function to print email subject and content
def listener(message):
    print("\nSubject: " + message['subject'])  # Prints the subject of the email
    print("Content: " + message['text'] if message['text'] else "No content")  # Prints email content

# Create a temporary email address
test = Email()

# Print the domain of the email
print("\nDomain: " + test.domain)

# Register a new email address
test.register()
Email_address = str(test.address)
print(Email_address)

# Start listening for new emails with 1-second intervals
test.start(listener, interval=1)
print("\nWaiting for new emails...")
