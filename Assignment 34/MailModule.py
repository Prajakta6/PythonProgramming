import smtplib
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_EMAIL = "testingpythoncode24@gmail.com"
SENDER_PASSWORD = "lcjy ekqd vyxp gszc"

def SendMail(ReceiverEmail, FileName):
    try:
        if not os.path.exists(FileName):
            return False
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = ReceiverEmail
        message["Subject"] = "Running Process Information Log"
        Body = """
                Hello,

                Please find the attached log file containing the running process information.

                This mail is generated automatically using Python Automation Script.

                Thank You.
                """

        message.attach(MIMEText(Body, "plain"))
        attachment = open(FileName, "rb")
        payload = MIMEBase("application", "octet-stream")
        payload.set_payload(attachment.read())
        encoders.encode_base64(payload)
        payload.add_header(
            "Content-Disposition",
            "attachment; filename={}".format(os.path.basename(FileName))
        )
        message.attach(payload)
        attachment.close()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(
            SENDER_EMAIL,
            ReceiverEmail,
            message.as_string()
        )
        server.quit()
        return True

    except smtplib.SMTPAuthenticationError:
        print("Authentication Failed")
        return False

    except smtplib.SMTPException as e:
        print("SMTP Error :", e)
        return False

    except FileNotFoundError:
        print("Log file not found")
        return False

    except Exception as e:
        print("Error :", e)
        return False