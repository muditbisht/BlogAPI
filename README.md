# BlogAPI
***
***
## Authentication
|path | entry | reply (valid entry) | reply (invalid entry)|
|-----|-------|----------------------|-----------------------|
|POST /api/auth/register/   | username=<*string*>unique for each user; password<*string*> | ``` {valid: true, token: <Token>}``` | ```{valid: false,errors: [<errors>]}```|
|POST /api/auth/login/| username=<*string*>unique for each user; password<*string*> | ``` {valid: true, token: <Token>}``` | ```{valid: false,errors: [<errors>]}```| 
|GET  /api/auth/logout/|                  | {'Logged Out':'Success'}|

***
***

##Blog
to access this api you need a token and add that to AUTHORIZATION head
AUTHORIZATION=  Bearer <Token>

|path | entry | reply (valid entry) | reply (invalid entry)|
|-----|-------|----------------------|-----------------------|
|GET /api/blog/|    |  ```[{title:<string>,content:<string>,author:<int>}]```| |
|POST /api/blog/| title=<*string*>;content=<*string*>| ```{valid:true, blog_ID:<int>}```| ```{valid:false, errors:[<errors>]}```
|GET /api/blog/<id> |   | ```{title:<string>,content:<string>,author:<int>}```| ```{"detail":"Not found."}```