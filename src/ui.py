def question(text):
    while True:
        answer = input(text+":")
        if(not answer):
            break

    return answer

def isok(text):
    while True:
        answer = input(text+"(Yes->Enter / No-> other)")
        if(not answer):
            return False

    return True
