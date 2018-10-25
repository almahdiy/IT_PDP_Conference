Project Reality: 2018 IT PDP Conference
---------------------------------------

<br><br>
<p align="center">
  <img align="middle" width=400 src="assets/logo_main.png">
</p>
<br><br>

Project Reality is a web application that is intended to act as the 
conference management tool for the 2018 IT PDP conference (to be held on 21st
 November 2018 inshAllah). See the *Key Features* section below for an overview.


Prerequisites
-------------
- Python 3+ (see requirements.txt file)


How to Run
----------
Back End Code (located in `/API`):
1. Install all the dependencies (e.g. `pip install -r requirements.txt`).
2. Run the back end server via invoking `python manage.py runserver`.
3. Launch a browser and connect to the server (e.g. 127.0.0.1:8000/admin).

Front End Code (located in `/website`):
1. Execute the `index.html` and your browser will launch.


Key Features
------------
- Splash page, allows connection to a conference session.
- Agenda page, displays the agenda of the conference.
- Booths page, displays the floor plan of the booths.
- Q&A session page, allows interactive posting and voting of questions. 


Authors
-------
- Programming Team (Yaqeen Mahdi)
- Graphics Team (artwork assets)


TODO
----
- Add navigation bar to Metaverse page
- Add rectangular instructions to Metaverse page
- Add navigation bar to Team Programming page
- Add navigation bar to Team Logistics page


Bugs
----
- File linking does not contain `.html` suffix (code smell?)
