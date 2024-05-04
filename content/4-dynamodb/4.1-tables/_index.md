---
title : "Create DynamoDB tables"
date :  "`r Sys.Date()`" 
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

1. At the AWS Console interface
- Choose DynamoDB
![](../../WorkShop2/04.dynamodb/4.1.tables/89.png?featherlight=false&width=90pc)
2. Choose Create table
![](../../WorkShop2/04.dynamodb/4.1.tables/90.png?featherlight=false&width=90pc)
3. At the DynamoDB Table interface
- Table name: Chat-Messages
- Partition key: ConversationId
- Sort key: Timestamp 
![](../../WorkShop2/04.dynamodb/4.1.tables/91.png?featherlight=false&width=90pc)
- Choose Create table
![](../../WorkShop2/04.dynamodb/4.1.tables/92.png?featherlight=false&width=90pc)
4. Choose create table to create the second table
![](../../WorkShop2/04.dynamodb/4.1.tables/93.png?featherlight=false&width=90pc)
5. At the table creation interface
- Table name : Chat-Conversations
- Partition key: ConversationId
- Sort key: Username
![](../../WorkShop2/04.dynamodb/4.1.tables/94.png?featherlight=false&width=90pc)
6. Scroll down and Choose Create global index
![](../../WorkShop2/04.dynamodb/4.1.tables/95.png?featherlight=false&width=90pc)
7. At the GSI interface
- Partition key : User name
- Sort key: ConversationId
- Choose Create index
![](../../WorkShop2/04.dynamodb/4.1.tables/96.png?featherlight=false&width=90pc)
8. Choose Create table
![](../../WorkShop2/04.dynamodb/4.1.tables/97.png?featherlight=false&width=90pc)