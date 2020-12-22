def solution(phone_book):
    length = len(phone_book)
    phone_book.sort()

    if length == 1:
        return True

    for i in range(length - 1):
        prefix = phone_book[i]
        prefix_len = len(prefix)
        for j in range(i + 1, length):

            # 각 전화번호의 길이가 1이상이므로 0으로 하드코딩 가능
            if phone_book[i][0] != phone_book[j][0]: break

            # prefix인지 확인
            if phone_book[j].find(phone_book[i]) != -1:
                return False

    return True
