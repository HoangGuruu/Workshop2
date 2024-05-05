---
title : "List Users on the site"
date :  "`r Sys.Date()`" 
weight : 3
chapter : false
pre : " <b> 6.3 </b> "
---

1. At S3 Bucket
- Choose Upload
- Choose Add files
![](../../WorkShop2/06.identity/6.3.users-site/322.png?featherlight=false&width=50pc)
2. Go to Site folder in v10 folder
- Choose All and drop to upload
![](../../WorkShop2/06.identity/6.3.users-site/323.png?featherlight=false&width=50pc)
- Grant piblic-read-access
- Choose I understand the risk
- Choose Upload
![](../../WorkShop2/06.identity/6.3.users-site/324.png?featherlight=false&width=50pc)
3. At Stages of API
- Choose Actions
- Choose Generate SDK
- Platform: Javascript
- Choose Generate SDK
![](../../WorkShop2/06.identity/6.3.users-site/325.png?featherlight=false&width=50pc)
4. At S3 Bucket
- Choose Upload
- Choose Add files
![](../../WorkShop2/06.identity/6.3.users-site/326.png?featherlight=false&width=50pc)
5. Choose sdk file unziped
![](../../WorkShop2/06.identity/6.3.users-site/327.png?featherlight=false&width=50pc)
- Grant piblic-read-access
- Choose I understand the risk
- Choose Upload
![](../../WorkShop2/06.identity/6.3.users-site/328.png?featherlight=false&width=50pc)
6. Choose /users at api gateway
- Choose Enable CORS
![](../../WorkShop2/06.identity/6.3.users-site/329.png?featherlight=false&width=50pc)
- Choose GET
- Choose Save
![](../../WorkShop2/06.identity/6.3.users-site/330.png?featherlight=false&width=50pc)
7. Test with browser again
![](../../WorkShop2/06.identity/6.3.users-site/331.png?featherlight=false&width=50pc)