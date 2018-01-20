http://blog.csdn.net/tao_627/article/details/22044583

不能忽略的Nginx做web服务器的favicon.ico图像找不到问题


我们在使用Nginx搭建HTTP的web server的过程中，一般都很顺利，默认的网站根目录一般是/usr/local/nginx/html，我们也可以正常访问到Nginx的欢迎信息，比如使用下面的网址：

http://localhost/

但是发现运行一段时间后，Nginx的error日志中会定期抱怨说，没有找到favicon.ico文件？

发生这种错误的原因一般是Nginx在根目录上找不到这个文件。我们可以在网上下载一个ico文件放在根目录下面就可以了。但是现在的业务场景有些区别：

我使用Nginx作为前台服务器，在80端口接收所有的http请求，对本地能缓存的资源直接提供服务，否则转发到upstream上的其他服务器处理，比如转给fastDFS，或者是ATS等等.



我现在在根目录下存放一个ico文件，如何让Nginx直接去本地拿这个文件，而不转发给其他服务器呢？直接在nginx.conf中增加下面一行就可以了：
[html] view plain copy
# set site favicon  
location /favicon.ico {  
    root html;  
    
