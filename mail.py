import os
import mimetypes

import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import requests

env = os.environ

SENDER = env.get("EMAIL_SENDER")
RECIPIENT = env.get("EMAIL_RECIPIENT")
CONFIGURATION_SET = "ConfigSet"
AWS_REGION = env.get("AWS_REGION")

SUBJECT = env.get("EMAIL_SUBJECT")

ses = boto3.client("ses", region_name=AWS_REGION)

def send_email(text, remote_attachments):
	msg = MIMEMultipart()
	msg["Subject"] = SUBJECT
	msg["From"] = SENDER
	msg["To"] = RECIPIENT
	
	msg.preamble = "Multipart message.\n"
	part = MIMEText(text + "\n\n")
	msg.attach(part)
	
	for i in range(len(remote_attachments)):
		r = requests.get(remote_attachments[i])
		if r.status_code != 200:
			continue
		content_type = r.headers["content-type"].split(";")[0]
		extension = mimetypes.guess_extension(content_type)
		
		part = MIMEApplication(r.content)
		part.add_header('Content-Disposition', 'attachment', filename="update" + str(i + 1) + extension)
		msg.attach(part)
	
	result = ses.send_raw_email(
		Source=SENDER,
		Destinations=[RECIPIENT],
		RawMessage={"Data": msg.as_string()}
	)
	
	print(result)