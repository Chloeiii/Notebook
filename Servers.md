## Table of Contents:  
- [HTTP & HTTPS](#http--httpsnail_care)
- [Web Servers](#web-serversschool_satchel)
- [IP && Domain Same && Port](#ip--domain-name--port-heart)
- [Linux Commands](#linux-commandsart)
- [Proxy vs Reverse Proxy](#proxy-vs-reverse-proxy-alien)

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

----
### Linux Commands:art:
    {

    ls -rtl                                    # 按时间倒叙列出所有目录和文件 ll -rt
    touch file                                 # 创建空白文件
    rm -rf dirname                             # 不提示删除非空目录(-r:递归删除 -f强制)
    dos2unix                                   # windows文本转linux文本
    unix2dos                                   # linux文本转windows文本
    enca filename                              # 查看编码  安装 yum install -y enca
    md5sum                                     # 查看md5值
    ln sourcefile newfile                      # 硬链接
    ln -s sourcefile newfile                   # 符号连接
    readlink -f /data                          # 查看连接真实目录
    cat file | nl |less                        # 查看上下翻页且显示行号  q退出
    head                                       # 查看文件开头内容
    head -c 10m                                # 截取文件中10M内容
    split -C 10M                               # 将文件切割大小为10M -C按行
    tail -f file                               # 查看结尾 监视日志文件
    tail -F file                               # 监视日志并重试, 针对文件被mv的情况可以持续读取
    file                                       # 检查文件类型
    umask                                      # 更改默认权限
    uniq                                       # 删除重复的行
    uniq -c                                    # 重复的行出现次数
    uniq -u                                    # 只显示不重复行
    paste a b                                  # 将两个文件合并用tab键分隔开
    paste -d'+' a b                            # 将两个文件合并指定'+'符号隔开
    paste -s a                                 # 将多行数据合并到一行用tab键隔开
    chattr +i /etc/passwd                      # 不得任意改变文件或目录 -i去掉锁 -R递归
    more                                       # 向下分面器
    locate aaa                                 # 搜索
    wc -l file                                 # 查看行数
    cp filename{,.bak}                         # 快速备份一个文件
    \cp a b                                    # 拷贝不提示 既不使用别名 cp -i
    rev                                        # 将行中的字符逆序排列
    comm -12 2 3                               # 行和行比较匹配
    echo "10.45aa" |cksum                      # 字符串转数字编码，可做校验，也可用于文件校验
    iconv -f gbk -t utf8 source.txt > new.txt  # 转换编码
    xxd /boot/grub/stage1                      # 16进制查看
    hexdump -C /boot/grub/stage1               # 16进制查看
    rename source new file                     # 重命名 可正则
    watch -d -n 1 'df; ls -FlAt /path'         # 实时某个目录下查看最新改动过的文件
    cp -v  /dev/dvd  /rhel4.6.iso9660          # 制作镜像
    diff suzu.c suzu2.c  > sz.patch            # 制作补丁
    patch suzu.c < sz.patch                    # 安装补丁

    sort排序{

        -t                                     # 指定排序时所用的栏位分隔字符
        -n                                     # 依照数值的大小排序
        -r                                     # 以相反的顺序来排序
        -f                                     # 排序时，将小写字母视为大写字母
        -d                                     # 排序时，处理英文字母、数字及空格字符外，忽略其他的字符
        -c                                     # 检查文件是否已经按照顺序排序
        -b                                     # 忽略每行前面开始处的空格字符
        -M                                     # 前面3个字母依照月份的缩写进行排序
        -k                                     # 指定域
        -m                                     # 将几个排序好的文件进行合并
        -T                                     # 指定临时文件目录,默认在/tmp
        -o                                     # 将排序后的结果存入指定的文        

        sort -n                                # 按数字排序
        sort -nr                               # 按数字倒叙
        sort -u                                # 过滤重复行
        sort -m a.txt c.txt                    # 将两个文件内容整合到一起
        sort -n -t' ' -k 2 -k 3 a.txt          # 第二域相同，将从第三域进行升降处理
        sort -n -t':' -k 3r a.txt              # 以:为分割域的第三域进行倒叙排列
        sort -k 1.3 a.txt                      # 从第三个字母起进行排序
        sort -t" " -k 2n -u  a.txt             # 以第二域进行排序，如果遇到重复的，就删除

    }

    find查找{

        # linux文件无创建时间
        # Access 使用时间
        # Modify 内容修改时间
        # Change 状态改变时间(权限、属主)
        # 时间默认以24小时为单位,当前时间到向前24小时为0天,向前48-72小时为2天
        # -and 且 匹配两个条件 参数可以确定时间范围 -mtime +2 -and -mtime -4
        # -or 或 匹配任意一个条件

        find /etc -name "*http*"                                # 按文件名查找
        find . -type f                                          # 查找某一类型文件
        find / -perm                                            # 按照文件权限查找
        find / -user                                            # 按照文件属主查找
        find / -group                                           # 按照文件所属的组来查找文件
        find / -atime -n                                        # 文件使用时间在N天以内
        find / -atime +n                                        # 文件使用时间在N天以前
        find / -mtime +n                                        # 文件内容改变时间在N天以前
        find / -ctime +n                                        # 文件状态改变时间在N天前
        find / -mmin +30                                        # 按分钟查找内容改变
        find / -size +1000000c -print                           # 查找文件长度大于1M字节的文件
        find /etc -name "*passwd*" -exec grep "xuesong" {} \;   # 按名字查找文件传递给-exec后命令
        find . -name 't*' -exec basename {} \;                  # 查找文件名,不取路径
        find . -type f -name "err*" -exec  rename err ERR {} \; # 批量改名(查找err 替换为 ERR {}文件
        find path -name *name1* -or -name *name2*               # 查找任意一个关键字

    }

    vim编辑器{

        gconf-editor           # 配置编辑器
        /etc/vimrc             # 配置文件路径
        vim +24 file           # 打开文件定位到指定行
        vim file1 file2        # 打开多个文件
        vim  -r file           # 恢复上次异常关闭的文件 .file.swp 
        vim -O2 file1 file2    # 垂直分屏
        vim -on file1 file2    # 水平分屏
        Ctrl+ U                # 向前翻页
        Ctrl+ D                # 向后翻页
        Ctrl+ww                # 在窗口间切换
        Ctrl+w +or-or=         # 增减高度
        :sp filename           # 上下分割打开新文件
        :vs filename           # 左右分割打开新文件
        :set nu                # 打开行号
        :set nonu              # 取消行号
        :nohl                  # 取消高亮
        :set paste             # 取消缩进
        :set autoindent        # 设置自动缩进
        :set ff                # 查看文本格式
        :set binary            # 改为unix格式
        :%s/str/newstr/g       # 全部替换
        :200                   # 跳转到200  1 文件头
        G                      # 跳到行尾
        dd                     # 删除当前行 并复制 可直接p粘贴
        11111dd                # 删除11111行，可用来清空文件
        r                      # 替换单个字符
        R                      # 替换多个字符
        u                      # 撤销上次操作
        *                      # 全文匹配当前光标所在字符串
        $                      # 行尾
        0                      # 行首
        X                      # 文档加密
        v =                    # 自动格式化代码
        Ctrl+v                 # 可视模式
        Ctrl+v I ESC           # 多行操作
        Ctrl+v s ESC           # 批量取消注释

    }
    
----
### Proxy vs Reverse Proxy :alien:
![alt text](https://i.stack.imgur.com/0qpxZ.png)
