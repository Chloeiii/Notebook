
## Definition:stuck_out_tongue_closed_eyes:
[**Nodejs**](https://nodejs.org/en/)

	Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine.

[**Express**](https://expressjs.com/) 

	Fast, unopinionated, minimalist web framework for node.
	
[**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) 

	an application program interface (API) that 
	uses HTTP requests to GET, PUT, POST and DELETE data.

----
## Environment Setup Sample
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
## Express File Structure Example
(an application where a user can login, register and leave a comment for everyone to admire)

	project/
	  controllers/
	    comments.js
	    index.js
	    users.js
	  helpers/
	    dates.js
	  middlewares/
	    auth.js
	    users.js
	  models/
	    comment.js
	    user.js
	  public/
	    libs/
	    css/
	    img/
	  views/
	    comments/
	      comment.jade
	    users/
	    index.jade
	  tests/
	    controllers/
	    models/
	      comment.js
	    middlewares/
	    integration/
	    ui/
	  .gitignore
	  app.js
	  package.json
- **controllers/** – defines your app routes and their logic
- **helpers/** – code and functionality to be shared by different parts of the project
- **middlewares/** – Express middlewares which process the incoming requests before handling them down to the routes
- **models/** – represents data, implements business logic and handles storage
- **public/** – contains all static files like images, styles and javascript
- **views/** – provides templates which are rendered and served by your routes
- **tests/** – tests everything which is in the other folders
- **app.js** – initializes the app and glues everything together
- **package.json** – remembers all packages that your app depends on and their versions
