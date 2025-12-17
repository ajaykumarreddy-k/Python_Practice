from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact')
def contact():
    return 'Contact Page'

@app.route('/<int:item_id>')
def item(item_id):
    return f'Item {item_id}'

@app.route('/user/<username>')
def user_profile(username):
    return f'User: {username}'

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about')
def about_page():
    return render_template('about.html')
@app.route('/contact')
def contact_page():
    return render_template('contact.html')  

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
