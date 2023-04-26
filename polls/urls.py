from django.urls import path

from . import views

app_name = "polls"
#app이 많아지면 템플릿에서 url 'detail'처럼 사용하였을 때
# 이 앱들의 url을 구별하기 위해 
#app_name을 추가하여 앱의 이름 공간을 설정해준다.
# 이제 템플릿에서 url 'polls:detail' 처럼 상세 뷰를 가리킬 수 있도록 코드를 작성하면 장고가 뷰를 쉽게 구분 할 수 있다.
# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     #전달 받은 값이 아무것도 없으면 view.index로 연결을 시켜준다.
#     #name 매개변수는 해당 URL 패턴에 대한 고유한 이름을 지정하는 것으로, 
#     # 이를 이용해 템플릿 등에서 URL 패턴을 참조할 수 있습니다.
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),

#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]  

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
] # 제네릭 뷰를 사용하여 코드를 적게 사용할 수 있다.

# IndexView, DetailView, ResultsView는 Django에서 제공하는 제네릭 뷰(Generic View)입니다
    #question_id를 인수로 전달하면, views.함수에서 값을 받아서 사용한다.
    #URL에서 값을 캡처하기 위해 꺾쇠 괄호를 사용한 것.
    #모든 URL에 슬래시가 있으므로 선행 슬래시는 사용하지 않는다.