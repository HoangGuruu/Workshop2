---
title : "Optimization Setting up a CloudFront CDN"
date : "`r Sys.Date()`"
weight : 7
chapter : false
pre : " <b> 7. </b> "
---
1. At AWS Console
- Choose Cloudfront
![](../WorkShop2/07.optimization-cdn/435.png?featherlight=false&width=50pc)
2. Choose Create a Cloudfront distribution
![](../WorkShop2/07.optimization-cdn/436.png?featherlight=false&width=50pc)
3. Choose s3 bucket we have just created
- Choose Use website endpoint
![](../WorkShop2/07.optimization-cdn/437.png?featherlight=false&width=50pc)
- Check and leave default
![](../WorkShop2/07.optimization-cdn/438.png?featherlight=false&width=50pc)
- Check and leave default
![](../WorkShop2/07.optimization-cdn/439.png?featherlight=false&width=50pc)
- Default root object: index.html
![](../WorkShop2/07.optimization-cdn/440.png?featherlight=false&width=50pc)
- Choose Create distribution
![](../WorkShop2/07.optimization-cdn/441.png?featherlight=false&width=50pc)
4. Copy distribution domain name
![](../WorkShop2/07.optimization-cdn/442.png?featherlight=false&width=50pc)
5. Wait it deploy success and check with browser
![](../WorkShop2/07.optimization-cdn/443.png?featherlight=false&width=50pc)
6. Check write function of this web
![](../WorkShop2/07.optimization-cdn/444.png?featherlight=false&width=50pc)