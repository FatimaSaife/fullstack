from flask import Flask, render_template,url_for

app = Flask(__name__)
@app.route('/')
def home():
	return render_template('homepage.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/event')
def event():
    return render_template('event.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/pages')
def pages():
    return render_template('pages.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)