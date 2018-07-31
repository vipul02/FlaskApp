from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/projects/')
def projects():
    return 'This url contains some directory'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User: {}'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post: {}'.format(post_id)


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_login()
#     else:
#         show_login_form()

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('projects'))
    # print(url_for('hello', next='/'))
    print(url_for('show_user_profile', username='Vipul Lalwani'))
    print(url_for('static', filename='style.css'))

if __name__ == '__main__':
    app.run()
