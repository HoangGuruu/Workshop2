---
title : "Add a Cognito authorizer to the API Gateway"
date :  "`r Sys.Date()`" 
weight : 8
chapter : false
pre : " <b> 6.8 </b> "
---

1. At API Gateway
- Choose Authorizers
- Choose Create an authorizer
![](../../WorkShop2/06.identity/6.8.authorizer/390.png?featherlight=false&width=50pc)
2. At authorizer interface
- Authorizer name: Cognito
- Type: Cognito
- Cognito user pool: ChatPool
- Token source: Authorization
- Choose Create authorizer
![](../../WorkShop2/06.identity/6.8.authorizer/391.png?featherlight=false&width=50pc)
3. Check new authorizer
![](../../WorkShop2/06.identity/6.8.authorizer/392.png?featherlight=false&width=50pc)
4. At API gateway
- Choose GET in /conversations
- Choose Method request
- Choose Edit
![](../../WorkShop2/06.identity/6.8.authorizer/393.png?featherlight=false&width=50pc)
- Authorization: Cognito
![](../../WorkShop2/06.identity/6.8.authorizer/394.png?featherlight=false&width=50pc)
5. At API gateway
- Choose GET in /conversations
- Choose Integration request
- Choose Edit
![](../../WorkShop2/06.identity/6.8.authorizer/395.png?featherlight=false&width=50pc)
- Template body
```php
#set($inputRoot = $input.path('$'))
{
    "cognitoUsername": "$context.authorizer.claims['cognito:username']"
}
```
- Choose Save
![](../../WorkShop2/06.identity/6.8.authorizer/396.png?featherlight=false&width=50pc)
- Choose Save
![](../../WorkShop2/06.identity/6.8.authorizer/397.png?featherlight=false&width=50pc)
6. At API gateway
- Choose POST in /conversations
- Choose Method request
- Choose Edit
![](../../WorkShop2/06.identity/6.8.authorizer/398.png?featherlight=false&width=50pc)
- Authorization: Cognito
![](../../WorkShop2/06.identity/6.8.authorizer/399.png?featherlight=false&width=50pc)
7. At API gateway
- Choose POST in /conversations
- Choose Integration request
- Choose Edit

![](../../WorkShop2/06.identity/6.8.authorizer/400.png?featherlight=false&width=50pc)
- Template body
```php
#set($inputRoot = $input.path('$'))
{
"cognitoUsername": "$context.authorizer.claims['cognito:username']",
"users":
[
#foreach($elem in $inputRoot)
 "$elem"
#if($foreach.hasNext),#end
#end
]
}
```
- Choose Save
![](../../WorkShop2/06.identity/6.8.authorizer/401.png?featherlight=false&width=50pc)
8. At API gateway
- Choose POST in /{id}
- Choose Method request
- Choose Edit
![](../../WorkShop2/06.identity/6.8.authorizer/402.png?featherlight=false&width=50pc)
- Authorization: Cognito
![](../../WorkShop2/06.identity/6.8.authorizer/403.png?featherlight=false&width=50pc)
- Choose Save
![](../../WorkShop2/06.identity/6.8.authorizer/404.png?featherlight=false&width=50pc)
9. At API gateway
- Choose POST in /{id}
- Choose Integration request
- Choose Edit
![](../../WorkShop2/06.identity/6.8.authorizer/405.png?featherlight=false&width=50pc)
- Template body
```php
#set($inputRoot = $input.path('$'))
{
    "cognitoUsername": "$context.authorizer.claims['cognito:username']",
    "id": "$input.params('id')",
    "message": "$inputRoot"
}
```
- Choose Save
![](../../WorkShop2/06.identity/6.8.authorizer/406.png?featherlight=false&width=50pc)
10. At API gateway
- Choose GET in /{id}
- Choose Method request
- Choose Edit
![](../../WorkShop2/06.identity/6.8.authorizer/407.png?featherlight=false&width=50pc)
- Authorization: Cognito
![](../../WorkShop2/06.identity/6.8.authorizer/408.png?featherlight=false&width=50pc)
- Choose Save
![](../../WorkShop2/06.identity/6.8.authorizer/409.png?featherlight=false&width=50pc)
11. At API gateway
- Choose GET in /{id}
- Choose Integration request
- Choose Edit
![](../../WorkShop2/06.identity/6.8.authorizer/410.png?featherlight=false&width=50pc)
- Template body
```php
#set($inputRoot = $input.path('$'))
{
    "cognitoUsername": "$context.authorizer.claims['cognito:username']",
    "id": "$input.params('id')"
}
```

![](../../WorkShop2/06.identity/6.8.authorizer/411.png?featherlight=false&width=50pc)
- Choose Save
![](../../WorkShop2/06.identity/6.8.authorizer/412.png?featherlight=false&width=50pc)
12. At API gateway
- Choose GET in /users
- Choose Method request
- Choose Edit
![](../../WorkShop2/06.identity/6.8.authorizer/414.png?featherlight=false&width=50pc)
- Authorization: Cognito
![](../../WorkShop2/06.identity/6.8.authorizer/415.png?featherlight=false&width=50pc)
- Choose Save
![](../../WorkShop2/06.identity/6.8.authorizer/416.png?featherlight=false&width=50pc)
13. At API gateway
- Choose GET in /users
- Choose Integration request
- Choose Edit
![](../../WorkShop2/06.identity/6.8.authorizer/417.png?featherlight=false&width=50pc)
- Template body
```php
#set($inputRoot = $input.path('$'))
{
    "cognitoUsername": "$context.authorizer.claims['cognito:username']"
}
```
![](../../WorkShop2/06.identity/6.8.authorizer/418.png?featherlight=false&width=50pc)
- Choose Save
![](../../WorkShop2/06.identity/6.8.authorizer/419.png?featherlight=false&width=50pc)