def solution(files):
    answer = []

    for file_name in files:
        HEAD, NUMBER, TAIL = parsing(file_name)
        answer.append([HEAD, NUMBER, TAIL, file_name])

        print(HEAD, NUMBER, TAIL)

    s = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    print(s)

    return answer

def parsing(file_name):
    HEAD, NUMBER, TAIL = "", "", ""

    file = ''
    if '.' not in file_name:
        file = file_name
    else:
        file, TAIL = file_name.split('.')


    for i in range(len(file)):
        if is_number(file[i]):
            HEAD, NUMBER = file[:i], file[i:]
            break

    for i in range(len(NUMBER)):
        if not is_number(NUMBER[i]):
            NUMBER = NUMBER[:i]
            TAIL = NUMBER[i:] + TAIL
            break

    return HEAD, NUMBER, TAIL

def is_number(num):
    return 48 <= ord(num) <= 57

solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
