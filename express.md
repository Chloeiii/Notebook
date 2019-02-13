
## Definition:stuck_out_tongue_closed_eyes:
[**Nodejs**](https://nodejs.org/en/)

	Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine.

[**Express**](https://expressjs.com/) 

	Fast, unopinionated, minimalist web framework for node.
	
[**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) 

	an application program interface (API) that 
	uses HTTP requests to GET, PUT, POST and DELETE data.

----
## Environment Setup Sample:kiss:
- [install nodejs](https://nodejs.org/en/)
- Install express framework using NPM

		 $ npm install express --save
- create a basic Express app (create a server.js file)

		var express =  require('express');  
		var app = express(); 
		app.get('/',  function  (req, res)  { 
			res.send('Hello World');  
		})  
		var server = app.listen(8081,  function  ()  {  
			var host = server.address().address 
			var port = server.address().port
	   
			console.log("Example app listening at http://%s:%s", host, port)  
		})
- run it with the following command

		$ node server.js 

- Open http://127.0.0.1:8081/ in any browser to see the result.

----
## Express Project Structure Example:sunny:
[create a skeleton website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/skeleton_website)  
(an application where a user can login, register and leave a comment for everyone to admire)

	project/
		routes/
			index.js
	 	controllers/
			comments.js
			index.js
			users.js
	  	views/
			comments/
				comment.jade
			users/
			index.jade
	 	bin/
			www
	  	public/
			libs/
			css/
			img/
	  	tests/
			controllers/
			models/
				comment.js
			integration/ 
	  	.gitignore
	  	app.js
	  	package.json
		
- **routes/** –import controllers and chain together the functions
- **controllers/** – defines your app routes and their logic
- **views/** – provides templates which are rendered and served by your routes
- **bin/** – define port, create HTTP server, and listen on the port
- **public/** – contains all static files like images, styles and javascript
- **tests/** – tests everything which is in the other folders
- **app.js** – initializes the app and glues everything together, exports app object at the last
- **package.json** – remembers all packages that your app depends on and their versions

![](https://mdn.mozillademos.org/files/14456/MVC%20Express.png)  

----

