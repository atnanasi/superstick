def question(text):
    while True:
        answer = input('[?] {} > '.format(text))
        if answer:
            break

    return answer

def isok(text):
    answer = input('[?] {} (press enter to continue)'.format(text))
    return False if answer else True

def info(text):
    print('{}'.format(text))

def warn(text):
    print('[!] {}'.format(text))
