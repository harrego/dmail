# dmail

Designed for news channels, dmail hosts a Discord self-bot that listens in specified channels for any message. When a message comes in a request is made to AWS Simple Email Service that sends the message text and attachments to an predetermined email address. Emails are sent in plain text, one per message.

### Discord Self-bot Warning

Running a Discord self-bot is a ToS violation, therefore **using `dmail` will get your Discord account suspended, you've been warned.**

## Requirements

* Python 3.9
* pipenv
* AWS Simple Email Service
	* Simple to setup in the AWS dashboard. You need to verify either two email addresses, or a single email address and a whole domain. One is the sending address and the other is the receiving address (by default you can only send emails to verified addresses).
* Discord account token

## Usage

1. Install dependencies, `pipenv install`.
2. Setup environment variables (more information below).
3. Start dmail, `pipenv run python3 main.py`.

### Environment Variables

All environment variables listed below are required. If you have any issues you probably misconfigured one.

|Variable|Description|
|-|-|
|`AWS_REGION`|AWS endpoint region to make the SES requests. The region is important for AWS SES (I believe), make sure you match the region you used when verifying email addresses/domains.|
|`AWS_ACCESS_KEY_ID`|AWS access key ID with SES permissions. I recommend setting up an IAM user.|
|`AWS_SECRET_ACCESS_KEY`|AWS secret access key, as mentioned before I recommend setting up an IAM user.|
|`DISCORD_TOKEN`|Discord user token extracted from the browser.|
|`DISCORD_CHANS`|Comma separated list of channels to listen and trigger an email.|
|`EMAIL_SENDER`|Sender name and address in email notation, e.g. `Example Sender <example@sender.com>`.|
|`EMAIL_RECIPIENT`|Recipient address, e.g. `example@recipient.com`.|
|`EMAIL_SUBJECT`|Subject for every update email.|
