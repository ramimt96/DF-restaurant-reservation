# Restaurant Reservation
This was the initial tech assessment for my internship at Digital Factory. We were instructed to learn Python Flask and create a simple site to track customer reservations. This was my first time utilizing Flask, HTML, or CSS.

## How to Run
1. Install `virtualenv`
```
$ pip install virtualenv
```
2. Open a terminal and run:
```
$ virtualenv env
```
3. Then run the command:
```
$ .\env\Scripts\activate
```
4. Then install:
```
$ (env) pip install flask flask-sqlalchemy
```
5. Finally start the web server:
```
$ (env) python app.py
```
This server will start on port 5000 by default. You can change this in app.py by changing the following line to this:

```
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
