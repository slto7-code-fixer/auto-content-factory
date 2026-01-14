import random

def get_idea():
    ideas = [
        "رسالة هتغير تفكيرك",
        "حكمة قصيرة لكن مؤثرة",
        "شيء بسيط ممكن ينقذ يومك"
    ]
    return random.choice(ideas)
