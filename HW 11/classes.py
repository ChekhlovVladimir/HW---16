import json


class CandidatesData:
    def __init__(self, path):
        self.path = path

    def load_candidates_from_json(self):
        with open(self.path, "r", encoding="utf-8") as my_file:
            data = json.load(my_file)
            return data

    def get_candidate(self, candidate_id):
        candidates = self.load_candidates_from_json()
        for candidate in candidates:
            if candidate["id"] == candidate_id:
                return candidate

    def get_candidates_by_name(self, candidate_name):
        candidates = self.load_candidates_from_json()
        list_candidates = []
        for candidate in candidates:
            if candidate_name.lower() in candidate["name"].lower():
                list_candidates.append(candidate)
                return list_candidates

    def get_candidates_by_skill(self, skill_name):
        candidates = self.load_candidates_from_json()
        skills_candidates = []
        for candidate in candidates:
            if skill_name.lower() in candidate["skills"].strip().lower().split(", "):
                skills_candidates.append(candidate)
                return skills_candidates
