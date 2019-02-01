## Table of Contents:  
- [Programming Languages](#programming-languages-ghost)
----
## Programming Languages:ghost:
 **C**  
C is one of the older languages still in use, and is the basis for most of the other languages on this list. C is used to develop low-level programs, and works very closely with the computer's hardware.

 **C++**  
This is the object-oriented version of C, and is the most popular programming language in the world. Programs such as Chrome, Firefox, Photoshop, and many others are all built with C++. It is also a very popular language for creating video games. C++ developers are almost always in very high demand.

 **Java**  
This is an evolution of the C++ language, and is used to due its ease of portability. Almost any system can run a Java Virtual Machine, allowing it to run Java software. It is widely used in video games and business software, and many people recommend it as an essential language.

 **C#**   
C# is a Windows-based language that is part of the .NET framework from Microsoft. It is closely related to Java and C++, and if you learn Java you can quickly transition to C#. This language is especially useful for developers working with Windows or Windows Phone software.

**Objective-C**   
This is another cousin of the C language that is specifically designed for Apple systems. It sees immense popularity in iPhone and iPad apps. It is a great language to learn as a freelancer.

**Python**    
This is an incredibly easy language to learn, one of the easiest. Python specializes in web development.

 **PHP**  
This isn't exactly software development, but PHP is essential if you are interested in getting into web development. There is always lots of work for PHP developers, though it isn't as lucrative as software development.

> Java, Python, C++, Visual Basic .NET and Ruby are the most popular OOP languages today. The Java programming language is designed especially for use in distributed applications on corporate networks and the Internet. Ruby is used in many Web applications
----
## HTTP & HTTPS:nail_care:
HTTP stands for "hypertext transfer protocol", a method of data communication for the Internet. HTTP is an application layer protocol, which means it focus on how information is presented to the user at the computer but doesn't address how data gets from Point A to Point B. Any data transferred with the HTTP protocol can potentially be intercepted and even manipualated by third parties.  

> HTTP: no passoword encryption implemented

HTTPS is an extension of the HTTP protocol that works in conjunction with another protocol, called Secure Sockets Layer (SSL), to transport data safely. Neither HTTP nor HTTPS address how data gets to its destination. By contrast, SSL doesn't have anything to do with the appearance of the data. 
People often use the terms HTTPS and SSL interchangeably, but this isn't accurate. HTTPS is secure because it uses SSL to move data. As SSL involved, it was replaced by TLS, or Transport Layer Security - an even more secure way of encrypting information.

> HTTPS: encrypted password

----
## Client-Side vs Server-Side Programming Languages:cat2:
- Basic Background  
Web development is all about communication and data exchange. This communication takes place via two parties over the HTTP protocol.
- Server  
The Server is responsible for serving the web pages depending on the client/end user requirement. It can be either static or dynamic.
- Client  
A client is a party that requests pages from the server and displays them to the end user. In general a client program is a web browser.

- Example | Working  
  
		We can explain this entire mechanism using the following:

		-   The user opens his web browser (client)
		-   The user starts browsing  
		
		-   The client forwards this request to the server, for accessing their web page.
		-   The server then acknowledges the request and replies back to the client program.  
		      
		    (An access link to that web page)  
		    
		-   The client then receives the page source and renders it.  
		      
		    (Into a viewable/under a stable website)  
		    
		-   Now the user types into search bar
		-   The client then submits data to the server
		-   The server processes the data and replies back with a related search result
		-   The client again renders it back for the user's view
		-   The user gets access to the requested link.

- Server-side | Uses
	-   It processes the user input
	-   Displays the requested pages
	-   Structure web applications
	-   Interaction with servers/storages
	-   Interaction with databases
	-   Querying the database
	-   Encoding of data into HTML
	-   Operations over databases like delete, update.

- Server-side | Languages Example    
	-   PHP
	-   ASP.NET (C# OR Visual Basic)
	-   C++
	-   Java and JSP
	-   Python
	-   Ruby on Rails and so on.

- Client-side | Uses
	-   Makes interactive web pages
	-   Make stuffs work dynamically
	-   Interact with temporary storage
	-   Works as an interface between user and server
	-   Sends requests to the server
	-   Retrieval of data from Server
	-   Interact with local storage
	-   Provides remote access for client server program
- Client-side | Languages Example   
	-   JavaScript
	-   VBScript
	-   HTML (Structure)
	-   CSS (Designing)
	-   AJAX
	-   jQuery etc.
----
## Web Servers:school_satchel:
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
