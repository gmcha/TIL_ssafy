# 원격 저장소 (GitHub, GitLab)

## github 사용법 설정
원격 브랜치 설정
- 기본 브랜치는 master로 바꿉니다. (Git, GitLab와 동일하게 설정)

원격 저장소 생성
- 이미 로컬에 하고 있던 작업이 있다면 -> 원격 저장소 비워서 생성 

## 원격 저장소 사용 명령어 (git push, pull, clone)
git remote add origin [주소]  원격 저장소 추가 (주소, 별명-origin)
git remote -v  연결된 원격 저장소 목록
git push origin master  origin에 내 master의 내용으로 push
- git push -u origin master
- git push

git clone [주소]  남의 주소를 최초로 복제

## fork란?
관련 없는 프로젝트에 기여하고 싶을 때 사용
