from web import app
from models import Post
from flask import render_template

@app.route('/api/posts')
def list_posts():
	posts = Post.all()
	return 'looool'
#return render_template('list_posts.html', posts=posts)
