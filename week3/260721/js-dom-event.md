# 26.07.21.(화) - JavaScript_DOM_Event

> JavaScript, DOM, 함수, 이벤트
> 

### JavaScript

JavaScript 역사

- ECMAScript
    - ECMAScript는 명세  (js언어가 이거 따라 구현됨)
    - ES6이 중요 버전

JavaScript 문법 (변수, 연산자, 제어문)

- 변수
    
    식별자(변수명) Naming case
    
    <aside>
    💡
    
    camelCase  변수, 객체, 함수에 사용
    
    PascalCase  클래스, 생성자에 사용
    
    SNAKE_CASE  상수(constants)에 사용
    
    </aside>
    
    변수 선언 키워드 2가지
    
    1. let (먼저 선점하면 재선언 불가)
    2. **const** (재할당도 불가)
    
    블록 스코프:  ‘중괄호({}) 내부’
    
    **for/if문 등의 괄호()도 포함됨
    
- 데이터 타입
    
    <aside>
    💡
    
    | **원시 자료형 (Primitive type)** | **참조 자료형 (Reference type)** |
    | --- | --- |
    | Number, String, Boolean, null, undefined | **Objects** (Object, Array, Function) |
    | 불변, 값이 복사 | 가변, 주소가 복사 |
    - 가변성이란?
        
        e.g. 객체(obj)의 주소는 그대로지만, 내부 속성(obj.title)은 변경 가능
        
    </aside>
    
    > 원시 자료형
    > 
    
    **Number** (Infinity, NaN)
    
    **String** (Template Literals - ``${expression}`` )
    
    **null**  vs  **undefined** (의도적 표현  vs  의도 안 된 거)
    
    **Boolean** (Boolean 아닌거 “자동 형변환 규칙” 적용됨)
    
    - 주의:  typeof null → “object”
    
    > 참조 자료형
    > 
    
    내일 자세히..
    
- 연산자
    - 동등 연산자(==)  ‘암묵적 타입 변환’으로 타입 맞춘 후 값 비교
    - 일치 연산자(===)  타입까지 비교
- 제어문 (반복문 - `for…in`, `for…of`)
    - `for…in`:  object 순회
    - `for…of`:  iterable(반복 가능한 객체) 순회

### DOM

“그래서 html 조작.. 어케 할건데?”

- DOM 개요
    
    **DOM** (The Document Object Model)  웹 페이지를 구조화된 객체로 제공 (tree)
    
    - 최상위:  `document` 객체
    
    **DOM API**  다른 프로그래밍 언어가 접근/조작하는 방법 제공
    

> 조작 순서
> 
> 1. 대상(요소) 선택
> 2. 조작
- DOM 선택 (선택 메서드)
    
    >> ㅇㅇ CSS에서 선택자 맞음
    
    | document.querySelector(`selector`) | 요소 한 개 선택 |
    | --- | --- |
    | document.querySelectorAll(`selector`) | 요소 여러 개 선택 |
    
- DOM 조작
    - 속성(attribute) 조작  - 요소의 속성
        - 클래스 속성 조작 → `클래스를 줬다 뺐다` (none 부여 말고)
            
            ```jsx
            elem.classList.add()
            elem.classList.remove()
            elem.classList.toggle()
            ```
            
        - 일반 속성 조작 → `하드코딩하지 말자`
            
            ```jsx
            elem.getAttribute()
            elem.setAttribute(name, value)
            elem.removeAttribute()
            ```
            
        
    - HTML 콘텐츠 조작  - 요소의 텍스트 콘텐츠
        
        ```jsx
        elem.textContent = '내용 수정'
        ```
        
    - DOM 요소 조작
        
        ```jsx
        document.createElement(tagName)
        Node.appendChild()
        Node.removeChild()
        ```
        
    

### 함수

참조형 자료형(Object) 분류 중 하나 

- 함수
    - 표현 방법 2가지 (선언식, 표현식)
        
          → 선언식보다 **표현식** 사용함  (’익명 함수’ 사용,  호이스팅 방지)
        
        선언식 (function declaration)
        
        ```jsx
        function add (num1, num2) {
        	return num1 + num2
        }
        ```
        
        표현식 (function expression)
        
        ```jsx
        const sub = function (num1, num2) {
        	return num1 - num2
        }
        ```
        
        **표현식 = 평가에 따라 하나의 값으로 나오는 것 (e.g. 1+1)
        
        **호이스팅 = 실행 단계에서 함수 정의문 당겨지는 것 
        
    - 화살표 함수
        
        :  표현식을 간단히하기.  ((동작 방식이 달라져서 쓴다~~)
        
        ```jsx
        const arrow = function (name) {
        	return `hello, ${name}`
        }
        ```
        
        ```jsx
        const arrow = name => `hello, ${name}`
        ```
        
        - 리턴만 있을 때
        - `function` 키워드 빼고 `⇒`
        

### 이벤트

웹에서 모든 동작은 이벤트다.
다룰려면 event 객체가 필요하다. (마우스가 클릭이 된걸까? 좌표? 클릭 속도?)

→ ‘처리’할 수 있다. (`event handler`)   (사용자의 행동에 어떻게 반응할까?)

```jsx
Element.addEventListener(type, handler)
```

- type: click
- handler:  콜백함수 (그 때 실행할 거리)

### 버블링

(div에 여러 버튼 넣고, div에 핸들러 줘버리기 - 그래서 여러 요소를 하나의 이벤트 리스너로 가능)

:  한 요소에 이벤트가 발생하면, 가장 최상단의 조상 요소(document)를 만날 때 까지 요소에 각각 할당된 핸들러가 동작

- 어디 선택됐는지는 어떻게 아는데? → `currentTarget`, `target`