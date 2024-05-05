---
title : "Lambda functions for reading and writing messages"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 5.2 </b> "
---
1. At Lambda function
- Choose Create function
![](../../WorkShop2/05.break/5.2.lambda/176.png?featherlight=false&width=50pc)
2. At Basic information
- Function name: Chat-Messages-GET
- Runtime: Node.js 18.x
![](../../WorkShop2/05.break/5.2.lambda/177.png?featherlight=false&width=50pc)
- Use an existing role : Lambda-Role-ChatApp
- Choose Create function
![](../../WorkShop2/05.break/5.2.lambda/178.png?featherlight=false&width=50pc)
3. Copy code and paste it
```php
import {DynamoDBClient, paginateQuery} from '@aws-sdk/client-dynamodb';

const client = new DynamoDBClient({});

export const handler = async function (event) {
    let messages = [];
    const paginator = paginateQuery({client: client}, {
        TableName: 'Chat-Messages',
        ProjectionExpression: '#T, Sender, Message',
        ExpressionAttributeNames: {'#T': 'Timestamp'},
        KeyConditionExpression: 'ConversationId = :id',
        ExpressionAttributeValues: {':id': {S: event.id}}
    });

    for await (const page of paginator) {
        for (const message of page.Items) {
            messages.push({
                sender: message.Sender.S,
                time: Number(message.Timestamp.N),
                message: message.Message.S
            });
        }
    }
    return loadConversationDetail(event.id, messages);
}

async function loadConversationDetail(id, messages) {
    const paginator = paginateQuery({client: client}, {
        TableName: 'Chat-Conversations',
        Select: 'ALL_ATTRIBUTES',
        KeyConditionExpression: 'ConversationId = :id',
        ExpressionAttributeValues: {':id': {S: id}}
    });

    let participants = [];

    for await (const page of paginator) {
        for (const item of page.Items) {
            participants.push(item.Username.S);
        }
    }

    return {
        id: id,
        participants: participants,
        last: messages.length > 0 ? messages[messages.length - 1].time : undefined,
        messages: messages
    }
}


```
- Choose Deploy
4. At Lambda function
- Choose Create function
- Function name: Chat-Messages-POÓT
- Runtime: Node.js 18.x
![](../../WorkShop2/05.break/5.2.lambda/180.png?featherlight=false&width=50pc)
- Use an existing role : Lambda-Role-ChatApp
- Choose Create function
![](../../WorkShop2/05.break/5.2.lambda/181.png?featherlight=false&width=50pc)
5. Copy code and paste it
```php
import {DynamoDBClient, PutItemCommand} from '@aws-sdk/client-dynamodb';

const client = new DynamoDBClient({});

export const handler = async function (event) {
    await client.send(new PutItemCommand({
        TableName: 'Chat-Messages',
        Item: {
            ConversationId: {S: event.id},
            Timestamp: {
                N: "" + new Date().getTime()
            },
            Message: {S: event.message},
            Sender: {S: 'Student'}
        }
    }));
};

```
- Choose Deploy

![](../../WorkShop2/05.break/5.2.lambda/183.png?featherlight=false&width=50pc)
6. At API Interface
- Choose /{id}
- Choose Create method
![](../../WorkShop2/05.break/5.2.lambda/184.png?featherlight=false&width=50pc)
7. At Method details
- Method type: GET
- Integration type: Lambda function
![](../../WorkShop2/05.break/5.2.lambda/185.png?featherlight=false&width=50pc)
- Choose lambda function: Chat-Messages-GET
![](../../WorkShop2/05.break/5.2.lambda/186.png?featherlight=false&width=50pc)
- Choose create method
![](../../WorkShop2/05.break/5.2.lambda/187.png?featherlight=false&width=50pc)

8. At API Interface
- Choose /{id}
- Choose Create method
![](../../WorkShop2/05.break/5.2.lambda/188.png?featherlight=false&width=50pc)
9. At Method details
- Method type: POST
- Integration type: Lambda function
![](../../WorkShop2/05.break/5.2.lambda/189.png?featherlight=false&width=50pc)
- Choose lambda function: Chat-Messages-POST
![](../../WorkShop2/05.break/5.2.lambda/190.png?featherlight=false&width=50pc)
- Choose create method
![](../../WorkShop2/05.break/5.2.lambda/191.png?featherlight=false&width=50pc)
10. At API gateway
- Choose Models
- Choose Create models
- Name: Conversation
- Content type: application/json
- Model schema
```php
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "participants": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "last": {
      "type": "number",
      "format": "utc-millisec"
    },
    "messages": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "sender": {
            "type": "string"
          },
          "time": {
            "type": "number",
            "format": "utc-millisec"
          },
          "message": {
            "type": "string"
          }
        }
      }
    }
  }
}
```
![](../../WorkShop2/05.break/5.2.lambda/192.png?featherlight=false&width=50pc)
- Choose Create
![](../../WorkShop2/05.break/5.2.lambda/194.png?featherlight=false&width=50pc)
12. At API gateway
- Choose Models
- Choose Create models
- Name: newMessages
- Content type: application/json

