class Email:
    def __init__(self,sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.recipient}: {self.content}. Sent: {self.is_sent}"


emails = []
input_line = input()
while input_line != "Stop":
    sender, recipient, content = input_line.split()
    final_email = Email(sender, recipient, content)
    emails.append(final_email)
    input_line = input()

indexes = [int(index) for index in input().split(", ")]

for index in indexes:
    emails[index].send()

for current_email in emails:
    print(current_email.get_info())
