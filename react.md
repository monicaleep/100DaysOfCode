## React FreeCodeCamp curriculum notes
You can have stateless JSX elements, functional components, class components.
You can pass props to a stateless functional component through `.props`. These are custom HTML attributes support by react to be passed to the component. The below code passes the `date` property which is set to `Date()` from Calendar down into CurrentDate, its child component:

```js
const CurrentDate = (props) => {
  return (
    <div>
      <p>The current date is: {props.date}</p>
    </div>
  );
};
class Calendar extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h3>What date is it?</h3>
        <CurrentDate date={Date()}/>
      </div>
    );
  }
};
```

You can set and then overwrite default props. The below code sets a default shopping cart inventory as 0, but it's overwritten.

```js
const Items = (props) => {
  return <h1>Current Quantity of Items in Cart: {props.quantity}</h1>
}
Items.defaultProps = {
  quantity: 0
}
class ShoppingCart extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return <Items quantity={100}/>
  }
};
```

You can also set property types and if they are required, both are a best practice:

```js
const Items = (props) => {
  return <h1>Current Quantity of Items in Cart: {props.quantity}</h1>
};

Items.propTypes = {quantity : PropTypes.number.isRequired}
Items.defaultProps = {
  quantity: 0
};
class ShoppingCart extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return <Items />
  }
};
```


If a child is a Class component, rather than a stateless functional component, you use the `this` keyword to pass props. Example below where it is passed from parent to child.

``` js

class ReturnTempPassword extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
        <div>
            <p>Your temporary password is: <strong>{this.props.tempPassword}</strong></p>
        </div>
    );
  }
};
class ResetPassword extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
        <div>
          <h2>Reset Password</h2>
          <h3>Weve generated a new temporary password for you. </h3>
          <h3>Please reset this password from your account settings ASAP.</h3>
          <ReturnTempPassword tempPassword={"1234gsdf4"}/>
        </div>
    );
  }
};
```
### State

Stateful components are one of the biggest uses of React. State refers to the data of the application and how it changes with time. You create state by declaring `state` property on a class **constructor**. (Remember props were not in the constructor but rather on the class itself and passed by its parent) The state property must be a JavaScript object.

```js
class StatefulComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'Monica'
    }
  }
  render() {
    return (
      <div>
        <h1>{this.state.name}</h1>
      </div>
    );
  }
};
```
#### Changing/Updating State
You can update and set state using the .setState() method. When using class elements, you need to bind `this` in the constructor so `this` becomes bound to the class methods when the component is initialized.
```js
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      text: "Hello"
    };
    this.handleClick = this.handleClick.bind(this)
  }
  handleClick() {
    this.setState({
      text: "You clicked!"
    });
  }
  render() {
    return (
      <div>
        <button onClick={this.handleClick}>Click Me</button>
        <h1>{this.state.text}</h1>
      </div>
    );
  }
};
```
State updates may be asynchronous, therefore you should not rely on the current value of `this.state` or `this.props` when calculating the next value. Instead, you should pass `setState` a function that allows you to access state and props. Using a function with `setState` ensures you have the most current values of state and props.
```js
this.setState((state, props) => ({
  counter: state.counter + props.increment
}));
```
As a more detailed example, here we toggle the visibility of the h1:
```js
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      visibility: false
    };
    this.toggleVisibility = this.toggleVisibility.bind(this)
  }
    toggleVisibility(){
      this.setState((state)=>({
          visibility : !state.visibility
      }
     ))
    }  
  render() {
    if (this.state.visibility) {
      return (
        <div>
          <button onClick={this.toggleVisibility}>Click Me</button>
          <h1>Now you see me!</h1>
        </div>
      );
    } else {
      return (
        <div>
          <button onClick={this.toggleVisibility}>Click Me</button>
        </div>
      );
    }
  }
};
```
And another more example, where the input is written to the DOM:
```js
class ControlledInput extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this)
  }
  handleChange(event){
    this.setState({
      input: event.target.value
    })
  }
  render() {
    return (
      <div>
        <input value={this.state.input} onChange={this.handleChange}></input>
        <h4>Controlled Input:</h4>
        <p>{this.state.input}</p>
      </div>
    );
  }
};
```
I think the above example will be helpful when I work on the markdown previewer. The input value={this.state.input} is important because it will update the state and not just the browser input.
### Unidirectional Data Flow
State flows down the tree of your application - from parent to child. You can pass a parent's state as a prop to a stateless child component. This can help by keeping one component stateful and the rest stateless, so they only take what they need. It simplifies the app. State management is handled in one part of the code and UI is rendered in another part. In the below example, the MyApp state is passed as the name prop to the child Navbar component:
```js
class MyApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'CamperBot'
    }
  }
  render() {
    return (
       <div>
         <Navbar name={this.state.name} />
       </div>
    );
  }
};
class Navbar extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
    <div>
      <h1>Hello, my name is: {this.props.name} </h1>
    </div>
    );
  }
};

```
Callback functions can also be passed as props.

#### Lifecycle method
React components also have several special methods that activate at specific points in the lifecycle of a component. These are also called lifecycle hooks. Some of the main lifecycle methods are componentDidMount, shouldComponentUpdate, componentDidUpdate... read the docs. If you are going to call an API endpoint with React, usually this call is done in the component `componentDidMount()` Any calls to setState in here will trigger a re-rendering of the component. It is also a good place to attach any event listeners.

#### Styles in React
Styles can be done directly in React code. Either inline styles or as an object. In both cases, you need to use camelCase for properties.
```js
const styles = {
  color: "purple",
  fontSize: 40,
  border: "2px solid purple"
}
class Colorful extends React.Component {
  render() {
    return (
      <div style={styles}>Style Me!</div>
    );
  }
};
```


Here is an example of using the state of a parent component, passing it to child as props, and rendering conditionally based on the state:
```js
class Results extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <h1>
      {
        this.props.fiftyFifty ? "You Win!" : "You Lose!"
      }
      </h1>
    )
  };
};

class GameOfChance extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 1
    }
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    this.setState({
      counter: this.state.counter + 1,
    });
  }
  render() {
    const expression = Math.random() >= 0.5
    return (
      <div>
        <button onClick={this.handleClick}>Play Again</button>
        { /* change code below this line */ }
        <Results fiftyFifty={expression}/>
        { /* change code above this line */ }
        <p>{'Turn: ' + this.state.counter}</p>
      </div>
    );
  }
};
```
