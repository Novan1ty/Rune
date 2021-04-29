from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Rune is now online in his discord account."

def run():
    app.run(host="0.0.0.0", port=3002)

def keep_alive():
    server = Thread(targer=run)
    server.start()