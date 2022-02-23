from flask import Flask, render_template
from classes import CandidatesData

app = Flask(__name__)


@app.route("/")
def page_index():
    """
    Вывод всех кандидатов из списка в браузере.
    :return: Полный список с определенными строками.
    """
    candidates_data = CandidatesData("candidates.json")
    return render_template("all_candidates.html", candidates=candidates_data.load_candidates_from_json())


@app.route("/candidate/<int:candidate_id>")
def page_candidate_id(candidate_id):
    """
    Вывод кандидата по его порядковому номеру
    """
    candidates_data = CandidatesData("candidates.json")
    candidate = candidates_data.get_candidate(candidate_id)
    return render_template("one_candidate.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_candidate_name(candidate_name):
    """
    Получение кандидата по его имени
    """
    candidates_data = CandidatesData("candidates.json")
    candidates = candidates_data.get_candidates_by_name(candidate_name)
    counted_candidates = len(candidates)
    return render_template("search_name.html", counted_candidates=counted_candidates, candidates=candidates,
                           candidate_name=candidate_name)


@app.route("/skill/<skill_name>")
def page_candidate_skill(skill_name):
    """
    Вывод кандидата по навыку
    """
    candidates_data = CandidatesData("candidates.json")
    candidates = candidates_data.get_candidates_by_skill(skill_name)
    counted_candidates = len(candidates)
    return render_template("search_skill.html", counted_candidates=counted_candidates, candidates=candidates,
                           skill_name=skill_name)


app.run()
