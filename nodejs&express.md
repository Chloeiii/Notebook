
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
