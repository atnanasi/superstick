def question(text):
    while True:
        answer = input(text+":")
        if(not answer):
            break
    
    return answer
