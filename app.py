from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def read_posts_from_file(filename):
    posts = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            posts.append({
                'title': lines[i].strip(),
                'text': lines[i+1].strip()
            })
    return posts

def add_post_to_file(filename, title, text):
    with open(filename, 'a') as file:
        file.write(f'{title}\n{text}\n\n')

posts_file = 'data.txt'



@app.route("/")
def home():
    posts = read_posts_from_file(posts_file)
    return render_template("index.html", posts = posts)

@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        add_post_to_file(posts_file, title, text)
        return redirect(url_for('home'))
    return render_template('newpost.html')
