### 1강 장고 설치
pip install virtualenv
virtualenv myenv 명령어를 작성 시 "virtualenv는 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다" 라는 에러 발생 
따라서 내가 가상환경을 저장하고 싶은 공간에 새롭게 폴더를 만들고 터미널에서 그 디렉토리로 이동하여 python -m venv “myenv” 이런 식으로 가상환경을 세팅하는 방법을 택하였다. 

virtualenv는 Python 2와 Python 3.2 이하를 지원하고, 시스템 패키지를 사용하거나 activate 스크립트를 자동으로 생성하는 기능이 있습니다. 반면, python -m venv는 Python 3.3 이상을 지원하고 Python에 내장되어 있으며 activate 스크립트를 생성하지 않습니다.
