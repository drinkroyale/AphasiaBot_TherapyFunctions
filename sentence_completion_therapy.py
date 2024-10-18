# Sentence Therapy
def sentence_therapy():
    sentences = [
        {"sentence": "The cat is sleeping on the couch.", "question": "Is the cat awake?", "answer": "no"},
        {"sentence": "The sun is shining brightly.", "question": "Is it raining?", "answer": "no"},
        {"sentence": "The boy is reading a book.", "question": "Is the boy playing a game?", "answer": "no"}
    ]
    
    score = 0
    for item in sentences:
        print(f"Sentence: {item['sentence']}")
        print(f"Question: {item['question']}")
        
        response = input("(yes/no): ")
        
        if response.lower() == item['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"Your final score is: {score}/{len(sentences)}")

sentence_therapy()
