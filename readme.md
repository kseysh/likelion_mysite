## cmd 관련 
###### pip install virtualenv
virtualenv myenv 명령어를 작성 시 "virtualenv는 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다" 라는 에러 발생 
따라서 제가 가상환경을 저장하고 싶은 공간에 새롭게 폴더를 만들고 터미널에서 그 디렉토리로 이동하여 
###### python -m venv “myenv” 
이런 식으로 가상환경을 세팅하는 방법을 택하였습니다. 

#### virtualenv와 venv의 차이
virtualenv는 Python 2와 Python 3.2 이하를 지원하고, 시스템 패키지를 사용하거나 activate 스크립트를 자동으로 생성하는 기능이 있습니다.    
반면, python -m venv는 Python 3.3 이상을 지원하고 Python에 내장되어 있으며 activate 스크립트를 생성하지 않습니다.

#### 가상환경 실행과 사이트 구축
가상환경을 실행하고 싶다면 가상환경 안의 Scripts 폴더에 들어가서 activate.bat이라는 파일을 실행시켜준다.

가상환경을 만드는 이유 -> 가상환경 마다 다른 개발환경을 구축할 수 있기 때문
프로젝트 시작 시 django-admin startproject mysite를 사용하여 사이트 구축

###### py manage.py runserver
서버를 구동시키기 위해 이용하는 명령어
미적용 마이그레이션에 관한 경고 메시지가 생성되었습니다.
장고 프로젝트의 루트 디렉토리에서 python manage.py migrate를 통해 미적용 마이그레이션 경고를 해결하였습니다.

>#### migration이란?
>데이터베이스의 구조를 관리하는 명령어로서 우리가 Django 프로젝트를 개발하다가, 모델을 수정하거나 새로운 모델을 추가하면, 데이터베이스에도 그것을 반영해줘야 합니다. 그래야만 모델의 변경사항을 데이터베이스에서도 사용할 수 있기 때문입니다. 즉, migrate 명령어는 Django에서 모델과 데이터베이스 간의 일관성을 유지하고, 모델의 변경사항을 데이터베이스에 적용하는 역할을 합니다.
>makemigrations는 마이그레이션 파일을 생성하고, migrate는 마이그레이션 파일을 실행하여 실제 데이터베이스 스키마를 변경합니다.

###### py manage.py startapp polls
Python 어플을 만드는 명령어 장고 프로젝트의 루트 디렉토리에서 polls라는 이름의 어플을 생성해줍니다.

###### py manage.py createsuperuser
관리자 사이트를 생성하는 명령

<hr>

## 장고에 대해서
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

### django-admin startproject를 하게 되면 생성되는 파이썬 파일들이 있다.
* __init__.py: 이 디렉토리를 Python 패키지로 간주해야 함을 Python에 알리는 빈 파일입니다.
* settings.py: 이 Django 프로젝트에 대한 설정/구성입니다.
* urls.py: 이 Django 프로젝트에 대한 URL 선언
* wsgi.py: 웹서버와 장고 프레임워크를 연결해준다.

### py manage.py startapp을 하게 되면 생성되는 파이썬 파일들
* admin.py : 관리자 사이트에서 모델을 어떻게 보여줄지, 어떤 액션을 취할지 등을 정의합니다.
* apps.py : 프로젝트의 앱들에 대한 설정을 담고 있습니다. 앱 이름, 별칭, 설정 등을 관리합니다.
* models.py : 데이터베이스의 테이블을 정의하는 역할을 합니다. 이 파일에서는 각 테이블의 필드와 관계를 정의할 수 있습니다.
>#### DRY 원칙이란?
>models.py에서는 Question과 Choice라는 두 개의 클래스를 만들어 활용하였습니다. Question과 Choice를 만들어놓고 적재적소에 활용하기 위함입니다. 이렇게 만들지 않았다면, 아마 중복된 코드를 여기저기에 만들고 사용해야 했을 것입니다. 이와 관련한 원칙을 DRY 원칙이라고 합니다.
>##### Don't Repeat Yourself
>중복 코드를 최소화하고 유지보수성, 확장성, 재사용성 등을 개선하기 위한 설계 원칙입니다. 이 원칙은 코드의 중복을 피하고, 코드를 수정할 때에는 최소한의 수정으로 원하는 결과를 얻을 수 있도록 설계해야 한다는 의미입니다.
>DRY 원칙을 준수하는 코드는 다음과 같은 특징을 가집니다.
>* 코드의 중복이 최소화된다.
>* 코드의 유지보수성이 높아진다.
>* 코드의 재사용성이 높아진다.
>* 코드의 확장성이 높아진다.
>DRY 원칙은 코드의 재사용성을 높이기 위해 함수, 클래스, 모듈 등을 잘게 나누는 것을 권장합니다. 또한 코드의 중복을 최소화하기 위해 상수, 변수, 함수 등을 재사용하고, 코드를 수정할 때에는 최소한의 수정으로 원하는 결과를 얻을 수 있도록 설계해야 한다는 의미입니다. 
* tests.py : 각 모델, 뷰, 폼, 템플릿 등의 유효성 검사를 작성할 수 있습니다.
* urls.py : URL 패턴을 정의합니다. 웹 브라우저로부터 요청이 오면, 해당 요청을 처리하는 뷰를 찾아내기 위해 URL 패턴을 검색합니다.
> #### URLConf란?
>urls.py 파일에서 코드를 작성하다 보면 URLConf라는 단어가 많이 나옵니다. URLConf는 뭘까요?
>URLConf는 URL Configuration의 약어로 URL과 view를 매핑(연결)하는 설정입니다. 
>URLConf를 이용하여 Django 앱의 URL을 정의하고, 각 URL을 해당하는 뷰(View)나 다른 URLConf와 연결합니다.
* views.py : 애플리케이션의 비즈니스 로직을 작성합니다. 이 파일에서는 요청을 처리하고, 데이터를 처리하고, 응답을 생성하는 함수를 작성할 수 있습니다.
* manage.py : Django 프로젝트의 유틸리티 스크립트입니다. 서버를 시작하거나 데이터베이스를 관리하는 등의 작업을 수행할 수 있습니다.

