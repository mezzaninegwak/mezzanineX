# ---------------------------------------- [edit] ---------------------------------------- #
from flask import Blueprint, render_template

from flask_test_2.models import Question
# ---------------------------------------------------------------------------------------- #

...

@bp.route('/')
def index():
    # ---------------------------------------- [edit] ---------------------------------------- #
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)
    # ---------------------------------------------------------------------------------------- #