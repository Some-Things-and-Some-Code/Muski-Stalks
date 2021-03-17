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
from random import randrange
from CSVServices import *
from Api import Api

csv = CSVServices()


class EmailServices:

    # right now it doesn't need the username and password, making a second init that doesn't have those
    def __init__(self):
        self.recipients = ["example@example.com"]

        # SMTP Variables
        self.sender = 'muski-stalks@somedomain.com'

        # Key words for the email
        self.keywords = ['Elon', 'Musk', 'Musky', 'Boi', 'Tesla', 'Spacex', 'Mars']

    def send_email(self):

        # Pick a random number for the elon image
        ran_num = randrange(2)
        rand_quote = randrange(47)

        # Pick the mood of the image based on our stats
        body = {"Happy": "You gosh dang diddly did it! You beat your record and are obsessing about the Muski Boi "
                "more and more every day. Congrats.",
                "Neutral": "You did okay. I'm not upset... just disappointed. Try better next time.",
                "Sad": "This time, I am disappointed. You messed up. Elon Musk can feel your failure throughout the "
                "universe. Check yourself before you wreck yourself."}
        quote = csv.quote_to_array()
        mood = ["Happy", "Neutral", "Sad"]
        complisult = ["Smarty Pants", "Guy", "Idiot"]
        dad_setup, dad_punchline = Api().daily_dadjoke()
        total = 0
        old_total = 0

        # get the values for the present and previous values
        for i in self.keywords:
            total += int(csv.get_data_today(i))
            old_total += int(csv.get_data_yesterday(i))

        # Find out what mood Elon is in
        if total > old_total:
            mood = mood[0]
            complisult = complisult[0]
        elif total == old_total:
            mood = mood[1]
            complisult = complisult[1]
        else:
            mood = mood[2]
            complisult = complisult[2]

        msg = MIMEMultipart('related')
        msg['From'] = self.sender
        msg['Subject'] = "Test Email"

        msg_text = MIMEText(f"<p>Hey {complisult},</p><br>"
                            f"<p>{body[mood]}</p><br>"
                            "<p>Here's a quote for inspiration:</p>"
                            f"<p>{quote[rand_quote]}</p><br>"
                            "<p>You're daily dad joke:</p>"
                            f"<p>{dad_setup}</p>"
                            f"<p>{dad_punchline}</p><br>"
                            "<p>Finally, your daily meme</p>"
                            "<img src='cid:meme'><br>"
                            "<p>Have a great day,</p>"
                            "<p>Muski-Stalks</p>"
                            "<img src='cid:image1'>", 'html')
        msg.attach(msg_text)

        # Elon picture
        sig = io.open(f'Images\\{mood}\\{ran_num}.jpg', 'rb')
        elon_musk = MIMEImage(sig.read())
        sig.close()

        # Meme
        meme = Api().daily_meme()
        meme_image = MIMEImage(meme.read())

        # Insert image
        elon_musk.add_header('Content-ID', '<image1>')
        msg.attach(elon_musk)

        # Insert Meme
        meme_image.add_header('Content-ID', '<meme>')
        msg.attach(meme_image)

        smtp_obj = SMTP("someip")

        for i in self.recipients:
            try:
                msg['To'] = i
                smtp_obj.sendmail(msg["From"], i, msg.as_string())
            except Exception as e:
                print(f"Failed to send email! {e}")

        smtp_obj.quit()
