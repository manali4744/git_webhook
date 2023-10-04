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
  
