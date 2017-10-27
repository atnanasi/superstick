def question(text):
    while True:
        answer = input(text+":")
        if answer:
            break

    return answer

def isok(text):
    answer = input(text+"(Yes->Enter / No-> other)")
    return False if answer else True
