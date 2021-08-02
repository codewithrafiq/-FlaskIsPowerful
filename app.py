from flask import Flask,render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"
    
data = {
    'name': "Jubayer Isalm",
    "age": 19,
    "Live":"Cumila"
}

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html',info=data)

posts = [
    {
        "id":1,
        "user":"user1",
        "title":"This Post 1 Title",
        "content":"This Post 1 Content",
    },
    {
        "id":2,
        "user":"user2",
        "title":"This Post 2 Title",
        "content":"This Post 2 Content",
    },
    {
        "id":3,
        "user":"user1",
        "title":"This Post 3 Title",
        "content":"This Post 3 Content",
    },
    {
        "id":4,
        "user":"user2",
        "title":"This Post 4 Title",
        "content":"This Post 4 Content",
    },
]

@app.route('/posts', methods=['GET'])
def allPosts():
    return render_template('posts.html',posts=posts)


@app.route('/single-post/<int:post_id>', methods=['GET'])
def singlePosts(post_id):
    print("post_id---------->",post_id)
    for post in posts:
        if post['id'] == post_id:
            return render_template('single-post.html',pppppppp=post)
    return "single Post"



if __name__ == '__main__':
    app.run(debug=True)
