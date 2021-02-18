import re
from collections import defaultdict
def solution(word, pages):

    # 기본 점수 : 검색어가 등장하는 횟수(not case-sensitive)
    # 외부 링크 수 : 현재 웹 페이지 -> 다른 외부페이지 연결 링크 수
    # 링크 점수 : 현재 웹 페이지의 링크가 걸린 다른 웹페이지의 기본 점수 / 외부 링크 수의 합
    # 매칭 점수 : 기본 점수 + 링크 점수

    # 파싱해서 얻어내야하는 것 : url, index, word

    # 현재 페이지 url : [기본 점수, 외부 링크 수, 링크 점수]
    urls = dict()

    out = defaultdict(list)

    for page in pages:
        spilted_page = page.split('<body>')
        # 현재 링크
        my_url = re.search(r'<meta[^>]*content="([\S]*)"/>', spilted_page[0]).group(1)
        urls[my_url] = [0, 0, 0, 0]
        # 기본 점수 구하기
        count = count_word(word, spilted_page[1])
        urls[my_url][0] = count
        # 외부 링크 구하기 -> out 딕셔너리에서 카운트
        out_urls = re.findall(r'<a href="(.*?)">', spilted_page[1])
        for out_url in out_urls:
            # 현재 url에서 외부 링크가 어떤게 있는지
            out[out_url].append(my_url)
            # url이 다른 곳에서 몇 번 등장했는지 카운트 해야하므로
            urls[my_url][1] += 1


    # 링크 점수
    for url in urls:
        # 링크 점수 = 기본 점수 / 외부 링크 수
        if urls[url][1] > 0:
            urls[url][2] = urls[url][0] / urls[url][1]

    answer = []

    # 현재 페이지 url : [기본 점수, 외부 링크 수, 링크 점수]
    for url in urls:
        # 기본점수 더해주고
        matching_score = float(urls[url][0])
        for out_link in out[url]:
            # 외부 링크점수 더해주고
            matching_score += float(urls[out_link][2])
        answer.append(matching_score)

    max_index = 0
    for index in range(len(urls)):
        if answer[max_index] < answer[index]:
            max_index = index
    return max_index

def count_word(target, body):
    answer = 0
    lowercase_target = target.lower()
    lowercase_body = body.lower()
    for word in re.findall(r'[a-z]+', lowercase_body):
        if word == lowercase_target:
            answer += 1
    return answer
