---
title : "List Users in the API"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 6.2 </b> "
---

1. At IAM Interface
- Choose Create policy
![](../../WorkShop2/06.identity/6.2.users-api/287.png?featherlight=false&width=50pc)
2. Choose JSON
- Copy policy and paste it
```php
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": "cognito-idp:ListUsers",
      "Resource": "arn:aws:cognito-idp:<your region>:<account id>:userpool/<user pool id>"
    }
  ]
}
```
![](../../WorkShop2/06.identity/6.2.users-api/288.png?featherlight=false&width=50pc)
3. Policy name: Lambda-User-Pool-ChatApp
![](../../WorkShop2/06.identity/6.2.users-api/289.png?featherlight=false&width=50pc)
4. Choose Create policy
![](../../WorkShop2/06.identity/6.2.users-api/290.png?featherlight=false&width=50pc)
5. At IAM Interface
- Find Role: Lambda-Role-ChatApp
![](../../WorkShop2/06.identity/6.2.users-api/291.png?featherlight=false&width=50pc)
- Choose Add permissions
- Choose Attach policies
![](../../WorkShop2/06.identity/6.2.users-api/292.png?featherlight=false&width=50pc)
- Find policy: Lambda-User-Pool-ChatApp
- Choose: Add permissions
![](../../WorkShop2/06.identity/6.2.users-api/293.png?featherlight=false&width=50pc)
6. At IAM Interface
- Choose Create Role
![](../../WorkShop2/06.identity/6.2.users-api/294.png?featherlight=false&width=50pc)
- Choose Service: Lambda
- Choose Next
![](../../WorkShop2/06.identity/6.2.users-api/295.png?featherlight=false&width=50pc)
- Add permission: Lamda-User-Pool-ChatApp
![](../../WorkShop2/06.identity/6.2.users-api/296.png?featherlight=false&width=50pc)
- Add permission: AWSLambdaBasicExecutionRole
![](../../WorkShop2/06.identity/6.2.users-api/297.png?featherlight=false&width=50pc)
- Role-name: Lambda-Cognito
![](../../WorkShop2/06.identity/6.2.users-api/298.png?featherlight=false&width=50pc)
- Choose Create Role
![](../../WorkShop2/06.identity/6.2.users-api/299.png?featherlight=false&width=50pc)
7. At Lambda function
- Choose Create function
- Function name: Chat-User-GET
- Runtime: Node.js 18.x
![](../../WorkShop2/06.identity/6.2.users-api/300.png?featherlight=false&width=50pc)
8. Using an existing role: Lambda-Cognito
- Create function
![](../../WorkShop2/06.identity/6.2.users-api/301.png?featherlight=false&width=50pc)

9. Copy this code and paste it
```php
import {CognitoIdentityProviderClient, paginateListUsers} from '@aws-sdk/client-cognito-identity-provider';

const cognito = new CognitoIdentityProviderClient({});

export const handler = async function () {
    const paginator = paginateListUsers({client: cognito}, {
        UserPoolId: '<user pool id>',
        AttributesToGet: [],
        Filter: '',
        Limit: 60
    });

    let logins = [];

    for await (const page of paginator) {
        for (const user of page.Users) {
            logins.push(user.Username);
        }
    }

    return logins;
};

```
- Choose Deploy
10. At ChatPool
- Check User pool ID
- Check ARN
![](../../WorkShop2/06.identity/6.2.users-api/303.png?featherlight=false&width=50pc)
11. At API interface
- Choose Models
- Choose create model
- Name: userList
- Content type: application/json
![](../../WorkShop2/06.identity/6.2.users-api/304.png?featherlight=false&width=50pc)
- Model schema
```php
{
  "type":"array",
  "items": {
    "type":"string"
  }
}
```
- Choose Create
![](../../WorkShop2/06.identity/6.2.users-api/305.png?featherlight=false&width=50pc)
12. At API interface
- Choose Create resource
- Resource path: /
- Resource name: users
- Choose Create resource
![](../../WorkShop2/06.identity/6.2.users-api/306.png?featherlight=false&width=50pc)
13. Choose Create Method
- Method: GET
- Lambda function
![](../../WorkShop2/06.identity/6.2.users-api/307.png?featherlight=false&width=50pc)
- Lambda function: Chat-User-GET
- Choose Create method
![](../../WorkShop2/06.identity/6.2.users-api/308.png?featherlight=false&width=50pc)
14. Choose Create Method request
- Choose Edit
![](../../WorkShop2/06.identity/6.2.users-api/309.png?featherlight=false&width=50pc)
15. At Response body
- Content type: application/json
- Model: userList
![](../../WorkShop2/06.identity/6.2.users-api/310.png?featherlight=false&width=50pc)
16. Choose Test 
![](../../WorkShop2/06.identity/6.2.users-api/311.png?featherlight=false&width=50pc)
17. Test
![](../../WorkShop2/06.identity/6.2.users-api/312.png?featherlight=false&width=50pc)
18. Check the results
![](../../WorkShop2/06.identity/6.2.users-api/313.png?featherlight=false&width=50pc)
19. At Users of ChatPool
- Choose Create user
![](../../WorkShop2/06.identity/6.2.users-api/314.png?featherlight=false&width=50pc)
- Username: frank
- Choose Generate password
- Choose Create user
![](../../WorkShop2/06.identity/6.2.users-api/315.png?featherlight=false&width=50pc)
20. Do the same with brian
- Username: frank
- Choose Generate password
- Choose Create user
![](../../WorkShop2/06.identity/6.2.users-api/316.png?featherlight=false&width=50pc)
21. Test again and see the results
![](../../WorkShop2/06.identity/6.2.users-api/317.png?featherlight=false&width=50pc)
22. At API Gateway interface
- Choose Deploy API
- Stages: prod
- Choose Deploy
![](../../WorkShop2/06.identity/6.2.users-api/318.png?featherlight=false&width=50pc)
23. Copy link of prod stage
![](../../WorkShop2/06.identity/6.2.users-api/319.png?featherlight=false&width=50pc)
24. Check with browser
![](../../WorkShop2/06.identity/6.2.users-api/320.png?featherlight=false&width=50pc)