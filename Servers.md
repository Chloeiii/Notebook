## Table of Contents:  
- [HTTP & HTTPS](#http--httpsnail_care)
- [Web Servers](#web-serversschool_satchel)
- []()

----
### HTTP & HTTPS:nail_care:
HTTP stands for "hypertext transfer protocol", a method of data communication for the Internet. HTTP is an application layer protocol, which means it focus on how information is presented to the user at the computer but doesn't address how data gets from Point A to Point B. Any data transferred with the HTTP protocol can potentially be intercepted and even manipualated by third parties.  

> HTTP: no passoword encryption implemented

HTTPS is an extension of the HTTP protocol that works in conjunction with another protocol, called Secure Sockets Layer (SSL), to transport data safely. Neither HTTP nor HTTPS address how data gets to its destination. By contrast, SSL doesn't have anything to do with the appearance of the data. 
People often use the terms HTTPS and SSL interchangeably, but this isn't accurate. HTTPS is secure because it uses SSL to move data. As SSL involved, it was replaced by TLS, or Transport Layer Security - an even more secure way of encrypting information.

> HTTPS: encrypted password

----
### Web Servers:school_satchel:
#### IIS 
the most popular web server software for microsoft computers is IIS. if its not already running, follow the instructions below to get things set up.

https://msdn.microsoft.com/en-us/library/ms181052(v=vs.80).aspx

#### SimpleHTTPServer (a Pythonic approach)
1.  navigate into the folder where you plan on saving your  `.html`  files (using terminal/cmd) and execute the following command:
    
        python -m SimpleHTTPServer 1337
    
    if you're using Python 3.x or higher, you'd use
    
        python -m http.server 1337
    
2.  now you should be able to access your own files via  [http://localhost:1337/myfile.html](http://localhost:1337/myfile.html)  in Chrome, Firefox or any other web browser.
    

        <html>
          <body>
            <h1>i'm web serving!</h1>
          </body>
        </html>

#### Node.js web server
Once you have installed Node, let's try building our first web server. Create a file named "app.js", and paste the following code:

	const http = require('http');

	const hostname = '127.0.0.1';
	const port = 3000;

	const server = http.createServer((req, res) => {
	  res.statusCode = 200;
	  res.setHeader('Content-Type', 'text/plain');
	  res.end('Hello World\n');
	});

	server.listen(port, hostname, () => {
	  console.log(`Server running at http://${hostname}:${port}/`);
	});
	
After that, run your web server using node app.js, visit http://localhost:3000, and you will see a message 'Hello World'
#### Other webserver
https://gist.github.com/jgravois/5e73b56fa7756fd00b89

----
### IP && Domain Name && Port :heart:

1.背景介绍  
当我们把项目部署到自己的服务器上以后,一般可以通过两种形式访问项目,一种是ip+端口号,还有一种是域名访问.那么这两种访问项目的方式的区别是什么呢？哪一种更好一些？IP，域名，端口号之间有什么联系呢？  

2.知识剖析  
IP,域名,端口号的基本概念  

（1） IP  
IP,（英语：Internet Protocol Address，又译为网际协议地址），缩写为IP地址（英语：IP Address），是分配给网络上使用IP协议的设备的数字标签。 常见的IP地址分为IPv4与IPv6两大类。目前我们使用的都是IPv4的地址，IPv4地址由32位二进制数组成，常以XXX.XXX.XXX.XXX形式表现。（以上参考于维基百科）通俗点说就是IP地址是用于标识出网络上的每一台主机的编号。有这个编号，网络上的其他主机才能在互联网浩若繁星的主机中定位到唯一的一台主机。  

（2）域名  
域名,（英语：domain name），是由一串用“点”分隔的字符组成的Internet上某一台计算机或计算机组的名称，用于在数据传输时标识计算机的电子方位。域名按域名系统（DNS）的规则流程组成。在DNS中注册的任何名称都是域名。域名用于各种网络环境和应用程序特定的命名和寻址目的。（以上参考于维基百科）域名和IP地址之间有区别也有联系，域名通常会和IP进行绑定，通过访问域名来访问网络上的主机的服务。IP地址通常指的是网络中的主机，而域名则通常表示一个网站，一个域名可以绑定到多个ip上，多个域名也可以绑定到一个ip上。  

（3）端口号  
端口，（英语：port），主要分为物理端口和逻辑端口。我们一般说的都是逻辑端口，用于区分不同的服务。因为网络中一台主机只有一个IP，但是一个主机可以提供多个服务，端口号就用于区分一个主机上的不同服务。一个IP地址的端口通过16bit进行编号，最多可以有65536个端口，标识是从0~65535.（以上参考于维基百科）端口号分为公认端口（0~1023）、注册端口（1024~49151）和动态端口（49152~65535）。我们自己的服务一般都绑定在注册端口上。  

3.常见问题及解决方案  
（1）域名和端口号是怎么对应起来的？  
客户端输入域名,通过DNS将域名解析成为服务器ip,找到代理服务器,因为http协议服务所占用的端口默认为80端口，所以会访问服务器的80端口,然后再通过代理服务器将请求转发到不同的服务器以及端口中

作者：淬火殇  
链接：https://www.jianshu.com/p/806d0514ec7d  
来源：简书  
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。  
