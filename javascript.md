## IIS :school_satchel:
the most popular web server software for microsoft computers is IIS. if its not already running, follow the instructions below to get things set up.

https://msdn.microsoft.com/en-us/library/ms181052(v=vs.80).aspx

Note Other webserver: https://gist.github.com/jgravois/5e73b56fa7756fd00b89

****
## Document Object Model (DOM) :smirk:
When a HTML page is loaded by a browser, it is converted to a hierarchical structure. Every tag in HTML is converted to an element / object in the DOM with a parent-child hierarchy. It makes our HTML more logically structured. Once the DOM is formed, it becomes easier to manipulate (add/modify/remove) the elements on the page.

Let us understand the DOM using the following HTML document −

    <!DOCTYPE html>
    <html lang = "en">
       <head>
          <title>My Document</title>
       </head>

       <body>
          <div>
             <h1>Greeting</h1>
             <p>Hello World!</p>
          </div>
       </body>
    </html>
    
![dom structure](https://www.tutorialspoint.com/d3js/images/document_object_model.jpg)   

****
## Array
select elements from an array

    var animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];

    console.log(animals.slice(2));
    // expected output: Array ["camel", "duck", "elephant"]

    console.log(animals.slice(2, 4));
    // expected output: Array ["camel", "duck"]

    console.log(animals.slice(1, 5));
    // expected output: Array ["bison", "camel", "duck", "elephant"]
