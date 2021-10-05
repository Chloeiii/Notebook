## JavaScript:innocent:

### Table of Contents
- [Concepts](#concepts)
- [DOM](#document-object-model-dom)
- [Array](#array)
- [Arrow Functions](#arrow-functions)
- [EventListener](#eventlistener)
- [Get Elements](#get-elements)

### Concepts

    JS 
    1. It is the brain of a web page
    2. It can control the apperance, communications, interations, etc.
    
    JS variables are
        created when page is loaded
        destroyed when a new page is loaded in the browser

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


### Array
select elements from an array

    var animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];

    console.log(animals.slice(2));
    // expected output: Array ["camel", "duck", "elephant"]

    console.log(animals.slice(2, 4));
    // expected output: Array ["camel", "duck"]

    console.log(animals.slice(1, 5));
    // expected output: Array ["bison", "camel", "duck", "elephant"]


### Arrow Functions
https://codeburst.io/javascript-arrow-functions-for-beginners-926947fc0cdc
- Shorter Syntax
- No binding of *this*
- [Arrow functions in React](https://medium.com/@oleg008/arrow-functions-in-react-f782d11460b4)

### EventListener
    The addEventListener() method attaches an event handler to the specified element.
    The addEventListener() method attaches an event handler to an element without overwriting existing event handlers.

    You can add many event handlers to one element.
    You can add many event handlers of the same type to one element, i.e two "click" events.
    You can add event listeners to any DOM object not only HTML elements. i.e the window object.

    The addEventListener() method makes it easier to control how the event reacts to bubbling.

    When using the addEventListener() method, the JavaScript is separated from the HTML markup, for better readability and allows you to add event listeners even when you do not control the HTML markup.

    You can easily remove an event listener by using the removeEventListener() method.
    
- example

        <!DOCTYPE html>
        <html>
        <body>

        <button id="myBtn">Try it</button>

        <p id="demo"></p>

        <script>
        document.getElementById("myBtn").addEventListener("click", displayDate);

        function displayDate() {
          document.getElementById("demo").innerHTML = Date();
        }
        </script>

        </body>
        </html> 
- add many events to the same element

        element.addEventListener("click", myFunction);
        element.addEventListener("click", mySecondFunction);
- add events of different types of the same element

        element.addEventListener("mouseover", myFunction);
        element.addEventListener("click", mySecondFunction);
        element.addEventListener("mouseout", myThirdFunction);
- add an event handler to the window object

        window.addEventListener("resize", function(){
          document.getElementById("demo").innerHTML = sometext;
        });
- passing parameters

        element.addEventListener("click", function(){ myFunction(p1, p2); });
- [events](https://developer.mozilla.org/en-US/docs/Web/Events)

### Get Elements
- by id

      const elem = document .getElementById("xyz");
- by tag name
        
      The tag_name is "div", "span", "p", etc.  
      const list = document .getElementsByTagName("p");
- by class

      const list = document .getElementsByClassName("abc");
- by name

      <input name="xyz" type="text" size="20">
      const xyz = document .getElementsByName("xyz");
