from flask import Flask, render_template
app=Flask(__name__)


@app.route('/')
def hello():
    return u'欢迎来到我的 Watchlist！'
