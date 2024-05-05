---
title : "Lambda functions for reading and writing messages"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 5.2 </b> "
---
1. At Lambda function
- Choose Create function
![](../../WorkShop2/05.break/5.2.lambda/176.png?featherlight=false&width=90pc)
2. At Basic information
- Function name: Chat-Messages-GET
- Runtime: Node.js 18.x
![](../../WorkShop2/05.break/5.2.lambda/177.png?featherlight=false&width=90pc)
- Use an existing role : Lambda-Role-ChatApp
- Choose Create function
![](../../WorkShop2/05.break/5.2.lambda/178.png?featherlight=false&width=90pc)
3. Copy code and paste it
```php
echo " code "
```
- Choose Deploy
4. At Lambda function
- Choose Create function
- Function name: Chat-Messages-GET
- Runtime: Node.js 18.x
![](../../WorkShop2/05.break/5.2.lambda/180.png?featherlight=false&width=90pc)
- Use an existing role : Lambda-Role-ChatApp
- Choose Create function
![](../../WorkShop2/05.break/5.2.lambda/181.png?featherlight=false&width=90pc)
5. Copy code and paste it
```php
echo " code "
```
- Choose Deploy

![](../../WorkShop2/05.break/5.2.lambda/183.png?featherlight=false&width=90pc)
6. At API Interface
- Choose /{id}
- Choose Create method
![](../../WorkShop2/05.break/5.2.lambda/184.png?featherlight=false&width=90pc)
7. At Method details
- Method type: GET
- Integration type: Lambda function
![](../../WorkShop2/05.break/5.2.lambda/185.png?featherlight=false&width=90pc)
- Choose lambda function: Chat-Messages-GET
![](../../WorkShop2/05.break/5.2.lambda/186.png?featherlight=false&width=90pc)
- Choose create method
![](../../WorkShop2/05.break/5.2.lambda/187.png?featherlight=false&width=90pc)

8. At API Interface
- Choose /{id}
- Choose Create method
![](../../WorkShop2/05.break/5.2.lambda/188.png?featherlight=false&width=90pc)
9. At Method details
- Method type: POST
- Integration type: Lambda function
![](../../WorkShop2/05.break/5.2.lambda/189.png?featherlight=false&width=90pc)
- Choose lambda function: Chat-Messages-POST
![](../../WorkShop2/05.break/5.2.lambda/190.png?featherlight=false&width=90pc)
- Choose create method
![](../../WorkShop2/05.break/5.2.lambda/191.png?featherlight=false&width=90pc)
10. At API gateway
- Choose Models
- Choose Create models
- Name: Conversation
- Content type: application/json
- Model schema
```php
echo "code"
```
![](../../WorkShop2/05.break/5.2.lambda/192.png?featherlight=false&width=90pc)
- Choose Create
![](../../WorkShop2/05.break/5.2.lambda/194.png?featherlight=false&width=90pc)
12. At API gateway
- Choose Models
- Choose Create models
- Name: newMessages
- Content type: application/json

![](../../WorkShop2/05.break/5.2.lambda/195.png?featherlight=false&width=90pc)
- Model schema
```php
echo "code"
```
- Choose Create
![](../../WorkShop2/05.break/5.2.lambda/197.png?featherlight=false&width=90pc)
13. At API resource
- Choose GET in /{id}
- Choose Integration request
- Choose Edit
![](../../WorkShop2/05.break/5.2.lambda/198.png?featherlight=false&width=90pc)
14. Choose Mapping templates
- Choose Add mapping template
![](../../WorkShop2/05.break/5.2.lambda/199.png?featherlight=false&width=90pc)
- Content type: application/json
- Template body
```php
echo "code"
```

