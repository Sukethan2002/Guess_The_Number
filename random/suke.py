from flask import Flask, render_template, request
import random

app = Flask(__name__)

number_to_guess = random.randint(1, 10)
tries = 0

@app.route("/", methods=["GET", "POST"])
def guess_game():
    global number_to_guess, tries
    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])
        tries += 1
        if guess == number_to_guess:
            message = f"🎉 Correct! You guessed it in {tries} tries."
            number_to_guess = random.randint(1, 10)
            tries = 0
        elif guess < number_to_guess:
            message = "Too low!"
        else:
            message = "Too high!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)


