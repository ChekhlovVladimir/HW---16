import json


def receiving_candidates():
    with open("candidates.json", encoding="utf-8") as my_file:
        candidates = json.load(my_file)

    return candidates


def candidate_by_id(person_id):
    candidates = receiving_candidates()
    for candidate in candidates:
        if person_id == candidate["id"]:
            return candidate


def candidates_by_skills(skills):
    candidates = receiving_candidates()
    skill_list = []
    lowered_skills = skills.lower()

    for candidate in candidates:
        splitted_skills = candidate["skills"].lower().split(",")
        if lowered_skills in splitted_skills:
            skill_list.append(candidate)
    return skill_list


def candidate_matching():
    candidates = receiving_candidates()
    container = ""
    for candidate in candidates:
        container += (f"{candidate['name']}\n "
                      f"{candidate['position']}\n"
                      f"{candidate['skills']}\n"
                      "-----------------\n"
                      )

    return container



