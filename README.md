# 包租Pro

使用高德地图JavaScript API 实现租房信息的地图展示



#代码说明：

1.首先运行crawl.py爬取数据源，根据需要爬取的不同页面，需要修改代码。

2.在templates文件夹下运行python -m SimpleHTTPServer + 8000。

> 注:这是python自带的微型的HTTP服务程序,实验时使用，省去写服务端代码的麻烦。


3.打开浏览器输入localhost:8000 就进入到下图所示页面

4.加载数据源 .csv文件。
> .csv文件要和html文件在一个目录下,因为SimpleHTTPServer是在此处运行的，否则无法加载数据。
# 效果图1 #
![](https://github.com/hugooood/baozuPro/blob/master/images/1.png)

# 效果图2 #
![](https://github.com/hugooood/baozuPro/blob/master/images/2.png)
