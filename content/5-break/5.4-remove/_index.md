---
title : "Remove hard-coded user names from Lambda"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 5.4 </b> "
---
1. Go to Chat-Conversation-GET lambda function
- Find: `{S: 'Student'}`
![](../../WorkShop2/05.break/5.4.remove/255.png?featherlight=false&width=50pc)
- Change it: `{S: event.cognitoUsername}`
- Choose Deploy
- Choose configure test
![](../../WorkShop2/05.break/5.4.remove/256.png?featherlight=false&width=50pc)
2. At configure test event
- Edit saved event
- Event JSON
```php
{
    "cognitoUsername": "Student"
}
```
- Choose Save
![](../../WorkShop2/05.break/5.4.remove/257.png?featherlight=false&width=50pc)
3. Check the results
![](../../WorkShop2/05.break/5.4.remove/258.png?featherlight=false&width=50pc)
4. Go to Chat-Conversation-POST lambda function
- Find: `{S: 'Student'}`
![](../../WorkShop2/05.break/5.4.remove/259.png?featherlight=false&width=50pc)
- Change it: `{S: event.cognitoUsername}`
- Choose Deploy
![](../../WorkShop2/05.break/5.4.remove/260.png?featherlight=false&width=50pc)
5. At API gateway
- Choose GET in /conversations
- Choose Integration request
- Choose Edit
![](../../WorkShop2/05.break/5.4.remove/261.png?featherlight=false&width=50pc)
6. Mapping templates
- Content type: application/json
- Template body: 
```php
{
    "cognitoUsername": "Student"
}
```
![](../../WorkShop2/05.break/5.4.remove/262.png?featherlight=false&width=50pc)
- Choose Save
![](../../WorkShop2/05.break/5.4.remove/263.png?featherlight=false&width=50pc)
7. At API gateway
- Choose POST in /{id}
- Choose Integration request
- Choose Edit
![](../../WorkShop2/05.break/5.4.remove/264.png?featherlight=false&width=50pc)
8. Mapping templates
- Content type: application/json
- Template body: 
```php
{
    echo "code"
    "cognitoUsername": "Student"
}
```
![](../../WorkShop2/05.break/5.4.remove/265.png?featherlight=false&width=50pc)
9. At API Interface
- Choose Deploy API
- Stage: prod
- Choose Deploy
![](../../WorkShop2/05.break/5.4.remove/266.png?featherlight=false&width=50pc)
10. At stages
- Choose stage actions
- Choose generate SDK
![](../../WorkShop2/05.break/5.4.remove/267.png?featherlight=false&width=50pc)
- Platform: Javascript
- Choose Generate SDK
![](../../WorkShop2/05.break/5.4.remove/268.png?featherlight=false&width=50pc)
11. At S3 Bucket
- Choose Upload
- Choose Add files
![](../../WorkShop2/05.break/5.4.remove/269.png?featherlight=false&width=50pc)
12. Extract file zip of sdk file
- Choose and drop this folder into ../js/
![](../../WorkShop2/05.break/5.4.remove/270.png?featherlight=false&width=50pc)
- Grant public-read access
- Choose I understand
- Choose Upload
![](../../WorkShop2/05.break/5.4.remove/271.png?featherlight=false&width=50pc)
13. Test again with browser chat-app remove harded-code
![](../../WorkShop2/05.break/5.4.remove/272.png?featherlight=false&width=50pc)