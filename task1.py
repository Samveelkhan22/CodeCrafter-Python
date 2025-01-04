def rank_students(students_scores):
    # Sort the students by scores in descending order
    sorted_students = sorted(students_scores, key=lambda x: x[1], reverse=True)
    
    # Assign ranks using enumerate
    ranked_students = [(rank + 1, student, score) for rank, (student, score) in enumerate(sorted_students)]
    
    return ranked_students


# Example list of students and their scores
students_scores = [
    ("Alice", 95),
    ("Bob", 85),
    ("Charlie", 95),
    ("Diana", 80),
    ("Eve", 90)
]

# Get ranked list of students
ranked_students = rank_students(students_scores)

# Display the results
print("Ranked Students:")
for rank, student, score in ranked_students:
    print(f"Rank {rank}: {student} with a score of {score}")
