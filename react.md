## Definition :monkey_face:
[React](https://reactjs.org/)

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
