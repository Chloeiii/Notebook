## IIS :school_satchel:
the most popular web server software for microsoft computers is IIS. if its not already running, follow the instructions below to get things set up.

https://msdn.microsoft.com/en-us/library/ms181052(v=vs.80).aspx

Note Other webserver: https://gist.github.com/jgravois/5e73b56fa7756fd00b89


## SimpleHTTPServer (a Pythonic approach) :mrs_claus:

Python comes preinstalled on Macs (and is installed on Windows with ArcGIS Software) so it's  [SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html)  module is an  **excellent**  choice.

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
