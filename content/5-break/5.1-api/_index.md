---
title : "Create API structure in API Gateway"
date :  "`r Sys.Date()`" 
weight : 1
chapter : false
pre : " <b> 5.1 </b> "
---
1. At API Interface 
- Choose Models 
- Choose Create
- Name: ConversationsList
- Content type: application/json
- Model schema:
```php
echo "code"
```
- Choose Create
![](../../WorkShop2/05.break/5.1.api/149.png?featherlight=false&width=50pc)
2. Choose /{proxy+}
- Choose Delete to create a new complete structure API
![](../../WorkShop2/05.break/5.1.api/150.png?featherlight=false&width=50pc)
- Choose Delete
![](../../WorkShop2/05.break/5.1.api/151.png?featherlight=false&width=50pc)
3. Choose Create resourse
- Resource name: conversation
- Choose Create resource
![](../../WorkShop2/05.break/5.1.api/152.png?featherlight=false&width=50pc)
4. Then create next resource
- Resource path: /conversation/
- Resource name: {id}
- Choose Create resource
![](../../WorkShop2/05.break/5.1.api/153.png?featherlight=false&width=50pc)
5. At Lambda Interface
- Choose Create function
![](../../WorkShop2/05.break/5.1.api/154.png?featherlight=false&width=50pc)
6. At function interface
- Function: Chat-Conversation-GET
- Runtime: Node.js 18.x
![](../../WorkShop2/05.break/5.1.api/155.png?featherlight=false&width=50pc)
- Use an existing role
- Choose : Lambda-Role-ChatApp
- Choose Create fuction
![](../../WorkShop2/05.break/5.1.api/156.png?featherlight=false&width=50pc)
7. Copy code for this function and paste it
```php
echo "code"
```
- Choose Deploy
- Choose configure test event
![](../../WorkShop2/05.break/5.1.api/158.png?featherlight=false&width=50pc)
8. Choose Creat new event
- Event: TestConversation
![](../../WorkShop2/05.break/5.1.api/159.png?featherlight=false&width=50pc)
- Event JSON: `{}`
- Choose Save
![](../../WorkShop2/05.break/5.1.api/160.png?featherlight=false&width=50pc)
9. Choose Test and check results
![](../../WorkShop2/05.break/5.1.api/161.png?featherlight=false&width=50pc)
10. At API interface
- Choose /conversations
- Choose Create method
![](../../WorkShop2/05.break/5.1.api/162.png?featherlight=false&width=50pc)
11. At method interface
- Method type: GET
- Integration type: Lambda function
![](../../WorkShop2/05.break/5.1.api/163.png?featherlight=false&width=50pc)
- Choose Lambda function : Chat-Conversation-GET
![](../../WorkShop2/05.break/5.1.api/164.png?featherlight=false&width=50pc)
- Choose Create method
![](../../WorkShop2/05.break/5.1.api/165.png?featherlight=false&width=50pc)
12. At API interface
- Choose Models
- Choose create model
![](../../WorkShop2/05.break/5.1.api/166.png?featherlight=false&width=50pc)
13. At models interface
- Name: ConversationsList
- Content type: application/json
![](../../WorkShop2/05.break/5.1.api/167.png?featherlight=false&width=50pc)
- Model schema:
```php
echo "code"
```
- Choose Create
![](../../WorkShop2/05.break/5.1.api/168.png?featherlight=false&width=50pc)
14. Choose GET in /conversations
- Choose Method response
![](../../WorkShop2/05.break/5.1.api/169.png?featherlight=false&width=50pc)
- Choose Edit
![](../../WorkShop2/05.break/5.1.api/170.png?featherlight=false&width=50pc)
15. At Edit interface - Response body
- Content type: application/json
- Model: ConversationsList
- Choose Save
![](../../WorkShop2/05.break/5.1.api/171.png?featherlight=false&width=50pc)
16. Choose Test and check results with GET
![](../../WorkShop2/05.break/5.1.api/172.png?featherlight=false&width=50pc)
17. Choose /converation
- Choose Enable CORS
![](../../WorkShop2/05.break/5.1.api/173.png?featherlight=false&width=50pc)
18. Choose GET
- Choose Save
![](../../WorkShop2/05.break/5.1.api/174.png?featherlight=false&width=50pc)