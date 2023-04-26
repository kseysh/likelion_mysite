from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World.")
# Django의 views.py 파일은 웹 어플리케이션의 요청(request)을 처리하고, 적절한 HTTP 응답(response)을 반환하는 함수들을 포함합니다.
#HttpResponse는 Django에서 가장 기본적인 HTTP 응답 객체 중 하나입니다. 이 객체를 사용하면, 단순한 문자열, HTML 코드, JSON 데이터 등을 포함한 응답을 생성할 수 있습니다.