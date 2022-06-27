from django.shortcuts import render, HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt


nextid = 4
topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ..'},
    {'id': 2, 'title': '크리에이트', 'body': '뷰 is ..'},
    {'id': 3, 'title': '리드', 'body': '모델 is ..'}
]


def index(request):
    article = '''
    <h2>웰컴</h2>
            Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))


# HttpResponse --> HTTP로 응답하겠다라는 겍체  str--> 문자열로 형변환

def HTMLTemplate(articleTag):
    global topics  # 변수를 사용하기위해서는 전역변슈를 지정해야함
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return f'''
        <html>
            <body>
                <hi><a href="/">장고</a></hi>
                <ol>
                    {ol}
                <ol>
                {articleTag}
                <ul>
                    <li><a href="/create/">create</a></li>
                </ul>
            </body>
        </html>
        '''


@csrf_exempt
def create(request):
    global nextid
    print('request.method', request.method)  # GET방식이면  request.method GET을 출력

    if request.method == 'GET':  # GET 방식일때
        article = '''
        <form action="/create">
            <p> <input type="text" name="title" placeholder="타이틀 입력"> </p>
            <p> <textarea name="이메일 주소" placeholder="이메일 입력"> </textarea></p>
            <p> <input type="submit"> </p>  
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))

    elif request.method == 'POST':
        title = request.POST['title']
        body =request.POST['body']
        newTopic ={"id":nextid,"title":title,"body":body}
        topics.append(newTopic)
        return HttpResponse('')


def read(request, id):
    return HttpResponse('리드' + id)
