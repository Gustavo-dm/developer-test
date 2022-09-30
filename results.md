## GET /surveys/
### HTTP 200 OK
### Allow: GET, POST, HEAD, OPTIONS
### Content-Type: application/json
### Vary: Accept

--- 

```json
[
    {
        "url": "http://127.0.0.1:8000/surveys/1/",
        "name": "Survey 1",
        "description": "Survey 1 description"
    },
    {
        "url": "http://127.0.0.1:8000/surveys/2/",
        "name": "survey 2",
        "description": "Survey 2 description"
    }
]
```

---

## GET /survey-question/
### HTTP 200 OK
### Allow: GET, POST, HEAD, OPTIONS
### Content-Type: application/json
### Vary: Accept
---
```json
[
    {
        "url": "http://127.0.0.1:8000/survey-question/1/",
        "survey_question_text": "Survey question 1",
        "survey": "http://127.0.0.1:8000/surveys/1/"
    },
    {
        "url": "http://127.0.0.1:8000/survey-question/2/",
        "survey_question_text": "Survey question 2",
        "survey": "http://127.0.0.1:8000/surveys/1/"
    },
    {
        "url": "http://127.0.0.1:8000/survey-question/3/",
        "survey_question_text": "Survey question 2",
        "survey": "http://127.0.0.1:8000/surveys/2/"
    }
]
```


---
## GET /surveys-alternative/
## HTTP 200 OK
## Allow: GET, POST, HEAD, OPTIONS
## Content-Type: application/json
## Vary: Accept

---

```json
[
    {
        "url": "http://127.0.0.1:8000/surveys-alternative/1/",
        "survey_question_alternative_text": "1",
        "survey": "http://127.0.0.1:8000/surveys/1/",
        "survey_question": "http://127.0.0.1:8000/survey-question/1/"
    },
    {
        "url": "http://127.0.0.1:8000/surveys-alternative/2/",
        "survey_question_alternative_text": "2",
        "survey": "http://127.0.0.1:8000/surveys/1/",
        "survey_question": "http://127.0.0.1:8000/survey-question/1/"
    }
]
```

## GET /
### HTTP 200 OK
### Allow: GET, HEAD, OPTIONS
### Content-Type: application/json
### Vary: Accept
---
```json
{
    "surveys": "http://127.0.0.1:8000/surveys/",
    "survey-question": "http://127.0.0.1:8000/survey-question/",
    "surveys-alternative": "http://127.0.0.1:8000/surveys-alternative/",
    "surveys-answers": "http://127.0.0.1:8000/surveys-answers/"
}
```