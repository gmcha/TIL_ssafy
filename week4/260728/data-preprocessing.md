# Python을 활용한 데이터 수집과 전처리

## Requests

파이썬과 함께 하는 외부 요청 (API) → 이를 위한 파이썬 라이브러리 ‘**Requests**’

global (가상 환경 없이 설정) - `pip install ##`, `pip list`

### 01_requests.py

\*\*딕셔너리 - 키가 정렬되지 않음.

- Requests 라이브러리로 API에 get 요청 보내기

  ```python
  import requests

  response = requests.get('https://jsonplaceholder.typicode.com/todos/')
  print(response)
  ```

- json()로 JSON→배열/딕셔너리 변환

  ```python
  import requests

  # 응답 데이터만 출력
  response = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
  print(response)
  ```

- 필터링 (completed == True)

  ```python
  import requests

  response = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
  # print(response)

  for res in response:
      if res['completed']:
          print(res)
  ```

- 데이터 전처리\_ 필요 데이터 양식에 맞춰 전처리

  ```python
  import requests

  response = requests.get('https://jsonplaceholder.typicode.com/users').json()
  result = []
  field_names = ['id', 'title']

  for res in response:
  	if res['completed']:
  		temp_item = {}
  		for key in field_names:
  			temp_item[key] = res[key]
  		result.append(temp_item)

  print(result)
  ```

## CSV

comma-separated values (대표적인 사례가 콤마다)

### 02_with_statement.py

- open(filename, mode, encoding): 파일을 열고 **파일 객체를 반환**하는 함수
- with문: 리소스를 자동으로 해제하는 문 (with문 종료 시 리소스 해제)

```python
with open('example.txt', 'r', encoding='UTF-8') as f:
	print(f)
	print(dir(f))
	content = f.read()
	print(content)
```

file → f(객체)로 다루기

### 03_csv_read.py

- `csv` 기본 내장됨
- csv.reader() → Reader 객체 반환 (List of Strings 반환함)

```python
import csv

with open('users.csv', 'r', encoding='UTF-8') as file:
	# csv_reader = csv.DictReader(file)
	csv_reader = csv.reader(file)
	for row in csv_reader:
		print(row)
```

### CSV file write

<aside>
💡

LineFeed, CarriageReturn

윈도우 LFCR \n\r

리눅스 LF(CR는 자동으로 됨)

⇒ 즉 \n\r이면 줄 바꿈 두 번 될 수 있음

</aside>

- open()의 `newline 매개변수` ⇒ ‘’로 설정하기

```python
import csv

with open('data.csv', 'w', newline='', encoding='UTF-8') as file:
	csv_writer = csv.writer(file)
	csv_writer.writerow(['이름', '나이', '직업'])
	csv_writer.writerow(['홍길동', 30, '개발자'])
	csv_writer.writerow(['김철수', 25, '디자이너'])
	csv_writer.writerow(['이영희', 28, '기획자'])
```

```python
import csv

with open('data.csv', 'w', newline='', encoding='UTF-8') as file:
	fieldnames = ['이름', '나이', '직업']
	csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

	csv_writer.writeheader()
	csv_writer.writerow({'이름': '홍길동', '나이': 30, '직업': '개발자'})
  csv_writer.writerow({'이름': '김철수', '나이': 25, '직업': '디자이너'})
  csv_writer.writerow({'이름': '이영희', '나이': 28, '직업': '기획자'})
```

```python
import csv

with open('data.csv', 'w', newline='', encoding='UTF-8') as file:
	fieldnames = ['이름', '나이', '직업']
	rows = [
        {'이름': '홍길동', '나이': 30, '직업': '개발자'},
        {'이름': '김철수', '나이': 25, '직업': '디자이너'},
        {'이름': '이영희', '나이': 28, '직업': '기획자'},
  ]
	csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

	csv_writer.writeheader()
	csv_writer.writerows(rows)
```

- writeheader() - csv 파일의 첫 번째 행에 헤더 작성

(이후 csv를 데이터베이스?에 쉽게 삽입)
