from flask import Flask, render_template
from post import Post
import requests

#Blogposts ophalen van API en in array steken.
post_objects = []
url_blogs = "https://api.npoint.io/c790b4d5cab58020d391"
resp_blogposts = requests.get(url=url_blogs)
blogposts = resp_blogposts.json()
for post in blogposts:
    #Post-object maken
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs=post_objects)

@app.route('/post/<int:index>')
def blogdetail(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)

