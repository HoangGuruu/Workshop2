---
title : "Create sign up page"
date :  "`r Sys.Date()`" 
weight : 5
chapter : false
pre : " <b> 6.5 </b> "
---

1. At User Pool
- Go to App client and copy ClienID
![](../../WorkShop2/06.identity/6.5.sign-up/362.png?featherlight=false&width=50pc)
2. Change information
```php
var poolData = {
    UserPoolId: 'us-east-1_bzELdEaCl',
    ClientId: 'jruh8009fqtifkckptbr494gp'
};
```
3. Prepare amazon-cognito-identity.js for this project
- Steps
- With available file
![](../../WorkShop2/06.identity/6.5.sign-up/364.png?featherlight=false&width=50pc)
4. At S3 Bucket
- Choose Upload
- Choose Add files
- Choose amazon-cognito-identity.js and drop it to upload

![](../../WorkShop2/06.identity/6.5.sign-up/365.png?featherlight=false&width=50pc)
- Choose all in folder site in v12 and drop it to upload
![](../../WorkShop2/06.identity/6.5.sign-up/366.png?featherlight=false&width=50pc)
- Grant public-read access
- Choose I understand
- Choose Upload
![](../../WorkShop2/06.identity/6.5.sign-up/367.png?featherlight=false&width=50pc)
5. Check with browser
- Access ../signup.html
![](../../WorkShop2/06.identity/6.5.sign-up/368.png?featherlight=false&width=50pc)
6. Type necessary information and Choose sign up
![](../../WorkShop2/06.identity/6.5.sign-up/369.png?featherlight=false&width=50pc)
7. Check email
![](../../WorkShop2/06.identity/6.5.sign-up/370.png?featherlight=false&width=50pc)
8. Check user in Chat-Pool
![](../../WorkShop2/06.identity/6.5.sign-up/371.png?featherlight=false&width=50pc)
9. Choose username has just created
- Choose Actions
- Choose Confirm account
![](../../WorkShop2/06.identity/6.5.sign-up/372.png?featherlight=false&width=50pc)
- Choose Confirm
![](../../WorkShop2/06.identity/6.5.sign-up/373.png?featherlight=false&width=50pc)
10. Check user is confirmed
![](../../WorkShop2/06.identity/6.5.sign-up/374.png?featherlight=false&width=50pc)