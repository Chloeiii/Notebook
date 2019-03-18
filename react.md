## Definition :monkey_face:
[React](https://reactjs.org/)
[React cheetsheet](https://devhints.io/react)
    React (also known as React.js or ReactJS) is a JavaScript library 
    that makes developing interactive user interfaces simple.

----
## [Data visualization in React using React D3](https://blog.logrocket.com/data-visualization-in-react-using-react-d3-c35835af16d0)

- set up react by using create-react-app boilerplate 

      npm install -g create-react-app
- create a new app using the create-react-app template

      create-react-app react-d3
- change directory into the newly created project
      
      cd react-d3
- install d3 via NPM

      npm install d3
- preview the app just created on the default browser, run the code below

      npm start
- navigate to **src/App.js**, and start render our chart...
:fire::fire::fire:
----
## Example I
    ReactDOM.render(
      <h1>Hello, world!</h1>,
      document.getElementById('root')
    );
It displays a heading saying “Hello, world!” on the page.    
## Example II
    class HelloMessage extends React.Component {
      render() {
        return <div>Hello {this.props.name}</div>;
      }
    }

    ReactDOM.render(
      <HelloMessage name="Taylor" />,
      document.getElementById('container')
    );
This example will render "Hello Taylor" into a container on the page.    

## Syntax of Creating React Components
    /**
     * This is how you import stuff.  In this case you're actually 
     * importing two things:  React itself and just the "Component" 
     * part from React.  Importing the "Component" part by itself makes it
     * so that you can do something like:
     *
     * class MyComponent extends Component ...
     * 
     * instead of...
     * 
     * class MyComponent extends React.Component
     * 
     * Also note the comma below
     */
         
import React, {Component} from 'react';

    /**
     * This is a "default" export.  That means when you import 
     * this module you can do so without needing a specific module
     * name or brackets, e.g.
     * 
     * import Header from './header';
     *
     * instead of...
     *
     * import { Header } from './header';
     */
         
export default class Header extends Component {}

    /**
     * This is a named export.  That means you must explicitly
     * import "Header" when importing this module, e.g.
     *
     * import { Header } from './header';
     *
     * instead of...
     * 
     * import Header from './header';
     */
         
export const Header = React.createClass({})

    /**
     * This is another "default" export, only just with a 
     * little more shorthand syntax.  It'd be functionally 
     * equivalent to doing:
     *
     * const MyClass = React.createClass({ ... });
     * export default MyClass;
     */

export default React.createClass({})



## [Fetch Data](https://daveceddia.com/where-fetch-data-componentwillmount-vs-componentdidmount/)
to be clear, the *render* function is never a good place to fetch data – or to do anything that’s asynchronous, that changes state in some way, or that causes side effects. The only thing *render* should do is return some JSX to display, and maybe spend a few lines preparing that data to display.

-  componentDidMount
	
	By the time  `componentDidMount`  is called, the component has been rendered once.

	In practice,  `componentDidMount`  is  **the best place to put calls to fetch data**, for two reasons:

	1.  Using  **did**Mount makes it clear that data won’t be loaded until  _after_  the initial render. This reminds you to set up initial  `state`  properly, so you don’t end up with  [undefined state that causes errors](https://daveceddia.com/watch-out-for-undefined-state).
	    
	2.  If you ever need to render your app on the server (a.k.a. server-side-rendering/SSR with  [Next.js](https://nextjs.org/)  or similar),  `componentWillMount`  will actually be called  _twice_  – once on the server, and again on the client – which is probably not what you want. Putting your API call code in  `componentDidMount`  will ensure that data is only fetched from the  _client_, where it should be.
