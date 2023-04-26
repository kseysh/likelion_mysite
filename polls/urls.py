from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    #전달 받은 값이 아무것도 없으면 view.index로 연결을 시켜준다.
    #name 매개변수는 해당 URL 패턴에 대한 고유한 이름을 지정하는 것으로, 이를 이용해 템플릿 등에서 URL 패턴을 참조할 수 있습니다.
]