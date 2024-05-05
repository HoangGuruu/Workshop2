---
title : "Create a new conversation"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 6.4 </b> "
---

1. At Lambda fuction
- Choose create function
- Function name: Chat-Conversation-POST
- Runtime: Node.js 18.x or Node.js 20.x
![](../../WorkShop2/06.identity/6.4.new-conversation/333.png?featherlight=false&width=50pc)        
- Use an existing role: Lambda-Role-ChatApp
- Choose Create function
![](../../WorkShop2/06.identity/6.4.new-conversation/334.png?featherlight=false&width=50pc)        
2. Copy code and paste it
```php
import { randomUUID } from 'node:crypto';
import {BatchWriteItemCommand, DynamoDBClient} from '@aws-sdk/client-dynamodb';

const dynamo = new DynamoDBClient({});

export const handler = async function (event) {
    const id = randomUUID();
    const users = event.users;
    users.push(event.cognitoUsername);
    const records = users.map((user) => {
        return {
            PutRequest: {
                Item: {
                    ConversationId: {
                        S: id
                    },
                    Username: {
                        S: user
                    }
                }
            }
        };
    });

    await dynamo.send(new BatchWriteItemCommand({
        RequestItems: {
            'Chat-Conversations': records
        }
    }));

    return id;
};

```
- Choose deploy   
![](../../WorkShop2/06.identity/6.4.new-conversation/336.png?featherlight=false&width=50pc)   
3. At API interface
- Choose Models
- Choose Create model     
![](../../WorkShop2/06.identity/6.4.new-conversation/337.png?featherlight=false&width=50pc)        
4. At model details interface
- Name: ConversationId
- Content type: application/json
![](../../WorkShop2/06.identity/6.4.new-conversation/338.png?featherlight=false&width=50pc)  
- Model schema
```php
{"type": "string"}
```      
- Choose Create
![](../../WorkShop2/06.identity/6.4.new-conversation/339.png?featherlight=false&width=50pc)  
5. At model details interface
- Name: NewConversation
- Content type: application/json      
![](../../WorkShop2/06.identity/6.4.new-conversation/340.png?featherlight=false&width=50pc) 
- Model schema
```php
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```      
- Choose Create       
![](../../WorkShop2/06.identity/6.4.new-conversation/341.png?featherlight=false&width=50pc)   
6. At API gateway
- Choose /conversations
- Choose Create method     
![](../../WorkShop2/06.identity/6.4.new-conversation/342.png?featherlight=false&width=50pc)        
- Choose POST
- Choose Lambda function
![](../../WorkShop2/06.identity/6.4.new-conversation/343.png?featherlight=false&width=50pc)  
- Choose Lambda function : Chat-Conversation-POST
![](../../WorkShop2/06.identity/6.4.new-conversation/344.png?featherlight=false&width=50pc)      
7. Choose POST method in /conversations
- Choose Method request
- Choose Edit  
![](../../WorkShop2/06.identity/6.4.new-conversation/345.png?featherlight=false&width=50pc)      
8. At Request body
- Content type: application/json
- Model: NewConversation
- Choose Save  
![](../../WorkShop2/06.identity/6.4.new-conversation/346.png?featherlight=false&width=50pc)
9. Choose POST method in /conversations
- Choose Method response
- Choose Edit 
![](../../WorkShop2/06.identity/6.4.new-conversation/347.png?featherlight=false&width=50pc)    
10. At Request body
- Content type: application/json
- Model: ConversationId
- Choose Save      
![](../../WorkShop2/06.identity/6.4.new-conversation/348.png?featherlight=false&width=50pc) 
11. Choose POST method in /conversations
- Choose Integration request
- Choose Edit 
![](../../WorkShop2/06.identity/6.4.new-conversation/349.png?featherlight=false&width=50pc)     
- Content type: application/json
- Template body
```php
#set($inputRoot = $input.path('$'))
{
"cognitoUsername": "Student",
"users":
[
#foreach($elem in $inputRoot)
 "$elem"
#if($foreach.hasNext),#end
#end
]
}
```    
- Choose Save  
![](../../WorkShop2/06.identity/6.4.new-conversation/350.png?featherlight=false&width=50pc)   
12. Choose /conversations
- Choose Enable CORS
![](../../WorkShop2/06.identity/6.4.new-conversation/351.png?featherlight=false&width=50pc)  
- Choose GET
- Choose OPTIONS
- Choose POST
- Choose Save      
![](../../WorkShop2/06.identity/6.4.new-conversation/352.png?featherlight=false&width=50pc)        
13. At API Gateway 
- Choose Deploy stage prod again

![](../../WorkShop2/06.identity/6.4.new-conversation/353.png?featherlight=false&width=50pc) 
- And choose generate SDK
- Platform: Javascript
- Choose GenerateSDK
![](../../WorkShop2/06.identity/6.4.new-conversation/354.png?featherlight=false&width=50pc)        
14. At S3 Bucket
- Choose Upload
- Choose Add files
- Choose folder sdk unziped and drop to upload  
![](../../WorkShop2/06.identity/6.4.new-conversation/355.png?featherlight=false&width=50pc)   
- Grant public-read access
- Choose I understand
- Choose Upload
![](../../WorkShop2/06.identity/6.4.new-conversation/356.png?featherlight=false&width=50pc)       
14. At S3 Bucket
- Choose Upload
- Choose Add files  
- Go to v11 folder
- Choose site.js and drop it  
![](../../WorkShop2/06.identity/6.4.new-conversation/357.png?featherlight=false&width=50pc)        
- Grant public-read access
- Choose I understand
- Choose Upload 
![](../../WorkShop2/06.identity/6.4.new-conversation/358.png?featherlight=false&width=50pc)  
15. Test with browser
- Start a new conversation
![](../../WorkShop2/06.identity/6.4.new-conversation/359.png?featherlight=false&width=50pc)     
- Test with new messages    
![](../../WorkShop2/06.identity/6.4.new-conversation/360.png?featherlight=false&width=50pc) 