---
title : "Exporting a JavaScript client and Swagger"
date :  "`r Sys.Date()`" 
weight : 3
chapter : false
pre : " <b> 5.3 </b> "
---

1. At API Interface
- Choose Deploy API
![](../../WorkShop2/05.break/5.3.export/233.png?featherlight=false&width=50pc)
- Stage: prod
- Choose Deploy
![](../../WorkShop2/05.break/5.3.export/234.png?featherlight=false&width=50pc)
2. At stages
- Choose stage actions
- Choose generate SDK
![](../../WorkShop2/05.break/5.3.export/235.png?featherlight=false&width=50pc)
- Platform: Javascript
- Choose Generate SDK
![](../../WorkShop2/05.break/5.3.export/236.png?featherlight=false&width=50pc)
3. At S3 Bucket
- Choose Upload
- Choose Add files
![](../../WorkShop2/05.break/5.3.export/237.png?featherlight=false&width=50pc)
4. Extract file zip of sdk file
- Choose and drop this folder into ../js/
![](../../WorkShop2/05.break/5.3.export/238.png?featherlight=false&width=50pc)
- Grant public-read access
- Choose I understand
- Choose Upload
![](../../WorkShop2/05.break/5.3.export/239.png?featherlight=false&width=50pc)
5. At S3 Bucket
- Choose Upload
- Choose Add files
![](../../WorkShop2/05.break/5.3.export/240.png?featherlight=false&width=50pc)
6. Go to Site folder in folder v9
- Choose all and drop to upload
![](../../WorkShop2/05.break/5.3.export/242.png?featherlight=false&width=50pc)
- Grant public-read access
- Choose I understand
- Choose Upload
![](../../WorkShop2/05.break/5.3.export/243.png?featherlight=false&width=50pc)
7. Test with browser
- Send new messages

![](../../WorkShop2/05.break/5.3.export/244.png?featherlight=false&width=50pc)

- Test wit 2nd conversation
![](../../WorkShop2/05.break/5.3.export/245.png?featherlight=false&width=50pc)

8. At Stages of API
- Choose stage actions
- Choose export
![](../../WorkShop2/05.break/5.3.export/246.png?featherlight=false&width=50pc)

- Choose Swagger
- Choose YAML
- Choose Export API

![](../../WorkShop2/05.break/5.3.export/247.png?featherlight=false&width=50pc)

- A file yaml will be downloaded
![](../../WorkShop2/05.break/5.3.export/248.png?featherlight=false&width=50pc)
9. Go to google and search Swagger Editor

![](../../WorkShop2/05.break/5.3.export/249.png?featherlight=false&width=50pc)
- Access this website

![](../../WorkShop2/05.break/5.3.export/250.png?featherlight=false&width=50pc)
10. Copy code in file into Editor
- Can see Any methods of this API
![](../../WorkShop2/05.break/5.3.export/251.png?featherlight=false&width=50pc)
11. Choose Try it out to test API
![](../../WorkShop2/05.break/5.3.export/252.png?featherlight=false&width=50pc)
12. See the results
![](../../WorkShop2/05.break/5.3.export/253.png?featherlight=false&width=50pc)