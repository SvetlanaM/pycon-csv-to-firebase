# Firebase setup for PyCon mobile app

This code is responsible for sending data in correct format to [Firebase](https://firebase.google.com/) database which is used as backend for PyCon mobile app. 

### Requirements
1. Python 3.4 || Python 3.5
2. [pip](https://pypi.python.org/pypi/pip/1.0.2) - tool for installing and managing Python packages
3. [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (not required) - tool to keep the dependencies required by different projects in separate places
 
### Installation
1. Create virtual environment in your project folder
2. Install required libraries and packages
   <code>pip install -r requirements.txt</code>
3. Create csv folder in your project
4. Run code:
   <code>python convert.py</code>
5. Enter the name of your CSV file (example: pyconcz_schedule).

### Basic config
<pre><code>{  
  "config":{  
     "pycon_name":"PyCon CZ",
     "pycon_logo":"https://cz.pycon.org/2016/static/img/pyconlogo.svg",
     "pycon_color":"#dedede ",
     "twitter_hashtag":"#pyconcz",
     "pycon_db":"pyconcz2016",
     "active":true
  }
}</code></pre>

