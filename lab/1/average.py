QUIZZES = 5
total = 0

for _ in range(QUIZZES):
    total += float(input())

average = total / QUIZZES
average = round(average,2)

print(average)
