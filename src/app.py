from flask import Flask

app = Flask("Ranking")

@app.route('/')
def Hello_world():
    return 'Status: OK...       Welcome to the Ranking API!'