![](../../WorkShop2/05.break/5.2.lambda/200.png?featherlight=false&width=90pc)
- Choose Save
![](../../WorkShop2/05.break/5.2.lambda/201.png?featherlight=false&width=90pc)
15. Choose Test at GET in /{id}
![](../../WorkShop2/05.break/5.2.lambda/202.png?featherlight=false&width=90pc)
16. Test
- id: 1
- Choose Test
![](../../WorkShop2/05.break/5.2.lambda/203.png?featherlight=false&width=90pc)
17. Check the results
![](../../WorkShop2/05.break/5.2.lambda/204.png?featherlight=false&width=90pc)
18. At API resource
- Choose GET in /{id}
- Choose Method response
- Choose Edit
![](../../WorkShop2/05.break/5.2.lambda/205.png?featherlight=false&width=90pc)
19. Update Response body
- Content type: application/json
- Model: Conversation
- Choose: Save
![](../../WorkShop2/05.break/5.2.lambda/206.png?featherlight=false&width=90pc)
20. At API resource
- Choose POST in /{id}
- Choose Integration request
- Choose Edit
![](../../WorkShop2/05.break/5.2.lambda/207.png?featherlight=false&width=90pc)
21. Choose Mapping templates
- Choose Add mapping template
![](../../WorkShop2/05.break/5.2.lambda/208.png?featherlight=false&width=90pc)
- Content type: application/json

![](../../WorkShop2/05.break/5.2.lambda/209.png?featherlight=false&width=90pc)
- Template body
```php
echo "code"
```
![](../../WorkShop2/05.break/5.2.lambda/210.png?featherlight=false&width=90pc)
- Choose Save
![](../../WorkShop2/05.break/5.2.lambda/211.png?featherlight=false&width=90pc)
22. At API resource
- Choose POST in /{id}
- Choose Method request
- Choose Edit
![](../../WorkShop2/05.break/5.2.lambda/212.png?featherlight=false&width=90pc)
23. Update Response body
- Content type: application/json
- Model: newMessage
- Choose: Save
![](../../WorkShop2/05.break/5.2.lambda/213.png?featherlight=false&width=90pc)
24. Choose Test at POST in /{id}
- id: 1
![](../../WorkShop2/05.break/5.2.lambda/214.png?featherlight=false&width=90pc)
- Request body: test message
![](../../WorkShop2/05.break/5.2.lambda/215.png?featherlight=false&width=90pc)
- Choose Test
![](../../WorkShop2/05.break/5.2.lambda/216.png?featherlight=false&width=90pc)
25. Check the results
![](../../WorkShop2/05.break/5.2.lambda/217.png?featherlight=false&width=90pc)
26. At API resource
- Choose POST in /{id}
- Choose Method response
- Choose Create response
![](../../WorkShop2/05.break/5.2.lambda/218.png?featherlight=false&width=90pc)
27. At response details
- HTTP status code: 204
- Choose: Save
![](../../WorkShop2/05.break/5.2.lambda/219.png?featherlight=false&width=90pc)
28. At API resource
- Choose POST in /{id}
- Choose Method response
- Choose Delete Response 200
![](../../WorkShop2/05.break/5.2.lambda/220.png?featherlight=false&width=90pc)
- Choose Delete
![](../../WorkShop2/05.break/5.2.lambda/221.png?featherlight=false&width=90pc)
29. At API resource
- Choose POST in /{id}
- Choose Integration response
- Choose Delete Default - response
![](../../WorkShop2/05.break/5.2.lambda/222.png?featherlight=false&width=90pc)
- Choose Delete
![](../../WorkShop2/05.break/5.2.lambda/223.png?featherlight=false&width=90pc)
30. At API resource
- Choose POST in /{id}
- Choose Integration response
- Choose Create response
![](../../WorkShop2/05.break/5.2.lambda/224.png?featherlight=false&width=90pc)
31. At response details
- Method response status code: 204
- Choose: Create
![](../../WorkShop2/05.break/5.2.lambda/225.png?featherlight=false&width=90pc)
32. Choose Test at POST in /{id}
![](../../WorkShop2/05.break/5.2.lambda/226.png?featherlight=false&width=90pc)
- id: 1
![](../../WorkShop2/05.break/5.2.lambda/227.png?featherlight=false&width=90pc)
- Request body: Test case
![](../../WorkShop2/05.break/5.2.lambda/228.png?featherlight=false&width=90pc)
- Check the new status for POST Method
![](../../WorkShop2/05.break/5.2.lambda/229.png?featherlight=false&width=90pc)
33. Choose /{id}
- Choose Enable CORS
![](../../WorkShop2/05.break/5.2.lambda/230.png?featherlight=false&width=90pc)
34. At CORS interface
- Choose GET
- Choose POST
- Choose Save
![](../../WorkShop2/05.break/5.2.lambda/231.png?featherlight=false&width=90pc)