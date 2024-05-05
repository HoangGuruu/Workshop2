---
title : "Creating a policy for the Lambda function"
date :  "`r Sys.Date()`" 
weight : 1
chapter : false
pre : " <b> 3.1 </b> "
---

1. Access IAM
![](../../WorkShop2/03.api/3.1.policy/33.png?featherlight=false&width=50pc)
2. At the IAM interface
- Choose Policies
- Choose Create policy
![](../../WorkShop2/03.api/3.1.policy/34.png?featherlight=false&width=50pc)
3. At the Policy interface
- Choose service: S3 

![](../../WorkShop2/03.api/3.1.policy/35.png?featherlight=false&width=50pc)
- Choose Actions allowed: GetObject 


![](../../WorkShop2/03.api/3.1.policy/36.png?featherlight=false&width=50pc)
- Choose Resource: Specific
- Add ARNs


![](../../WorkShop2/03.api/3.1.policy/37.png?featherlight=false&width=50pc)
4. At the ARN interface
- Name bucket: chat-app-lab
- Object name: *
- Choose Add ARNs

![](../../WorkShop2/03.api/3.1.policy/38.png?featherlight=false&width=50pc)
5. Name the Policy
- Policy name : S3-Access-ChatApp

![](../../WorkShop2/03.api/3.1.policy/39.png?featherlight=false&width=50pc)
6. Choose Create policy

![](../../WorkShop2/03.api/3.1.policy/40.png?featherlight=false&width=50pc)
7. At the IAM interface
- Choose Roles
- Choose Create role

![](../../WorkShop2/03.api/3.1.policy/41.png?featherlight=false&width=50pc)
8. Choose AWS Service

![](../../WorkShop2/03.api/3.1.policy/42.png?featherlight=false&width=50pc)
9. Choose Lambda service
- Choose Next

![](../../WorkShop2/03.api/3.1.policy/43.png?featherlight=false&width=50pc)
10. At Add permissions
- Find and Choose S3-Access-ChatApp 
![](../../WorkShop2/03.api/3.1.policy/44.png?featherlight=false&width=50pc)
- Find and Choose AWSLambdaBasicExecutionRole 
![](../../WorkShop2/03.api/3.1.policy/45.png?featherlight=false&width=50pc)
- Choose Next
![](../../WorkShop2/03.api/3.1.policy/46.png?featherlight=false&width=50pc)
11. At Name, review and create
- Role name: Lambda-Role 

![](../../WorkShop2/03.api/3.1.policy/47.png?featherlight=false&width=50pc)
- Choose Create role
![](../../WorkShop2/03.api/3.1.policy/48.png?featherlight=false&width=50pc)

