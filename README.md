# OneQuantum Phillipines Website
## Project Description

This project is a small-scale website for the organization, OneQuantum Philippines, that uses free services.


I used flask as the web framework for this project. Flask is a lightweight and flexible framework for building web applications in Python. I also used Bootstrap as the framework for the css. 

---
## Challenges Faced

For the front-end, I encountered an unexpected difficulty in implementing the design I created into the website. Additionally, I have been operating under a tight schedule for the past week, which has impacted my performance. However, I have been diligently seeking ways to allocate more time to the project despite these challenges.

---
## Getting Started
Follow these steps to set up and run the project on your local machine:

1) Clone the repository

    ```bash
    git clone https://github.com/lalalance12/OneQuantum-PH-Website.git
    ```

2) Change the directory to the app

    ```bash
    cd /OneQuantum-PH-Website
    ```

3) Run the environment
    ```bash
    pipenv shell 
    ```

4) Install dependencies

    ```bash
    pipenv install 
    ```

5) Create a .env file containing the keys/values of the required variable

    ```
    SECRET_KEY=onequantumph
    PIPENV_VENV_IN_PROJECT=1
    FLASK_APP=app
    FLASK_DEBUG=true
    FLASK_RUN_PORT=5000
    ```

6) Run the flask application 
    ```bash
    flask run
    ```

    > Click the link of the development server example of this is 'http://127.0.0.1:5000'

    > Press CTRL+C to quit/exit the development server