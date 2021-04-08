Playbook은 JSON은 기반으로 약간의 표현규칙을 추가한 화일로서 github repository내 playbook.csv 화일을 현재 구현한 web server에서 git pull 함으로 데모 버전에서 live 버전에 적용되는 형태로 되어있다.

좀더 유연한 형태로 수정을 허용하기위해, 이 화일을 google spreadsheet으로 구성하고, playbook.py 에서 on-the-fly 로 바로 읽어가는 방법으로 구현하게되면 극단적으로 유연한 수정과 관리가 가능해질 수 있다. (현재는 구현에 미포함되어있고, 최초 아래의 구글에서 작성된 내용은 playbook.csv 형태로 저장되어 사용중)

https://docs.google.com/spreadsheets/d/1HRpjR7VKiyH5NrL4f50IM1im6WrFGbs5g-i7tu1fJk0/edit#gid=0 
