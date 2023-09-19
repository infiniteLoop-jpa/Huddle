# Project: Huddle
# Group: infiniteLoop-JPA
# Names: Julia Ybanez, Pablo Duenas, Alondra Marin
# Fall 2023


from flask import Flask
app = Flask(__name__)

@app.route('/juliaybanez')
def juliaPage():
    return "This is my page."

if __name__ == '__main__':
    app.run()