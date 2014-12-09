townsquare-flask
================

What will TownSquare be?
========================

As it stands, the requirements are pretty much written as the issues 
at https://github.com/sc3/django-townsquare/issues. It could definitely 
be cleaned up, but here's the basic rundown (probably isn't comprehensive):

Basic mission
===============

Have a system to keep track of volunteers' contributions of hours to the 
organization and to keep track of the reward credits they've earned as a 
result of their efforts. 

Basic Features:

1. Autocomplete for name insertion (issue 35 in that repo)
2. Add volunteers to system
3. Add events (where volunteer hours can be earned)
4. Track which volunteers are at each events (to issue rewards credits)
5. Track rewards credits

Expanding
===========

1. Report generation
2.Sign-in/Sign-out kiosk (which, as it stands, is a separate project -- may be integrated later)

Setup
=====

Make sure you are using Python 3.5! This app does not make any attempt
to be backwards compatible with older versions.

```
git clone git@github.com:sc3/townsquare-flask.git

cd townsquare-flask

mkvirtualenv town

pip install -r requirements.txt

```

Run the app:

```
./town

```

Run the tests:

```
nosetests tests

```



