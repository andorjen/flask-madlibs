from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def show_template_options():
    """render html that shows a dropdown menu for diffrent madlibs template"""
    return render_template("home.html")

@app.get("/silly_option")
def display_mad_libs_prompt():
    #Need more context of name display_mad_libs_prompt
    """Render mad libs form for input"""

    # Make variable and input it in the arguments of questions.html
    return render_template("questions.html",prompts=silly_story.prompts)

@app.get('/results')

def show_results():
    """Create Dictionary from silly_story.prompts, render story.html of results using generate function of silly_story"""

    #story_input = {prompt: request.args.get(prompt) for prompt in silly_story.prompts }

    story_info = silly_story.generate(request.args)
    return render_template("story.html", story=story_info)


