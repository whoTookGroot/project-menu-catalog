# Intro

This is my project summarizing my experience so far in the past lession. At this point i'm able
to create a web application implementing the fundamentals of full stack web dev. This repo/project
lacks much of the house keeping and authorizing that I will employ in coming projects, as well as 
session handling.

DISCLAIMER: I realized there is hardly any value checking in this app, but I need to move on
to a new project of larger scope.

# Table of Contents

- [Intro](../master/README.md#intro)
- [Run Instructions](../master/README.md#run_instructions)
- [ScreenShots](../master/README.md#screenshots)


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
