import random

# Simulated content database
content_db = {
    "Math": ["Algebra Basics", "Geometry Shapes", "Fractions", "Decimals"],
    "Science": ["Plants", "Animals", "Water Cycle", "Solar System"],
    "English": ["Vocabulary", "Grammar Basics", "Reading Comprehension", "Writing Skills"]
}

# Each student will have an interaction profile
class StudentProfile:
    def __init__(self, name):
        self.name = name
        # Track interaction scores with each topic
        self.topic_scores = {}  # e.g., {"Algebra Basics": 5, "Fractions": 2}
    
    def update_score(self, topic, score):
        if topic in self.topic_scores:
            self.topic_scores[topic] += score
        else:
            self.topic_scores[topic] = score

    def get_preference(self):
        # Returns the subject student shows most interest in
        if not self.topic_scores:
            return random.choice(list(content_db.keys()))
        
        topic = max(self.topic_scores, key=self.topic_scores.get)
        for subject, topics in content_db.items():
            if topic in topics:
                return subject
        return random.choice(list(content_db.keys()))

def recommend_next_topic(student_profile):
    preferred_subject = student_profile.get_preference()
    topics = content_db[preferred_subject]

    # Recommend the topic the student has not yet interacted with or least interacted
    scores = {topic: student_profile.topic_scores.get(topic, 0) for topic in topics}
    next_topic = min(scores, key=scores.get)
    return preferred_subject, next_topic

# === Simulated interaction ===
def simulate_learning_session(student_profile):
    subject, topic = recommend_next_topic(student_profile)
    print(f"🧠 Recommended for {student_profile.name}: {topic} in {subject}")

    # Simulate interaction (e.g., quiz taken, time spent)
    interaction_score = random.randint(1, 5)
    student_profile.update_score(topic, interaction_score)
    print(f"✔️  {student_profile.name} completed '{topic}' and earned score: {interaction_score}\n")

# === Main Loop ===
if __name__ == "__main__":
    student = StudentProfile("Asha")

    for _ in range(5):  # simulate 5 learning sessions
        simulate_learning_session(student)

    print("Final Learning Profile:")
    print(student.topic_scores)
