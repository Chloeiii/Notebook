## Table of Contents:  
- [Programming Languages](#programming-languagesghost)
- [HTTP & HTTPS](#http--httpsnail_care)
- [Client-Side vs Server-Side Programming Languages](#client-side-vs-server-side-programming-languagescat2)
- [Web Servers](#web-serversschool_satchel)
- [Git vs SVN](#git-vs-svn)
- [OOP - Object-Oriented Programming](#oop)


----
### Programming Languages:ghost:
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
### HTTP & HTTPS:nail_care:
HTTP stands for "hypertext transfer protocol", a method of data communication for the Internet. HTTP is an application layer protocol, which means it focus on how information is presented to the user at the computer but doesn't address how data gets from Point A to Point B. Any data transferred with the HTTP protocol can potentially be intercepted and even manipualated by third parties.  

> HTTP: no passoword encryption implemented

HTTPS is an extension of the HTTP protocol that works in conjunction with another protocol, called Secure Sockets Layer (SSL), to transport data safely. Neither HTTP nor HTTPS address how data gets to its destination. By contrast, SSL doesn't have anything to do with the appearance of the data. 
People often use the terms HTTPS and SSL interchangeably, but this isn't accurate. HTTPS is secure because it uses SSL to move data. As SSL involved, it was replaced by TLS, or Transport Layer Security - an even more secure way of encrypting information.

> HTTPS: encrypted password

----
### Client-Side vs Server-Side Programming Languages:cat2:
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
### Git vs SVN 
	SVN is a Centralized Version Control System (CVCS), and Git is a Distributed Version Control System (DVCS).

	A centralized version control system operates on the basic idea that there is one single copy of the project 
	that developers will commit changes to, and where all version of the project are stored.

	A distributed version control system, however, works on the principle that each developer “clones” the 
	project repository to their hard drive. A copy of the project is stored on every developer’s local machine, 
	and changes are either “pushed” up to the online repository, or “pulled” down from the repo to update the 
	version that the developer has on their machine.

----
### OOP

    The four principles of object-oriented programming are:
    {encapsulation, abstraction, inheritance, and polymorphism}
- Encapsulation

      Encapsulation is achieved when each object keeps its state private, inside a class. 
      Other objects don’t have direct access to this state. Instead, they can only 
      call a list of public functions — called methods.
      
      e.g.
      -You can feed the cat. But you can’t directly change how hungry the cat is-
      
      Here the “state” of the cat is the private variables mood, hungry and energy. 
      It also has a private method meow(). It can call it whenever it wants, 
      the other classes can’t tell the cat when to meow.

      What they can do is defined in the public methods sleep(), play() and feed(). 
      Each of them modifies the internal state somehow and may invoke meow(). 
      Thus, the binding between the private state and public methods is made.

- Abstraction

      Applying abstraction means that each object should only expose a high-level mechanism for using it.
      
      e.g.
      You interact with your phone by using only a few buttons. 
      What’s going on under the hood? You don’t have to know — implementation details are hidden. 
      You only need to know a short set of actions.
      
      Implementation changes — for example, a software update — rarely affect the abstraction you use.

- Inheritance

      Objects are often very similar. They share common logic. But they’re not entirely the same.
      So how do we reuse the common logic and extract the unique logic into a separate class? 
      One way to achieve this is inheritance.
      
      e.g.
                  person
                /       \
           Teacher      Student
            /   \
      private   public
      teacher   teacher
      
- Polymorphism

      Say we have a parent class and a few child classes which inherit from it. 
      Sometimes we want to use a collection — for example a list — which contains a mix of all these classes. 
      Or we have a method implemented for the parent class — but we’d like to use it for the children, too.
      This can be solved by using polymorphism.
      
      e.g
      reuse a common interface for calculating surface area and perimeter:
      interface:
        *CalculateSurface()
        *CalculatePerimeter()
        
      Having these three figures inheriting the parent Figure Interface lets you create a list of 
      mixed triangles, circles, and rectangles. And treat them like the same type of object.
        
      If you have a function which operates with a figure by using its parameter, 
      you don’t have to define it three times — once for a triangle, a circle, and a rectangle.

      You can define it once and accept a Figure as an argument. 
      Whether you pass a triangle, circle or a rectangle — as long as they implement CalculateParamter(), 
      their type doesn’t matter.