#### Django Template 언어
장고에서 HTML 파일을 작성할 때 사용하는 문법으로 HTML과 유사하지만, Django에서 제공하는 특별한 문법을 사용할 수 있습니다.
##### {{ }} 중괄호
Python 코드에서 생성한 값을 출력하기 위해 사용하며 변수를 중괄호 안에 둘러싸서 활용합니다.
예를 들어, {{ my_variable }}은 my_variable이라는 변수의 값을 출력합니다
##### {{% %}} 중괄호와 퍼센트기호
if문, for문 등의 제어문을 사용하기 위해 사용합니다,
예를 들어, if문은 {% if %}로 시작하여 {% endif %}로 끝내고,
for in 문은  {% for i in object %}로 시작하여 {% endfor %} 로 끝냅니다.
   
추가적으로 주석은 {# 주석 #} 이런 방식으로 생성할 수 있습니다.
## 느슨한 결합 다시 이해하기


## POST 방식과 GET 방식의 차이
이번 투표앱을 만들면서 HTML 파일의 form태그를 이용해 views.py로 POST 방식을 이용해 사용자가 투표한 내용을 보내는 코드를 작성한 적이 있습니다. 
장고 튜토리얼에서는 method를 get이 아닌 post로 사용해야하는 것은 중요하다라고 이야기 합니다. 그러면 get과 post 방식의 차이는 무엇이고 왜 투표앱에서는 post 방식을 사용해야 할까요?

##### get request
get 요청은 URL을 통해 데이터를 전송하며, 클라이언트에서 서버로 정보를 요청하기 위해 사용되는 메서드입니다. 
GET 요청은 URL의 끝에 쿼리스트링(query string)을 붙여서 데이터를 전송합니다. 쿼리스트링은 ?으로 시작하며, key=value 형태로 구성됩니다. 여러 개의 키-값 쌍을 전송할 때는 &로 구분합니다.

유튜브에서 영상을 검색하게 되면 get 요청을 통해 영상을 검색하는 것을 확인할 수 있습니다. 저번 파이썬 세션에서 유튜브 분석 api를 만들었을 때 영상의 id를 가지고 오기 위해 유튜브의 주소에서 id를 찾은 것을 생각해보면 get 요청이 url에 데이터를 담는다는 의미를 쉽게 이해하실 수 있을 것이라고 생각합니다.

추가적으로 get은
* 캐싱할 수 있습니다
* 브라우저 기록에 남습니다
* 북마크에 추가할 수 있습니다
* 데이터 길이에 대한 제한이 있습니다.

>캐싱이란?
>클라이언트가 웹 서버에 한번 페이지에 접근 후 해당 페이지를 또 요청할 시 빠르게 접근하기 위해 방문시 요청한 데이터를 저장해 두고 동일한 요청을 할 때 사용하여 서버에 대한 요청을 줄이기 위해 사용하는 방식

##### post request
POST 요청은 HTTP 메시지의 body라고 불리는 공간에 데이터를 넣고 전송하며 리소스를 생성/업데이트하기 위해 서버에 데이터를 보내는 데 사용합니다.
예를 들어, 로그인 폼을 작성하고 제출할 때 POST 요청을 사용합니다. POST 요청은 데이터를 서버에 제출하는 요청으로, 서버는 이에 대한 처리를 하고 결과를 반환합니다. 
POST 요청은 데이터의 길이에 제한이 없고, URL에 데이터가 노출되지 않으므로 get보다 보안 면에서 안전합니다. 따라서 데이터를 서버에 제출하고나, 상태를 변경할 때 사용됩니다. 예를 들어 로그인 정보 제출 (로그인 정보가 url에서 표시되면 안되므로), 게시글 작성(대용량 데이터를 전송) 이 있습니다.
> post방식이라고 무조건 보안면에서 믿지 말아야 하는 이유!
> post 방식이 get방식보다 보안면에서 우수한 것은 맞지만, post 요청으로 전송한 데이터도 결국 크롬 개발자 도구같은 툴로 요청 내용을 확인 할 수 있기 때문에 민감한 비밀번호 같은 데이터들은 꼭 암호화를 해주어야 합니다.

##### 비교 정리표
<table style="border-collapse:collapse" border="1"> 
    <tr>
        <td> HTTP Method </td>
        <td> GET 방식 </td>
        <td> POST 방식 </td>
    </tr>
    <tr>
        <td> 사용 목적 </td>
        <td> 서버의 리소스에서 데이터를 요청하기 위함 </td>
        <td> 서버의 리소스를 새로 생성하거나 갱신하기 위함 </td>
    </tr>
    <tr>
        <td> 데이터가 담기는 곳 </td>
        <td> HTTP 패킷 Header </td>
        <td> HTTP 패킷 Body </td>
    </tr>
    <tr>
        <td> 리소스 전달 방식 </td>
        <td> 쿼리스트링 </td>
        <td> HTTP Body </td>
    </tr>
    <tr>
        <td> 캐싱 가능 여부 </td>
        <td> O </td>
        <td> X </td>
    </tr>
    <tr>
        <td> 브라우저 기록 </td>
        <td> O </td>
        <td> X </td>
    </tr>
    <tr>
        <td> 데이터 길이 제한 </td>
        <td> O </td>
        <td> X </td>
    </tr>

    
</table>

