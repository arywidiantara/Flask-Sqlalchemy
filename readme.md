# Flask Rest Api 
A Flask Driven Restful API, Flask is written by Ary Widiantara [arywidiantara33@gmail.com]


## Technologies used
* **[Python3.7](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[MySQL](https://dev.mysql.com/downloads/installer/)** – Database 
* Minor dependencies can be found in the requirements.txt file on the root folder.


## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).

* #### Dependencies
    1. Cd into your the cloned repo as such:

        ```
        $ cd flask-example
        ```

    2. Create and fire up your virtual environment in python3: 

        ```
        $ source /venv/bin/active
        ```
        
        ```
        $ cp .env.example .env
        ```
* #### Environment Variables
    Create a .env file and add the following:

    ```
    export FLASK_APP=flask-example.py
    ```

* #### Install your requirements

    ```
    (venv)$ pip install -r requirements.txt
    ```

* #### Running It
    On your terminal, run the server using this one simple command:

    ```
    (venv)$ flask run
    ```

    Or you can running whit this

    ```
    (venv)$ python flask-example.py
    ```

    Or if you want using **[Docker](https://docs.docker.com/install/)** you are just run this without dependencies

    ```
    (venv)$ docker-compose up
    ```

    You can now access the app on your local browser by using

    ```
    http://localhost:2800/
    ```


    ```
    POSTMAN => https://www.getpostman.com/collections/e0e1468f936336b85687
    ```

