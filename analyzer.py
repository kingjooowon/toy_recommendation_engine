import json, os
from recommender import build_transition_table, build_probability_table, recommend_next

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "sample_sequences.json")

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
if __name__ == "__main__":
    sequences = read_json("sample_sequences.json")
    transition = build_transition_table(sequences)
    recommend_next_view = recommend_next(transition, "view")
    probabilities = build_probability_table(transition)
    
    print("Transition Table: ")
    for curr, nexts in transition.items():
        for nxt, count in nexts.items():
            print(f"{curr} -> {nxt} ({count})")
            
    print("\nRecommendation: ")
    print(f"After 'view' -> {recommend_next_view}({probabilities["view"][recommend_next_view]})")