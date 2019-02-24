from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Dick Butkis',
        'title': 'Fendi Booty',
        'content': 'FENDI FENDI FENDI! BOOTY BOOTY BOOTY!',
        'date_posted': 'April 1st, 2099'
    },
    {
        'author': 'Assy McChapstick',
        'title': 'Piddy pop on the tippy tai',
        'content': 'Watotay mah damie? Seppy tow on the tippy tai.',
        'date_posted': 'December 3rd, 2099'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)