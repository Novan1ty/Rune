from flask import Flask
from threading import Thread

App = Flask('')


@App.route('/')
def Start():
    Rune = '<h1 style="font-family: monospace">Rune The Unknown.<h1>'
    return Rune


def Run():
    App.run(host='0.0.0.0', port=8080)


def Get_Port():
    The_Thread = Thread(target=Run)
    The_Thread.start()
