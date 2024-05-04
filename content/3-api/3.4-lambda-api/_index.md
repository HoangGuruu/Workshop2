---
title : "Adding an API Gateway trigger to the function"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 3.4 </b> "
---

1. At the AWS Console interface
Choose API Gateway
![](../../WorkShop2/03.api/3.4.lambda-api/62.png?featherlight=false&width=90pc)
2. Choose Build at REST API
![](../../WorkShop2/03.api/3.4.lambda-api/63.png?featherlight=false&width=90pc)
3. Configure the API
- Name: Chat-API
- Type: Edge-optimized
- Choose Create API
![](../../WorkShop2/03.api/3.4.lambda-api/64.png?featherlight=false&width=90pc)
4. At Chat-API interface
- Choose Create resource
![](../../WorkShop2/03.api/3.4.lambda-api/65.png?featherlight=false&width=90pc)
5. At the resource interface
- Resource name: {proxy+}
- Choose Create resource
![](../../WorkShop2/03.api/3.4.lambda-api/66.png?featherlight=false&width=90pc)
6. Choose ANY under /{proxy+}
- Choose Edit integration
![](../../WorkShop2/03.api/3.4.lambda-api/67.png?featherlight=false&width=90pc)
7. Choose Lambda function 
![](../../WorkShop2/03.api/3.4.lambda-api/68.png?featherlight=false&width=90pc)
- Choose the link of the created lambda function: Lambda-ChatApp-Proxy
![](../../WorkShop2/03.api/3.4.lambda-api/69.png?featherlight=false&width=90pc)
8. Leave the rest as default and 
- Choose Save
![](../../WorkShop2/03.api/3.4.lambda-api/70.png?featherlight=false&width=90pc)
9. Choose Test
![](../../WorkShop2/03.api/3.4.lambda-api/71.png?featherlight=false&width=90pc)
10. Choose method: GET
![](../../WorkShop2/03.api/3.4.lambda-api/72.png?featherlight=false&width=90pc)
11. Test and see the results are returned
![](../../WorkShop2/03.api/3.4.lambda-api/73.png?featherlight=false&width=90pc)
12. Check results
![](../../WorkShop2/03.api/3.4.lambda-api/74.png?featherlight=false&width=90pc)