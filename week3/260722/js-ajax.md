# 26.07.22.(수)

> JavaScript, AJAX
> 

참조 자료형.. 

### 객체 (Object)

키로 구분된 데이터 집합을 저장하는 자료형

```jsx
const user = {
	name: 'Alice',
	'key with space': true,
	greeting: function () {
		return 'hello'
	}
}
```

- 구조 및 속성
    
    key, value
    
    - key는 “문자형”만 허용 (e.g. 문자열, 따옴표 없는 단어)
    - value는 모든 자료형 허용
    
    속성  `user.name` `user[’key with space’]` (조회/추가/수정/삭제, in 연산자)
    
- 객체와 함수 - Method
    
    **Method**  객체의 함수 (객체의 기능을 기대함)
    
    - 유용한 객체 메서드:  keys(), values()
    

객체에 대한 다른 속성을 접근하려면? (작업할 때)

- this
    
    **this**  함수나 메서드를 호출한 객체를 가리키는 키워드 (누가 호출했는데?)
    
    **자바의 this, 파이썬의 self와 다르다(동작 방식도)
    
    - 장점
        - 재사용성 (메서드를 여러 객체에서 재사용)
    - 중첩된 함수에서의 문제점과 해결
        
        문제:  일반적 함수 호출을 this가 전역 객체를 가리킴
        
        ```jsx
        const myObj2 = {
        	numbers: [1, 2, 3],
        	myFunc: function () {
        		this.numbers.forEach(function (number) {
        			console.log(this) // window
        		})
        	}
        }
        
        console.log(myObj2.myFunc())
        ```
        
        ⇒ 화살표 함수 사용 (자신만의 this를 가지지 않음)
        
        ```jsx
        const myObj3 = {
        	numbers: [1, 2, 3],
        	myFunc: function () {
        		this.numbers.forEach((number) => {
        			console.log(this) // myObj3
        		})
        	}
        }
        
        console.log(myObj3.myFunc())
        ```
        
    
- 추가 객체 문법 - ES6+ 이후
    
    **구조 분해 할당** (destructuring assignment)
    
    ```jsx
    const userInfo = {
    	firstName: 'Alice',
    	userId: 'alice123',
    	email: 'alice123@gmail.com'
    }
    
    const { firstName } = userInfo
    const { firstName, userId } = userInfo
    const { firstName, userId, email } = userInfo
    ```
    
    - 활용 방법 - 함수의 매개변수
        
        ```jsx
        const person = {
        	name: 'Bob',
        	age: 35,
        	city: 'London',
        }
        
        function printInfo({ name, age, city }) {
        	console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
        }
        
        printInfo(person)
        ```
        
    
- 참고 - JSON
    
    JS 객체 표기법을 JSON에서도 쓴다. (그냥 문자열임 - 변환해야)
    

### 배열 (Array)

“이제는 순서가 있는 collection이 필요하다!” → **배열**

- 얘도 객체의 한 종류!  (키 별로 자료형, length 속성 보유)

```jsx
const names = ['Alice', 'Bella', 'Cathy']
```

- 배열 메서드
    
    서비스로 준 메서드   (push / pop,  unshift / shift)
    
- Array helper method
    - 주요 Array Helper Methods :  `forEach()`,  `map()`
        - forEach  - 반환값 없음
            
            ```jsx
            array.forEach(function (item, index, array) {
            	// do something
            })
            ```
            
        - map  - 적용 후 새 배열 반환
            
            ```jsx
            // map: 새로운 배열도 반환
            const newArr = array.map(function (item, index, array) {
            	// do something
            })
            ```
            
        
    
    **`for..of`  vs  `forEach` 
    
    - break, continue 가능 / 불가능
    - (후자가 for..in이랑 안 헷갈리기 좋음)
    

사용자의 데이터를 저장하고 싶음. (UX 유지하면서)

### 비동기

