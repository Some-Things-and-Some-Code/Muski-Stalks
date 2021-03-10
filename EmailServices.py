"""
Used to send the email to let us know how we are doing statistically
"""

import io
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from os.path import basename


class EmailServices:

    # right now it doesn't need the username and password, making a second init that doesn't have those
    def __init__(self):
        self.recipients = ["eseidel@castlecookemortgage.com", "eberg@castlecookemortgage.com",
                           "amassey@castlecookemortgage.com"]

        # SMTP Variables
        self.sender = 'muski-stalks@twothingsandsomecode.com'

    def send_email(self):

        msg = MIMEMultipart('related')
        msg['From'] = self.sender
        msg['Subject'] = "Test Email"

        msg_text = MIMEText(f"<p>Hello,</p>"
                            f"<p></p>"
                            f"<p>This is a sample email from Muski-Stalks.</p>"
                            f"<p></p>"
                            f"<p>Thanks,</p>"
                            f"<p>Muski-Stalks :*</p>"
                            f"<img src='cid:image1'>", 'html')
        msg.attach(msg_text)

        # Elon picture
        sig = io.open('Images\\Happy\\0.jpg', 'rb')
        elon_musk = MIMEImage(sig.read())
        sig.close()

        # Insert image
        elon_musk.add_header('Content-ID', '<image1>')
        msg.attach(elon_musk)

        smtp_obj = SMTP("172.21.1.20:25")

        for i in self.recipients:
            try:
                msg['To'] = i
                smtp_obj.sendmail(msg["From"], i, msg.as_string())
            except Exception as e:
                print(f"Failed to send email! {e}")

        smtp_obj.quit()