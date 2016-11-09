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
5. Enter the name of your CSV file (example: "pyconcz_schedule").

### Basic config
This config is used for settings in mobile application. Add code to the [config file](https://github.com/SvetlanaM/csvToFirebase-PyConMobileApp/blob/master/config.json).
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

### Database mapping
For every dictionary key, add value based on the column name in your database. On the left side, there are final keys, on the right side, there are your database columns. Add code to the [mapping file](https://github.com/SvetlanaM/csvToFirebase-PyConMobileApp/blob/master/mapping.json). It would be appropriate, If you have all your columns in one exported csv file. Example of the configuration:
<pre><code>{
 "room" : "room",
 "active" : true,
 "avatar" : "avatar",
 "bio" : "More information about you (public)",
 "description" : "Abstract (public)",
 "github" : "",
 "speaker" : "Your full name",
 "date_start" : "time",
 "date_end" : "time_end",
 "title" : "Title",
 "twitter" : "Your Twitter User-name/github account",
 "type" : "What are you proposing?"
}</code></pre>

### Event types
You can define these types:

1. Workshop
2. Talk
3. Break
4. Other (afterparty, lighting talks, ...)

## ToDo
1. Import csv files to Amazon S3 Storage
2. Download csv files from S3
3. Create django admin interface for managing input/output csv and mapping columns
