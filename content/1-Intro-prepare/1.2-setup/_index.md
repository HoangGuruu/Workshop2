---
title : "Setup the website"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 1.2 </b> "
---

1. Access AWS Console Management
- Locate and choose S3
- Choose Create Bucket
![](../../WorkShop2/01.intro-prepare/1.2.setup/2.png?featherlight=false&width=50pc)
2. In the S3 Interface
- Bucket name: **chat-app-lab**
![](../../WorkShop2/01.intro-prepare/1.2.setup/3.png?featherlight=false&width=50pc)
3. Untick Block all public access
![](../../WorkShop2/01.intro-prepare/1.2.setup/4.png?featherlight=false&width=50pc)
4. Choose ACLs enabled
![](../../WorkShop2/01.intro-prepare/1.2.setup/5.png?featherlight=false&width=50pc)
5. Tick I acknowledge ...
![](../../WorkShop2/01.intro-prepare/1.2.setup/6.png?featherlight=false&width=50pc)
6. Choose Create bucket
![](../../WorkShop2/01.intro-prepare/1.2.setup/7.png?featherlight=false&width=50pc)
7. After creating the bucket
- Choose: **chat-app-lab**
![](../../WorkShop2/01.intro-prepare/1.2.setup/8.png?featherlight=false&width=50pc)
8. Choose Upload
![](../../WorkShop2/01.intro-prepare/1.2.setup/9.png?featherlight=false&width=50pc)
9. Choose Add files
![](../../WorkShop2/01.intro-prepare/1.2.setup/10.png?featherlight=false&width=50pc)
10. With the downloaded folder, go to v1 to copy the original files to S3
- Select all then drag and drop
- Choose Upload
![](../../WorkShop2/01.intro-prepare/1.2.setup/11.png?featherlight=false&width=50pc)
11. Choose all downloaded files
- Choose Actions
- Choose Make public using ACL
![](../../WorkShop2/01.intro-prepare/1.2.setup/12.png?featherlight=false&width=50pc)
12. Choose Make public
![](../../WorkShop2/01.intro-prepare/1.2.setup/13.png?featherlight=false&width=50pc)
13. At the S3 interface
- Choose Properties
![](../../WorkShop2/01.intro-prepare/1.2.setup/14.png?featherlight=false&width=50pc)
14. Scroll down to Static website hosting
- Select Edit
![](../../WorkShop2/01.intro-prepare/1.2.setup/15.png?featherlight=false&width=50pc)
15. At the static website interface
- Select enable for static website hosting
- Hosting type : Host a static website
![](../../WorkShop2/01.intro-prepare/1.2.setup/16.png?featherlight=false&width=50pc)
16. At Index document
- Fill in: index.html
![](../../WorkShop2/01.intro-prepare/1.2.setup/17.png?featherlight=false&width=50pc)
17. Choose save changes
![](../../WorkShop2/01.intro-prepare/1.2.setup/18.png?featherlight=false&width=50pc)
18. Copy the website output link
![](../../WorkShop2/01.intro-prepare/1.2.setup/19.png?featherlight=false&width=50pc)
19. Access the browser with the copied link
![](../../WorkShop2/01.intro-prepare/1.2.setup/20.png?featherlight=false&width=50pc)
