# chat

All inclusive basic chat application with pbkdf2 authentication - web socket communication and MySQL for long term storage.

Example video of chat application running
https://drive.google.com/file/d/0B6JIs8C0YBjlclZTVkJzOHBua1E/view

### setup instructions

The first thing you are going to need to do is set up the previous dependencies. The manual ones are as follows
* Install python 2.7x
* Have a running MySQL server
* Have sqlite3 ready to run in python.

Now you need to setup the python dependencies. I recommend you use a virtualenvironment to do so as I specifify versions for my packages.
`pip install -r requirements.txt`

I made the configuration file for this project a sqlite database that you need to setup. You can do so by running the 'setup.py' file from the command line.
`python setup.py`

Select all the items in the setup program and hopefully you should have a properly run configuration in the library.

From here you should be ready to run the application.

`python app.py`

Navigate to your browser and verify `localhost:5000` gives the proper response.