- 개요:  `동기/비동기`,  `block/non-block`,  `동시성/병렬성`
    
    Synchronous (동기)  프로그램의 실행 흐름이 순차적으로 진행
    
    Asynchronous (비동기)  동시에 다른 작업들을 수행할 수 있는 방식
    
    block - 작업 제어권을 안 넘어줌
    
    non-block - 다음 작업자에게 넘겨줌
    
    |  | 동기 | 비동기 |
    | --- | --- | --- |
    | block | 늘 하던 거 | (일반적인 상황에 잘 없음) |
    | non-block | 내 할 일은 하는데 계속 물어보는거 
    e.g. 파일 다운로드 | 일 → 맡기고
    내 일을 하기 |
    
    동시성 - 한 명한테 동시에 하는 것처럼 보이게 하는 것
    
    병렬성 - 여러명한테 시키는 것
    
- JavaScript와 비동기
    
    JS =  Single Thread 언어
    
    - 그러면 어떻게 비동기 처리하냐? → 환경(Runtime) 제공 - 브라우저나 node.js
    
    브라우저 환경에서의 JS 비동기 처리 관련 요소
    
    ![image.png](https://blog.kakaocdn.net/dna/4efum/btsv8UPz0mc/AAAAAAAAAAAAAAAAAAAAAKJ8NV6dwM4rwigo-XzTWlJHp0_EyLx7YsVixJ1vV3Do/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1785509999&allow_ip=&allow_referer=&signature=1hSJROI%2FSudiUc5hYL3I4h3ZpNg%3D)
    
    1. JavaScript Engine의 Call Stack
    2. Web API (오래 걸리는 작업 처리 - setTimeout, DOM Event, 비동기 요청 )
    3. Task Queue (비동기 처리된 콜백함수 대)
    4. Event Loop (Call Stack과 Task Queue 모니터링, call stack 비어 있으면 task queue에꺼 하나 부여)
    

### AJAX

(Asynchronous JavaScript and XML)

XMLHttpRequest 기술을 이용해 비동기를 구현하기 위한 프로그래밍 방식

- 목적:  전체 페이지가 로드되지 x.  HTML 페이지 일부 DOM만 업데이트!
- XMLHttpRequest란?
    
    서버와 상호작용할 때 사용하는 객체
    
- 기존 기술과의 차이
    - 기존:  html 전체를 전달 (새로고침, 대욕폭 낭비)
    

### Callback과 Promise

순서를 강제로 제어하도록 하고 싶음  (e.g. movie 의 응답이 왔을 때 director를 호출해라.)

> Callback
> 
- 비동기 콜백
    
    ```jsx
    const asyncTask = function (callback) {
    	setTimeout(function () {
    		console.log('비동기 작업 완료')
    		callback()  // 작업 완료 후 콜백 호출
    	}, 2000)  // 1초 후 작업 완료
    }
    
    // 비동기 작업 수행 후 콜백 실행
    asyncTask(function () {
    	console.log('작업 완료 후 콜백 실행')
    })
    ```
    
- 콜백 지옥 (Callback Hell)
    
    ![image.png](https://vietnamlife.info/wp-content/uploads/2023/04/callback-hell.jpg)
    
    어떤 기능의 실행 결과를 받아서 다른 기능 수행..  → 단점
    

> Promise - 가독성 & 유지보수성!
> 

JavaScript에서 비동기 작업의 결과를 나타내는 객체

- 성공에 대한 약속 then()
- 실패에 대한 약속 catch()

![image.png](https://miro.medium.com/v2/resize:fit:1276/0*GLhhuxHI3I0tnvdN)

⇒ 비동기 작업의 “순차적인” 처리 가능

### Axios

위에 다 복잡하니.. Axios 라이브러리를 씁니다

- Axios:  서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구
    
    (XHR 객체 생성 및 요청 → 응답 데이터 생성 → JSON 데이터 응답 → Promise로 DOM 조)
    
    - 즉, AJAX 사용!!

<aside>
💡

정리

1. “사용자 경험”을 위해 AJAX 사용
2. 구현을 위해 Axios 라이브러리 활용
</aside>