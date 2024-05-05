---
title : "Code walkthrough of the first Lambda function"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 3.2 </b> "
---

1. At AWS Console
- Choose Lambda
![](../../WorkShop2/03.api/3.2.lambda/50.png?featherlight=false&width=50pc)
2. At the create function interface
- Choose author from scratch
- Function name: Lambda-ChatApp-Proxy 
![](../../WorkShop2/03.api/3.2.lambda/51.png?featherlight=false&width=50pc)
- Choose Runtime: Nodejs 18.x 
- Choose Create function
![](../../WorkShop2/03.api/3.2.lambda/52.png?featherlight=false&width=50pc)
- Use the created role: Lambda-Role-ChatApp
![](../../WorkShop2/03.api/3.2.lambda/53.png?featherlight=false&width=50pc)
3. Enter the code for the function Copy the code and paste it into index.js
```php
echo ("code");

```
- Choose Deploy
![](../../WorkShop2/03.api/3.2.lambda/55.png?featherlight=false&width=50pc)
