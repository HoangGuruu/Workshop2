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
{
  "type": "array",
  "items": {
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
      }
    }
  }
}
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
import {DynamoDBClient, paginateQuery, QueryCommand} from '@aws-sdk/client-dynamodb';

const client = new DynamoDBClient({});

export const handler = async function (event) {
    const paginator = paginateQuery({client: client}, {
        TableName: 'Chat-Conversations',
        IndexName: 'Username-ConversationId-index',
        Select: 'ALL_PROJECTED_ATTRIBUTES',
        KeyConditionExpression: 'Username = :username',
        ExpressionAttributeValues: {':username': {S: 'Student'}}
    });

    let conversationIds = [];
    for await (const page of paginator) {
        for (const item of page.Items) {
            conversationIds.push(item.ConversationId.S);
        }
    }

    let lastsPromise = loadConvosLast(conversationIds);
    let partsPromise = loadConvoParticpants(conversationIds);
    let lasts = await lastsPromise;
    let parts = await partsPromise;

    return conversationIds.map((id) => {
        return {
            id: id,
            last: lasts[id],
            participants: parts[id]
        };
    });
};

async function loadConvosLast(ids) {
    const queryResults = ids.map((id) => client.send(new QueryCommand({
        TableName: 'Chat-Messages',
        ProjectionExpression: 'ConversationId, #T',
        Limit: 1,
        ScanIndexForward: false,
        KeyConditionExpression: 'ConversationId = :id',
        ExpressionAttributeNames: {'#T': 'Timestamp'},
        ExpressionAttributeValues: {':id': {S: id}}
    })));

    let result = new Map;

    for await (const qr of queryResults) {
        if (qr.Items.length === 1) {
            result[qr.Items[0].ConversationId.S] = Number(qr.Items[0].Timestamp.N);
        }
    }

    return result;
}

async function loadConvoParticpants(ids) {
    const queryResults = ids.map(async (id) => {
        const paginator = paginateQuery({client: client}, {
            TableName: 'Chat-Conversations',
            Select: 'ALL_ATTRIBUTES',
            KeyConditionExpression: 'ConversationId = :id',
            ExpressionAttributeValues: {':id': {S: id}}
        });

        let p = [];
        for await (const page of paginator) {
            for (const item of page.Items) {
                p.push(item.Username.S);
            }
        }
        return {
            id: id,
            participants: p
        };
    });

    let result = new Map;

    for await (const qr of queryResults) {
        result[qr.id] = qr.participants;
    }

    return result;
}

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
{
  "type": "array",
  "items": {
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
      }
    }
  }
}
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