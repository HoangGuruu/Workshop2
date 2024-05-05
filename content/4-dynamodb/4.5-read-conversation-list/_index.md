---
title : "Read conversation list from DynamoDB"
date :  "`r Sys.Date()`" 
weight : 5
chapter : false
pre : " <b> 4.5 </b> "
---
1. At S3 Bucket
- Choose Upload
- Choose Add files
![](../../WorkShop2/04.dynamodb/4.5.read-conversation-list/131.png?featherlight=false&width=50pc)  
2. Go to v6 folder
- Choose site file and add to upload
![](../../WorkShop2/04.dynamodb/4.5.read-conversation-list/132.png?featherlight=false&width=50pc)  
3. Choose Grant public-read acccess
- Choose I understand     
- Choose Upload
![](../../WorkShop2/04.dynamodb/4.5.read-conversation-list/133.png?featherlight=false&width=50pc)  
  
4. At Lambda function
- Copy this code and paste it
```php
import {DynamoDBClient, paginateQuery, QueryCommand} from '@aws-sdk/client-dynamodb';

const client = new DynamoDBClient({});

export const handler = async function (event) {
    const path = event.pathParameters.proxy;

    try {
        if (path === 'conversations') {
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

            const resultObjs = conversationIds.map((id) => {
                return {
                    id: id,
                    last: lasts[id],
                    participants: parts[id]
                };
            });
            return done(null, resultObjs);
        } else if (path.startsWith('conversations/')) {
            const id = path.substring('conversations/'.length);

            return done(null, await loadMessages(id));
        } else {
            done('No cases hit');
        }
    } catch (e) {
        return done(e);
    }
};

async function loadMessages(id) {
    let messages = [];
    const paginator = paginateQuery({client: client}, {
        TableName: 'Chat-Messages',
        ProjectionExpression: '#T, Sender, Message',
        ExpressionAttributeNames: {'#T': 'Timestamp'},
        KeyConditionExpression: 'ConversationId = :id',
        ExpressionAttributeValues: {':id': {S: id}}
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
    return loadConversationDetail(id, messages);
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

function done(err, res) {
    if (err) {
        console.error(err);
    }
    return {
        statusCode: err ? '400' : '200',
        body: err ? JSON.stringify(err) : JSON.stringify(res),
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    };
}

```
- Choose Deploy
![](../../WorkShop2/04.dynamodb/4.5.read-conversation-list/135.png?featherlight=false&width=50pc)  
5. Choose Test and check results
![](../../WorkShop2/04.dynamodb/4.5.read-conversation-list/136.png?featherlight=false&width=50pc)  
6. Check again with browser
![](../../WorkShop2/04.dynamodb/4.5.read-conversation-list/137.png?featherlight=false&width=50pc)