---
title : "Update Lambda policy to access DynamoDB tables"
date :  "`r Sys.Date()`" 
weight : 3
chapter : false
pre : " <b> 4.3 </b> "
---
1. At the IAM interface
- At the IAM interface
![](../../WorkShop2/04.dynamodb/4.3.update-policy/109.png?featherlight=false&width=90pc)
2. Complete the policy and copy paste the JSON 

![](../../WorkShop2/04.dynamodb/4.3.update-policy/110.png?featherlight=false&width=90pc)
- Select Next
![](../../WorkShop2/04.dynamodb/4.3.update-policy/111.png?featherlight=false&width=90pc)
3. Click Review and create
Policy name: Access-DynamoDB-ChatApp
![](../../WorkShop2/04.dynamodb/4.3.update-policy/112.png?featherlight=false&width=90pc)
- Select Create policy
![](../../WorkShop2/04.dynamodb/4.3.update-policy/113.png?featherlight=false&width=90pc)
4. Find and choose Role: Lambda-Role-ChatApp
![](../../WorkShop2/04.dynamodb/4.3.update-policy/114.png?featherlight=false&width=90pc)
5. Choose Add permissions
- Choose Attach policies
![](../../WorkShop2/04.dynamodb/4.3.update-policy/115.png?featherlight=false&width=90pc)
6. Tick Policy : Access-DynamoDB-ChatApp
![](../../WorkShop2/04.dynamodb/4.3.update-policy/116.png?featherlight=false&width=90pc)
7. Choose Add Permission
![](../../WorkShop2/04.dynamodb/4.3.update-policy/117.png?featherlight=false&width=90pc)