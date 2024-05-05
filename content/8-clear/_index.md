---
title : "Clear Resources "
date : "`r Sys.Date()`"
weight : 8
chapter : false
pre : " <b> 8. </b> "
---
1. At Cloudfront
- Choose this cloudfront has just created
- Choose Disable
![](../WorkShop2/08.clear/r1(1).png?featherlight=false&width=50pc)
- Choose Disable
![](../WorkShop2/08.clear/r1(2).png?featherlight=false&width=50pc)
2. At Cognito
- Choose ChatPool
- Choose Delete user pool
![](../WorkShop2/08.clear/r1(3).png?featherlight=false&width=50pc)
- Tick Deactivate deletion protection
- Type: ChatPool
- Choose: Delete
![](../WorkShop2/08.clear/r1(4).png?featherlight=false&width=50pc)
3. At lambda function
- Choose All lambda function
- Choose Delete
![](../WorkShop2/08.clear/r1(5).png?featherlight=false&width=50pc)
- Type: delete
- Choose Delete
![](../WorkShop2/08.clear/r1(6).png?featherlight=false&width=50pc)
4. At API Gateway
- Choose API Action
- Choose delete API
![](../WorkShop2/08.clear/r1(7).png?featherlight=false&width=50pc)
- Type: confirm
- Choose Delete
![](../WorkShop2/08.clear/r1(8).png?featherlight=false&width=50pc)
5. At DynamoDB
- Choose all database
- Choose Delete
![](../WorkShop2/08.clear/r1(9).png?featherlight=false&width=50pc)
- Type confirm
- Choose Delete
![](../WorkShop2/08.clear/r1(10).png?featherlight=false&width=50pc)
6. At DynamoDB
- Choose all database
- Choose Delete
![](../WorkShop2/08.clear/r1(11).png?featherlight=false&width=50pc)
- Type confirm
- Choose Delete
![](../WorkShop2/08.clear/r1(12).png?featherlight=false&width=50pc)
7. At S3
- Choose chat-app-lab bucket
- Choose Empty
![](../WorkShop2/08.clear/r1(13).png?featherlight=false&width=50pc)
- Type: permanently delete
- Choose Empty
![](../WorkShop2/08.clear/r1(14).png?featherlight=false&width=50pc)
8. At S3
- Choose chat-app-lab bucket
- Choose Delete
![](../WorkShop2/08.clear/r1(15).png?featherlight=false&width=50pc)
- Type: chat-app-lab
- Choose Delete Bucket
![](../WorkShop2/08.clear/r1(16).png?featherlight=false&width=50pc)
9. At IAM Interface
- Choose Roles
- Find: Lambda-Role-ChatApp
![](../WorkShop2/08.clear/r1(17).png?featherlight=false&width=50pc)
- Find: Lambda-Cognito
- Choose Delete
![](../WorkShop2/08.clear/r1(18).png?featherlight=false&width=50pc)
- Type: delete
- Choose Delete
![](../WorkShop2/08.clear/r1(19).png?featherlight=false&width=50pc)
10. At IAM Interface
- Choose Policies
- Find: Chat-S3-Access
![](../WorkShop2/08.clear/r1(22).png?featherlight=false&width=50pc)
- Type: Chat-S3-Access
- Choose Delete
![](../WorkShop2/08.clear/r1(23).png?featherlight=false&width=50pc)
11. At IAM Interface
- Choose Policies
- Find: Lambda-User-Pool-ChatApp
- Choose Delete
![](../WorkShop2/08.clear/r1(24).png?featherlight=false&width=50pc)
- Type: Lambda-User-Pool-ChatApp
- Choose Delete
![](../WorkShop2/08.clear/r1(25).png?featherlight=false&width=50pc)
11. At IAM Interface
- Choose Policies
- Find: Access-DynamoDB-ChatApp
- Choose Delete
![](../WorkShop2/08.clear/r1(26).png?featherlight=false&width=50pc)
- Type: Access-DynamoDB-ChatApp
- Choose Delete
![](../WorkShop2/08.clear/r1(27).png?featherlight=false&width=50pc)
