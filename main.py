from sanic import Sanic
from sanic.response import text, html

import sqlite3

app = Sanic("MyHelloWorldApp")

# Connect to the database
conn = sqlite3.connect('../license-plate-detection/data.db')
cursor = conn.cursor()

@app.get("/")
async def hello_world(request):
    cursor.execute("SELECT * FROM license_plates")
    rows = cursor.fetchall()

    return html(f"<h1>Hello World <p>{rows}/p></h1>.")
