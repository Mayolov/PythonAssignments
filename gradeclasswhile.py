def display_grade(score):
    if score >= 90 :
        print('A')
    elif score >= 80 :
        print('B')
    elif score >= 70 :
        print('C')
    elif score >= 60 :
        print('D')
    else:
        print('f')

def get_score():
    valid = False
    
    while not valid:
        score = float(input('Enter a score 0-100, or -1 to finish: '))
        if score == -1 or (score >= 0 and score <= 100):
            valid = True
        else:
            print('please enter valid score')
        
    return score

def main():
    count_scores = 0
    total_scores = 0
    
    finished = False
    
    while not finished:
        score = get_score()
        
        if score == -1:
            finished = True
        else:
            display_grade(score)
            count_scores += 1
            total_scores += score
        
    if count_scores > 0:
        average = total_scores / count_scores
        print(f"Total number of scores: {total_scores}")
        print(f"Average score: {average:.2f}")
    else:
        print("No scores entered, no scores computed")

main()
                