from flask import Flask, render_template, request
import requests
from responder import Responder
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
# temp_db = create_engine('sqlite:///:memory:')

# posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


comms = open("text/comms.txt").read().splitlines()
journalism = open("text/journalism.txt").read().splitlines()
pr = open("text/pr.txt").read().splitlines()
media = open("text/media.txt").read().splitlines()
media_relations = open("text/media_relations.txt").read().splitlines()
lecturer = open("text/lecturer.txt").read().splitlines()
change_management = open("text/change_management.txt").read().splitlines()
dei = open("text/dei.txt").read().splitlines()
posts = [

  {
    "id":1,
    "title":"Strategic Communications Specialist",
    "subtitle":"The Power of Communication",
    "heading":"Strategic Communications Specialist | Campaign Strategist",
    "body": comms,
    "image_url": "coffee.jpeg"
  },
  {
    "id":2,
    "title":"Media Relations",
    "subtitle":"Shaping Stories, Building Brands & Reputations",
    "heading":"Organisational Change Management",
    "body": media_relations,
    "image_url":"rayinterview.jpeg"
  },
  {
    "id":3,
    "title":"Publicist | PR Specialist",
    "subtitle":"Lights, Camera, Publicity: Your Film's Success",
    "heading":"Publicist | PR",
    "body": pr,
    "image_url":"getgone.png"
  },
  {
    "id":4,
    "title":"Journalist",
    "subtitle":"Where Stories Soar and Messages Resonate",
    "heading":"Journalism",
    "body": journalism,
    "image_url":"bbc1.jpeg"
  },
  {
    "id":5,
    "title":"Multi-Media",
    "subtitle":"Where your vision meets mastery",
    "heading":"Multi-Media",
    "body": media,
    "image_url":"sign.jpeg"
  },
  {
    "id":6,
    "title":"Lecturer",
    "subtitle":"Your Playbook to Prosperity",
    "heading":"Lecturer",
    "body": lecturer,
    "image_url":"LecturingSingapore2.jpeg"
  },
  {
    "id":7,
    "title":"Change Management",
    "subtitle":"From Chaos to Opportunity",
    "heading":"Change Management",
    "body": change_management,
    "image_url":"closeup2.jpeg"
  },
  {
    "id":8,
    "title": "DEI Consultant & Trainer",
    "subtitle": "Let's Change the World Together",
    "heading": "DEI Consultant & Trainer",
    "body": dei,
    "image_url": "singapore_lecture.JPG"
  }
]


app = Flask(__name__)


@app.route('/form-entry', methods=["POST", "GET"])
def receive_data():
     if request.method == "POST":
         data = request.form
         email = Responder.send_email(name=data["name"],email=data["email"], message=data["message"], phone=data["phone"])
         return render_template("contact.html", msg_sent=True)
     return render_template("contact.html", msg_sent=False)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
