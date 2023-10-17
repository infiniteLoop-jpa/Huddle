# Project: Huddle
# Group: infiniteLoop-JPA
# Names: Alondra Marin, Julia Ybanez, Pablo Duenas
# Fall 2023


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Anime')
def animeMessage():
    return "Welcome to the page that has a list of my favorite anime. Hunter X Hunter, Jujutsu Kaisen, One Piece.  "


if __name__ == '__main__':
    app.run()
