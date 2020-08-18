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

```js

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
          <h3>We've generated a new temporary password for you. </h3>
          <h3>Please reset this password from your account settings ASAP.</h3>
          <ReturnTempPassword tempPassword={'1234gsdf4'}/>
        </div>
    );
  }
};
```
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
