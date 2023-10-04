# Git Webhook Project Setup
This project is designed to track changes in a Git repository and identify differences between different versions of the code. Follow these concise steps to set up the project:

## Install dependencies
  ```bash
  $ python install -r requirements.txt
  ```
##  Create .env File
Create a .env file to store keys and tokens required for your project.

## Start Ngrok
 ```bash
  $ ngrok http 8000
  ```
##  Run the Server
  ```bash
  $ python manage.py runserver
  ```

##  Configure Webhook in GitHub

 In your GitHub repository settings:

    Add a secret key.
    Configure the payload URL to match your Ngrok or server URL.

Your project is now set up to track Git repository changes and identify code differences. Enjoy using it!

# Setting Up JIRA Webhooks for Your Ngrok URL

    Visit the JIRA Webhook configuration page(https://magnifio.atlassian.net/plugins/servlet/webhooks) at JIRA Webhook Configuration.
    Replace the existing URL with your Ngrok URL: https://8219-2401-4900-1f3f-6b73-d044-5def-dfcb-f020.ngrok-free.app/jira/.

# Configuring Figma Webhooks for Your Ngrok Site
    Navigate to the Figma Webhooks setup page (https://www.figma.com/developers/api#webhooks-v2-post-endpoint)

  Create a New Webhook:

    Log in to your Figma account if you're not already logged in.
    On the Figma Webhooks setup page, locate the option to create a new webhook.

Fill in Data from figma_webhook.json:

    Open the figma_webhook.json file and extract the required data such as:
    Event Type(s): Identify the events you want to trigger the webhook.
    Callback URL: This should be your Ngrok URL. Replace it with your Ngrok URL.
    Secret Key (Optional): If your webhook requires a secret key for verification, include it.