![](../../WorkShop2/05.break/5.2.lambda/195.png?featherlight=false&width=50pc)
- Model schema
```php
{
  "type": "string"
}
```
- Choose Create
![](../../WorkShop2/05.break/5.2.lambda/197.png?featherlight=false&width=50pc)
13. At API resource
- Choose GET in /{id}
- Choose Integration request
- Choose Edit
![](../../WorkShop2/05.break/5.2.lambda/198.png?featherlight=false&width=50pc)
14. Choose Mapping templates
- Choose Add mapping template
![](../../WorkShop2/05.break/5.2.lambda/199.png?featherlight=false&width=50pc)
- Content type: application/json
- Template body
```php
#set($inputRoot = $input.path('$'))
{
    "id": "$input.params('id')"
}
```

![](../../WorkShop2/05.break/5.2.lambda/200.png?featherlight=false&width=50pc)
- Choose Save
![](../../WorkShop2/05.break/5.2.lambda/201.png?featherlight=false&width=50pc)
15. Choose Test at GET in /{id}
![](../../WorkShop2/05.break/5.2.lambda/202.png?featherlight=false&width=50pc)
16. Test
- id: 1
- Choose Test
![](../../WorkShop2/05.break/5.2.lambda/203.png?featherlight=false&width=50pc)
17. Check the results
![](../../WorkShop2/05.break/5.2.lambda/204.png?featherlight=false&width=50pc)
18. At API resource
- Choose GET in /{id}
- Choose Method response
- Choose Edit
![](../../WorkShop2/05.break/5.2.lambda/205.png?featherlight=false&width=50pc)
19. Update Response body
- Content type: application/json
- Model: Conversation
- Choose: Save
![](../../WorkShop2/05.break/5.2.lambda/206.png?featherlight=false&width=50pc)
20. At API resource
- Choose POST in /{id}
- Choose Integration request
- Choose Edit
![](../../WorkShop2/05.break/5.2.lambda/207.png?featherlight=false&width=50pc)
21. Choose Mapping templates
- Choose Add mapping template
![](../../WorkShop2/05.break/5.2.lambda/208.png?featherlight=false&width=50pc)
- Content type: application/json

![](../../WorkShop2/05.break/5.2.lambda/209.png?featherlight=false&width=50pc)
- Template body
```php
#set($inputRoot = $input.path('$'))
{
    "id": "$input.params('id')",
    "message": "$inputRoot"
}
```
![](../../WorkShop2/05.break/5.2.lambda/210.png?featherlight=false&width=50pc)
- Choose Save
![](../../WorkShop2/05.break/5.2.lambda/211.png?featherlight=false&width=50pc)
22. At API resource
- Choose POST in /{id}
- Choose Method request
- Choose Edit
![](../../WorkShop2/05.break/5.2.lambda/212.png?featherlight=false&width=50pc)
23. Update Response body
- Content type: application/json
- Model: newMessage
- Choose: Save
![](../../WorkShop2/05.break/5.2.lambda/213.png?featherlight=false&width=50pc)
24. Choose Test at POST in /{id}
- id: 1
![](../../WorkShop2/05.break/5.2.lambda/214.png?featherlight=false&width=50pc)
- Request body: test message
![](../../WorkShop2/05.break/5.2.lambda/215.png?featherlight=false&width=50pc)
- Choose Test
![](../../WorkShop2/05.break/5.2.lambda/216.png?featherlight=false&width=50pc)
25. Check the results
![](../../WorkShop2/05.break/5.2.lambda/217.png?featherlight=false&width=50pc)
26. At API resource
- Choose POST in /{id}
- Choose Method response
- Choose Create response
![](../../WorkShop2/05.break/5.2.lambda/218.png?featherlight=false&width=50pc)
27. At response details
- HTTP status code: 204
- Choose: Save
![](../../WorkShop2/05.break/5.2.lambda/219.png?featherlight=false&width=50pc)
28. At API resource
- Choose POST in /{id}
- Choose Method response
- Choose Delete Response 200
![](../../WorkShop2/05.break/5.2.lambda/220.png?featherlight=false&width=50pc)
- Choose Delete
![](../../WorkShop2/05.break/5.2.lambda/221.png?featherlight=false&width=50pc)
29. At API resource
- Choose POST in /{id}
- Choose Integration response
- Choose Delete Default - response
![](../../WorkShop2/05.break/5.2.lambda/222.png?featherlight=false&width=50pc)
- Choose Delete
![](../../WorkShop2/05.break/5.2.lambda/223.png?featherlight=false&width=50pc)
30. At API resource
- Choose POST in /{id}
- Choose Integration response
- Choose Create response
![](../../WorkShop2/05.break/5.2.lambda/224.png?featherlight=false&width=50pc)
31. At response details
- Method response status code: 204
- Choose: Create
![](../../WorkShop2/05.break/5.2.lambda/225.png?featherlight=false&width=50pc)
32. Choose Test at POST in /{id}
![](../../WorkShop2/05.break/5.2.lambda/226.png?featherlight=false&width=50pc)
- id: 1
![](../../WorkShop2/05.break/5.2.lambda/227.png?featherlight=false&width=50pc)
- Request body: Test case
![](../../WorkShop2/05.break/5.2.lambda/228.png?featherlight=false&width=50pc)
- Check the new status for POST Method
![](../../WorkShop2/05.break/5.2.lambda/229.png?featherlight=false&width=50pc)
33. Choose /{id}
- Choose Enable CORS
![](../../WorkShop2/05.break/5.2.lambda/230.png?featherlight=false&width=50pc)
34. At CORS interface
- Choose GET
- Choose POST
- Choose Save
![](../../WorkShop2/05.break/5.2.lambda/231.png?featherlight=false&width=50pc)