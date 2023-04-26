### cmd 관련 
###### pip install virtualenv
virtualenv myenv 명령어를 작성 시 "virtualenv는 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다" 라는 에러 발생 
따라서 제가 가상환경을 저장하고 싶은 공간에 새롭게 폴더를 만들고 터미널에서 그 디렉토리로 이동하여 
###### python -m venv “myenv” 
이런 식으로 가상환경을 세팅하는 방법을 택하였습니다. 

virtualenv는 Python 2와 Python 3.2 이하를 지원하고, 시스템 패키지를 사용하거나 activate 스크립트를 자동으로 생성하는 기능이 있습니다.    
반면, python -m venv는 Python 3.3 이상을 지원하고 Python에 내장되어 있으며 activate 스크립트를 생성하지 않습니다.

가상환경을 실행하고 싶다면 가상환경 안의 Scripts 폴더에 들어가서 activate.bat이라는 파일을 실행시켜준다.

가상환경을 만드는 이유 -> 가상환경 마다 다른 개발환경을 구축할 수 있기 때문
프로젝트 시작 시 django-admin startproject mysite를 사용하여 사이트 구축

###### py manage.py runserver
서버를 구동시키기 위해 이용하는 명령어
미적용 마이그레이션에 관한 경고 메시지가 생성되었습니다.
장고 프로젝트의 루트 디렉토리에서 python manage.py migrate를 통해 미적용 마이그레이션 경고를 해결하였습니다.

>migration이란?
>데이터베이스의 구조를 관리하는 명령어로서 우리가 Django 프로젝트를 개발하다가, 모델을 수정하거나 새로운 모델을 추가하면, 데이터베이스에도 그것을 반영해줘야 합니다. 그래야만 모델의 변경사항을 데이터베이스에서도 사용할 수 있기 때문입니다. 즉, migrate 명령어는 Django에서 모델과 데이터베이스 간의 일관성을 유지하고, 모델의 변경사항을 데이터베이스에 적용하는 역할을 합니다.



> 장고를 이해하기 위해서는 장고의 request cycle에 대한 이해가 선행되어야 한다고 생각합니다.
>
> # [ 장고 request cycle 이미지 넣기 ]
>
>   >1. client가 웹에 대한 정보를 요청
>   >2. Nginx/Apache와 같은 web server가 요청을 받음 (장고에서는 개발을 위한 경량 개발 웹서버가 제공된다. 하지만 배포할 때는 Nginx/Apache와 같은 web server를 이용하여 배포해야 한다.)
>   >3. wsgi를 통해 웹서버와 장고 프레임워크를 연결해준다. 
>   >4. 사용자가 특정 주소를 요청한다.
>   >5. url 파일에서 요청한 주소를 잘게 나눈다.(파싱)
>   >6. 잘게 나눠진 주소는 view.py로 이동한다. (view에는 웹사이트를 위한 코드들이 있다.) ex) 데이터 저장, 데이터 베이스에서 꺼내옴
>   >7. Template에서 디자인 담당 (html)
>   >8. Template가 response를 받는다.

django-admin startproject를 하게 되면 생성되는 파이썬 파일들이 있다.
* __init__.py: 이 디렉토리를 Python 패키지로 간주해야 함을 Python에 알리는 빈 파일입니다.
* settings.py: 이 Django 프로젝트에 대한 설정/구성입니다.
* urls.py: 이 Django 프로젝트에 대한 URL 선언
* wsgi.py: 웹서버와 장고 프레임워크를 연결해준다.

