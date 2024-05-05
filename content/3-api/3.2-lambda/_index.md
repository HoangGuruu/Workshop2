---
title : "Code walkthrough of the first Lambda function"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 3.2 </b> "
---

1. At AWS Console
- Choose Lambda
![](../../WorkShop2/03.api/3.2.lambda/50.png?featherlight=false&width=50pc)
2. At the create function interface
- Choose author from scratch
- Function name: Lambda-ChatApp-Proxy 
![](../../WorkShop2/03.api/3.2.lambda/51.png?featherlight=false&width=50pc)
- Choose Runtime: Nodejs 18.x 
- Choose Create function
![](../../WorkShop2/03.api/3.2.lambda/52.png?featherlight=false&width=50pc)
- Use the created role: Lambda-Role-ChatApp
![](../../WorkShop2/03.api/3.2.lambda/53.png?featherlight=false&width=50pc)
3. Enter the code for the function Copy the code and paste it into index.js
```php
import {GetObjectCommand, S3Client} from '@aws-sdk/client-s3';

const client = new S3Client({});

const bucket = '<your bucket name>';

export const handler = async function () {
    try {
        const response = await client.send(new GetObjectCommand({
            Bucket: bucket,
            Key: 'data/conversations.json'
        }));
        return done(null, JSON.parse(await response.Body.transformToString()));
    } catch (e) {
        return done(e);
    }
};

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
![](../../WorkShop2/03.api/3.2.lambda/55.png?featherlight=false&width=50pc)
