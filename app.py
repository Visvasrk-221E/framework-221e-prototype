
#[Initialize]===========================================================================================================
# Import the necessary modules

from flask import Flask, render_template, url_for, redirect, Response, send_from_directory
from flask_flatpages import FlatPages
import markdown
from datetime import datetime
import time
import os

#[Configuration]========================================================================================================
# Configure the app settings

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)
docsdir = os.path.join(app.static_folder, "documents")

# Configure flat pages
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'pages'
app.config['FLATPAGES_MARKDOWN_EXTENSIONS'] = ['fenced_code', 'codehilite', 'tables', 'toc', 'attr_list']
app.config['FLATPAGES_MARKDOWN_EXTENSION_CONFIGS'] = {
    'codehilite': {'linenums': False}
}

pages = FlatPages(app)


#[Utilities]============================================================================================================
# Create the utility functions

def render_markdown(text):
	md = markdown.Markdown(extensions=['toc', 'fenced_code', 'tables', 'attr_list', 'codehilite'])
	html = md.convert(text)
	toc = md.toc
	return html, toc

#[Routes]===============================================================================================================

#[Create the utils for main routes]
# Create the roots for the app

@app.route('/')
def redirect_to_home():
	return redirect(url_for('home'))

@app.route('/home')
def home():
	posts = sorted(pages, key=lambda p: p.meta.get('date'), reverse=True)
	docnum = len([f for f in os.listdir(docsdir)])
	subjects = {
	"biology" : "Topics based on general biology as well as grade 12 biology can be learnt from here.[Grade 12]",
	"cybersecurity" : "Topics based on cybersecurity, from school to college level or even masters can be learnt from here.[Basics]",
	}
	anadomains = {
	"sec-reports" : "Uncover details and studies about various security reports and current emerging threats. We gather information from the Fortiguard Labs, The Guardian, The Bulletin of Atomic Scientists, and other trust worthy sources. We cover a various range of topics from biosecurity to poverty and health issues, cyberattacks, etc.[Security]",
	"scene-scape" : "Read about movie like reality based stimulations using AI, which predicts the divergence of current scene and provides the possible scenario in near future. SceneScape constructs just stimulations of what will happen, we are not assuring you that it will happen. We tell that it may happen, be prepared. If you feel bored, read these nightmare stimulations.[Stimulation]",
	}
	subject_count = len(subjects) + len(anadomains)
	crt_time = datetime.now()
	return render_template('index.html', time=crt_time, subjects=subjects, posts=posts, subject_count=subject_count, docnum=docnum, anadomains=anadomains)

# Create the route for blog perceptions

@app.route('/ideas/<path:path>')
def idea_page(path):
    page = pages.get_or_404(path)
    #return render_template('page.html', page=page)
    html, toc = render_markdown(page.body)
    return render_template('page.html', page=page, html=html, toc=toc)

#[Create the utils for the sub main routes]===============================================================================================================

# Create route for dochub
@app.route('/dochub')
def dochub():
	return render_template('documents/index.html')


# Create dowload file facility
@app.route('/dochub/<path:filename>')
def download_file(filename):
	return send_from_directory('static/documents', filename, as_attachment=True)


# Create route for the courses mains
@app.route('/courses')
def courses():
	docnum = len([f for f in os.listdir(docsdir) if "[course]" in f])
	courses = {
		"bash" : "Learn Bash programming from scratch and master in 10 days by hands on projects, tutorials and linux system guidance, assuming that you have a linux system ready to run bash scripts. This is modular course, we increment step by step.[Essentials, Scripting]",
	}
	course_count = len(courses)
	return render_template('courses/index.html', courses=courses, course_count=course_count, docnum=docnum)

