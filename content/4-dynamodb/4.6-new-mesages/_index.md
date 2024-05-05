---
title : "Write new messages to DynamoDB"
date :  "`r Sys.Date()`" 
weight : 6
chapter : false
pre : " <b> 4.6 </b> "
---
1. At lambda function
- Choose configure test event
- Choose Edit saved event
- Event JSON
```php
{
    "httpMethod": "GET",
    "pathParameters": {
        "proxy": "conversations/1"
    }
}
```
- Choose Save
![](../../WorkShop2/04.dynamodb/4.6.new-messages/139.png?featherlight=false&width=50pc)
2. Choose Test and check results
![](../../WorkShop2/04.dynamodb/4.6.new-messages/140.png?featherlight=false&width=50pc)
3. Change Event JSON
```php
{
    "httpMethod": "POST",
    "body": "This is new message",
    "pathParameters": {
        "proxy": "conversations/1"
    }
}
```
- Choose Save and Test
- Or Invoke
![](../../WorkShop2/04.dynamodb/4.6.new-messages/141.png?featherlight=false&width=50pc)
4. Go to DynamoDB tables and check new item 
![](../../WorkShop2/04.dynamodb/4.6.new-messages/142.png?featherlight=false&width=50pc)
5. Check again with browser
![](../../WorkShop2/04.dynamodb/4.6.new-messages/143.png?featherlight=false&width=50pc)
6. This is new items
![](../../WorkShop2/04.dynamodb/4.6.new-messages/144.png?featherlight=false&width=50pc)
7. At S3 Bucket
- Choose Upload
- Choose Add files
- Go to site folder in v7 folder 
- Add all file to upload
![](../../WorkShop2/04.dynamodb/4.6.new-messages/145.png?featherlight=false&width=50pc)
8. Choose Grant public-read acccess
- Choose I understand     
- Choose Upload
![](../../WorkShop2/04.dynamodb/4.6.new-messages/146.png?featherlight=false&width=50pc)
9. Check with browser
- Type new message
![](../../WorkShop2/04.dynamodb/4.6.new-messages/147.png?featherlight=false&width=50pc)