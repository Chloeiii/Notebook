## JavaScript:innocent:

### Table of Contents

****
### Document Object Model (DOM)
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
### Array
select elements from an array

    var animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];

    console.log(animals.slice(2));
    // expected output: Array ["camel", "duck", "elephant"]

    console.log(animals.slice(2, 4));
    // expected output: Array ["camel", "duck"]

    console.log(animals.slice(1, 5));
    // expected output: Array ["bison", "camel", "duck", "elephant"]

****
### Arrow Functions
https://codeburst.io/javascript-arrow-functions-for-beginners-926947fc0cdc
- Shorter Syntax
- No binding of *this*
- [Arrow functions in React](https://medium.com/@oleg008/arrow-functions-in-react-f782d11460b4)