# Create route for the biology subject
@app.route('/subjects/biology')
def biology():
	docnum = len([f for f in os.listdir(docsdir) if "[bio]" in f])
	topics = {
	"organisms_and_populations" : "This topic is about how different organisms interact with each other in a population, the factors affecting it and study of ecology. Different organisms interact with each other differently. Population growth and the ecosystem, though are very large, these are all small worlds. Think about how diseases spread through different populations. Will they spread more in big population or in a small population? Which population will be fully infected if the infection started in the same time for both the big and small population? Read this lesson to learn more.[Ecology]",
	"molecular_basis_of_inheritance" : "How do organisms grow? Where are these informations stored? What is inheritance? Does your parents give you some sort of information for your growth? Have you ever wondered when someone says 'You look like your grandmother.'? Everything is routed in molecular biology, your cells and DNA. Explore this chapter to know more. [Biotechnology]",
	}
	topic_count = len(topics)
	return render_template('biology/index.html', topics=topics, topic_count=topic_count, docnum=docnum)


# Create route for cybersecurity mains
@app.route('/subjects/cybersecurity')
def cybersecurity():
	topics = {
	"cybersec0" : "This is the first step in learning cybersecurity. You are on right path to take the fundamentals, just step right in.[Basics]",
	"basic_tools" : "Know the basic tools of cybersecurity. Learn how to use Nmap, Burpsuite, Telnet, connect with CLI, etc.[Basics, Tools]",
	}
	topic_count = len(topics)
	return render_template('cybersecurity/index.html', topics=topics, topic_count=topic_count)

# Create route for sec-reports mains
@app.route('/analytical_domains/sec-reports')
def sec_reports():
	docnum = len([f for f in os.listdir(docsdir) if "[secreport]" in f])
	topics = {
	}
	topic_count = len(topics)
	return render_template('secreports/index.html', topics=topics, topic_count=topic_count, docnum=docnum)

# Create route for scene-scape mains
@app.route('/analytical_domains/scene-scape')
def scene_scape():
	docnum = len([f for f in os.listdir(docsdir) if "[scenescape]" in f])
	topics = {
	"rabrid-x133" : "An accidental global biowar scenario involving a genetically engineered rabies-like virus, set in a multipolar conflit. Rabies with only 12000 base pairs of genes is abundant in natural reserviors like dogs and other racoon like species, has -ssRNA. With advancing biotechnological and AI integration, the chances of mutating it is very high.[Hypothetical Scenario]",
	}
	topic_count = len(topics)
	return render_template('scenescape/index.html', topics=topics, topic_count=topic_count, docnum=docnum)


#[Create dynamic routes]===============================================================================================================

# Create dynamic route for subject
@app.route('/subjects/<subject>')
def route_subject(subject):
	return redirect(url_for('subject'))

# Create dynamic route for anadomain
@app.route('/analytical_domains/<anadomain>')
def route_analytical_domain(anadomain):
	return redirect(url_for('anadomain'))

# Create dynamic route for courses
@app.route('/courses/<course_name>')
def return_course(course_name):
	return redirect(url_for('course_name'))

# Create dynamic route for biology subject
@app.route('/subjects/biology/<topic>')
def biology_topic(topic):
	return redirect(url_for('topic'))

# Create dynamic route for cybersecurity topics
@app.route('/subjects/cybersecurity/<topic>')
def cybersecurity_topic(topic):
	return redirect(url_for('topic'))

# Create dynamic route for scene-scape topics
@app.route('/analytical_domains/scene-scape/<topic>')
def scene_scape_topic(topic):
	return redirect(url_for('topic'))

# Create dynamic route for cybersec tools
@app.route('/subjects/cybersecurity/basic_tools/<tool_name>')
def render_basic_tools(tool_name):
	return redirect(url_for('tool_name'))

# Create dynamic route for bash lessons
@app.route('/courses/bash/<module_name>')
def return_bash_module(module_name):
	return redirect(url_for('module_name'))

#[Routes for serving final html files]===============================================================================================================

@app.route('/courses/bash/')
def bash_course():
	modules = {
	"introduction" : "A shell is both a command language interpreter and a programming environment: it reads input, tokenizes and parses it, expands variables and patterns, redirects I/O, and executes commands.[module 0]",
	"basic_commands" : "In interactive mode, Bash reads commands from a terminal and provides features like prompts, history, and job control to aid live use. In non‑interactive mode, Bash reads commands from a file or string, which is how scripts run to automate tasks consistently and unattended.[module 1]",
	}
	return render_template('courses/bash/index.html', modules=modules)

