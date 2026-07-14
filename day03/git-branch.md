# Git Branch

## Git Branch이란? 
나뭇가지처럼 여러 갈래로 작업 공간을 나눔

## Git Branch 장점
각자 다른 작업 가능 (e.g. article, auth 작업 따로) 

## Branch 명령어
git branch  내가 현재 보유하고 있는 브랜치 목록 보여줘
git branch -r  원격 저장소에 브랜치 목록 보여줘
git switch [branch명]  다른 브랜치로 이동
git branch [branch명]  새 브랜치 생성

git merge [branch명]  두 브랜치를 하나로 병합
- git merge hotfix  마스터에서 hotfix 작업사항 불러오기
- git merge master  hotfix에서 마스터 작업사항 불러오기

## Git Merge
1. fast-forward merge  한 줄로만 만들어도 되는 머지 형태
2. three-way merge  merge시 새 커밋(변경사항)을 만들어야 할 때


단, 모두가 작업할 내용을 원격 컴퓨터에 올린다. (git push)
그리고 나는 dev 브랜치와 내 작업 브랜치만 신경쓴다. 