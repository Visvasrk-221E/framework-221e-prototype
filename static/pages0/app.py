from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages

app = Flask(__name__)

# --- Configuration ---
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'pages'
app.config['FLATPAGES_MARKDOWN_EXTENSIONS'] = ['fenced_code', 'codehilite', 'tables', 'toc']
app.config['FLATPAGES_MARKDOWN_EXTENSION_CONFIGS'] = {
    'codehilite': {'linenums': False}
}

pages = FlatPages(app)

# --- Routes ---
@app.route('/')
@app.route('/index')
def index():
    # Sort posts by date descending
    posts = sorted(pages, key=lambda p: p.meta.get('date'), reverse=True)
    return render_template('index.html', posts=posts)

@app.route('/ideas/<path:path>')
def idea_page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == '__main__':
    app.run(debug=True)