@app.route('/analytical_domains/scene-scape/rabrid-x133')
def scene_scape_rabrid_x133():
	return render_template('scenescape/rabrid-x133.html')

@app.route('/subjects/biology/organisms_and_populations')
def organisms_and_populations():
	return render_template('biology/organisms_and_populations.html')

@app.route('/subjects/biology/molecular_basis_of_inheritance')
def molecular_basis_of_inheritance():
	return render_template('biology/molecular_basis_of_inheritance.html')

@app.route('/subjects/cybersecurity/cybersec0')
def cybersec0():
	return render_template('cybersecurity/cybersec0.html')

@app.route('/subjects/cybersecurity/basic_tools')
def basic_tools():
	tool_dict = {
		"nmap" : "Network Mapper, shortly known as Nmap, is a command line tool for checking and surfing open ports...[Tools]",
	}
	return render_template('cybersecurity/basic_tools.html', tool_dict=tool_dict)





#[Routes for cybersec tools]===============================================================================================================

@app.route('/subjects/cybersecurity/basic_tools/nmap')
def nmap():
	return render_template('cybersecurity/basic_tools/nmap.html')


#[Routes for bash lessons ]===============================================================================================================

@app.route('/courses/bash/introduction')
def bash_scripting_introduction():
	return render_template('courses/bash/introduction.html')

@app.route('/courses/bash/basic_commands')
def bash_scripting_module1():
	return render_template('courses/bash/module1.html')







#[Routes for dochub]===============================================================================================================

# biodoc route
@app.route('/dochub/biodoc')
def biodoc():
	unacademydocs = [f for f in os.listdir(docsdir) if "[bio]" and "[unacademy]" in f]
	qbdocs = [f for f in os.listdir(docsdir) if "[bio]" and "[qb]" in f]
	gendocs = [f for f in os.listdir(docsdir) if "[bio]" and "[gen]" in f]
	doccount = len(unacademydocs) + len(qbdocs) + len(gendocs)
	return render_template('documents/biodoc.html',unacademydocs=unacademydocs, qbdocs=qbdocs, gendocs=gendocs)

# compdoc route
@app.route('/dochub/compdoc')
def compdoc():
	netdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[net]" in f] #Networking
	hackdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[hack]" in f] #Hacking
	pydocs = [f for f in os.listdir(docsdir) if "[comp]" and "[pydoc]" in f] #Python documents and documentations
	gendocs = [f for f in os.listdir(docsdir) if "[comp]" and "[gen]" in f] # general documents
	cdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[cdoc]" in f] #C and C++ language documents
	jsdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[jsdoc]" in f] #Javascript documents
	javadocs = [f for f in os.listdir(docsdir) if "[comp]" and "[javadoc]" in f] # javadocuments
	fsdocs = [f for f in os.listdir(docsdir) if "[comp]" and "[fsdoc]" in f] #file systems and os documents
	doccount = len([f for f in os.listdir(docsdir) if "[comp]" in f])
	return render_template('documents/compdoc.html', netdocs=netdocs, hackdocs=hackdocs, pydocs=pydocs, gendocs=gendocs, cdocs=cdocs, jsdocs=jsdocs, javadocs=javadocs, fsdocs=fsdocs)

# weapdoc route
@app.route('/dochub/weapdoc')
def weapdoc():
	docs = [f for f in os.listdir(docsdir) if "[weap]" in f]
	return render_template('documents/weapdoc.html', docs=docs)




#[Routes for comming soons]===============================================================================================================

# websites
@app.route('/websites')
def websites():
	return render_template('comming_soon.html', title="My Websites", pgdesc="Welcome to my websites page. Here you can find the links to all of my other websites. Currently site under development.")

# codes
@app.route('/codes')
def codes():
	return render_template('comming_soon.html', title="My Codes", pgdesc="Welcome to my codes. Here you can find all of my codes. Soon I will post them all.")



#[main if condn for the sys]===============================================================================================================

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=port)


