from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""


    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)

    projects_and_grades = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            projects_and_grades=projects_and_grades
                            )
    return html

@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student. """

    return render_template("student_search.html")

@app.route("/add_student_form")
def add_student_form():

    return render_template("add_student_form.html")


@app.route("/student_added", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    html = render_template("student_added.html",
                            first_name=first_name,
                            last_name=last_name,
                            github=github
                            )
    return html



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
