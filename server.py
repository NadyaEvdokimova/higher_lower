from flask import Flask
import random
number_guessed = random.randint(0, 9)
print(number_guessed)
app = Flask(__name__)


@app.route('/')
def higher_lower():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<h2>Type in the URL "/" + the number </h2>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route("/<int:number>")
def guess_number(number):
    if number < number_guessed:
        return ('<h1 style="color: red"> Too low, try again! </h1>'
                '<img src="https://media.giphy.com/media/Puc4FZWExJc0E/giphy.gif" width=400>')
    elif number > number_guessed:
        return ('<h1 style="color: blue"> Too high, try again! </h1>'
                '<img src="https://media.giphy.com/media/7NrwdWfZUcolgKcbOc/giphy.gif">')
    else:
        return ('<h1 style="color: green"> You got it! </h1>'
                '<img src="https://media.giphy.com/media/NfzERYyiWcXU4/giphy.gif">')


@app.route('/<name>')
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)