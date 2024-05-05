---
title : "Read a conversation from Dynamo DB"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 4.4 </b> "
---
1. At the code of lambda function
- Choose Test
- Choose Configure test event
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/119.png?featherlight=false&width=50pc)
2. At Configure test event interface
- Choose Edit saved event
- Event JSON: 
```php
{
    "pathParameters":{
        "proxy": "conversations/1"
    }
}
```
- Choose Save
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/120.png?featherlight=false&width=50pc) 
3. Choose Test      
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/121.png?featherlight=false&width=50pc)     
4. At S3 Bucket
- Choose Upload  
- Choose Add files
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/122.png?featherlight=false&width=50pc)      
5. Go to v4
- Go to site
- Add file to upload
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/123.png?featherlight=false&width=50pc)   
6. Choose Grant public-read acccess
- Choose I understand     
- Choose Upload
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/124.png?featherlight=false&width=50pc)    
7. Access browser and test again   
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/125.png?featherlight=false&width=50pc)  
8. At API interface
- Choose Test
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/126.png?featherlight=false&width=50pc)       
- Method type: GET
- proxy: conversations
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/127.png?featherlight=false&width=50pc)       
- Choose Test 
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/128.png?featherlight=false&width=50pc)  
- Chech the results     
![](../../WorkShop2/04.dynamodb/4.4.read-conversation/129.png?featherlight=false&width=50pc)