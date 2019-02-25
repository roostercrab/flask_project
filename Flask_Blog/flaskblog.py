from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ef7ec7733ac126fa334a31ea7c382501'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)