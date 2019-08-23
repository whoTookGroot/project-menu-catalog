# Intro

This is my project summarizing my experience so far in the past lession. At this point i'm able
to create a web application implementing the fundamentals of full stack web dev. This repo/project
lacks much of the house keeping and authorizing that I will employ in coming projects, as well as 
session handling.

DISCLAIMER:
- I realized there is hardly any value checking in this app, but I need to move onto a new project of larger scope.
- Forms were not styled. I'm a novice in web dev and wanted to style the forms alittle nicer and embed them in their parent templates. However I decided I should learn to properly build the front end of projects at a later date. (my cascading is messy and redundant)   

# Table of Contents

- [Intro](../master/README.md#intro)
- [Run Instructions](../master/README.md#run_instructions)
- [Screenshots](../master/README.md#screenshots)


# Run Instructions

- Create or connect to a db of your choosing, modify this in [database_setup.py](../master/database_setup.py)
- If you need to create a local db from scratch to connect to, I used postgreSQL for OSX
    - ```brew install postgres```
    - If you already have an initialized psql db directory and want to start fresh: 
    ```rm -r /usr/local/var/postgres```
    - Initialize your new psql db directory with ```initdb /usr/local/var/postgres```
    - Start postgres ```pg_ctl -D /usr/local/var/postgres start```
    - Create your new db ```createdb dbname```
- Once you have a db setup, how you choose to populate it is up to you. Methods include
    manual( through client or connecting to db in terminal) or running sql scripts, two sample ones
    have been provided [here](../master/tablePopulation/). I have not added a JSON endpoint for importing data,
    only exporting.
- Simply run [catalogServer.py](../master/catalogServer.py) with ```python3 catalogServer.py```
- Open browser and connect to ```localhost:12345```

# Screenshots
==============================================================================================================================
<img width="664" alt="Screen Shot 2019-08-23 at 3 54 34 PM" src="https://user-images.githubusercontent.com/22012906/63627862-70e49f00-c5be-11e9-9a49-108b207128f8.png">
==============================================================================================================================
<img width="1094" alt="Screen Shot 2019-08-23 at 3 53 50 PM" src="https://user-images.githubusercontent.com/22012906/63627863-70e49f00-c5be-11e9-838a-5526b3fd914e.png">
==============================================================================================================================
<img width="875" alt="Screen Shot 2019-08-23 at 3 53 32 PM" src="https://user-images.githubusercontent.com/22012906/63627864-717d3580-c5be-11e9-849e-74eac3f3756c.png">
==============================================================================================================================
<img width="1092" alt="Screen Shot 2019-08-23 at 3 53 18 PM" src="https://user-images.githubusercontent.com/22012906/63627865-717d3580-c5be-11e9-8692-2633fa57d0e0.png">
==============================================================================================================================
<img width="817" alt="Screen Shot 2019-08-23 at 3 52 55 PM" src="https://user-images.githubusercontent.com/22012906/63627866-717d3580-c5be-11e9-8d66-ec8abdd8ae52.png">
==============================================================================================================================
<img width="819" alt="Screen Shot 2019-08-23 at 3 52 49 PM" src="https://user-images.githubusercontent.com/22012906/63627867-717d3580-c5be-11e9-9d78-9549d8e4da54.png">
==============================================================================================================================
<img width="826" alt="Screen Shot 2019-08-23 at 3 52 40 PM" src="https://user-images.githubusercontent.com/22012906/63627868-717d3580-c5be-11e9-8da0-97f391690e2c.png">
==============================================================================================================================
<img width="1080" alt="Screen Shot 2019-08-23 at 3 52 25 PM" src="https://user-images.githubusercontent.com/22012906/63627869-7215cc00-c5be-11e9-815d-65b01c147681.png">
==============================================================================================================================
<img width="1180" alt="Screen Shot 2019-08-23 at 3 51 29 PM" src="https://user-images.githubusercontent.com/22012906/63627870-7215cc00-c5be-11e9-9187-0601c2804579.png">
==============================================================================================================================
<img width="996" alt="Screen Shot 2019-08-23 at 3 51 40 PM" src="https://user-images.githubusercontent.com/22012906/63627871-7215cc00-c5be-11e9-8800-b57d36ebd119.png">
