When using React with Redux, a single redux store will manage the state of the application. The React components will subscribe to only the pieces of data in the store that affects them. You dispatch actions from the redux store which then trigger store updates.

To add redux into an app first we handle state locally:
```js
class DisplayMessages extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      messages: []
    }
   this.handleChange = this.handleChange.bind(this);
  this.submitMessage = this.submitMessage.bind(this);
  }
  handleChange(event){
    this.setState({
      input: event.target.value,
      messages: this.state.messages
    })
  }
  submitMessage(){
    this.setState({
      messages: this.state.messages.concat([this.state.input]),
      input: ""
    });

  }

  render() {
    return (
      <div>
        <h2>Type in a new Message:</h2>
        <input value={this.state.input} onChange={this.handleChange}></input>
        <button onClick={this.submitMessage}>Submit</button>
        <ul>
        {this.state.messages.map((x,i)=>{
          return <li key={i}>{x}</li>
        })}
        </ul>
      </div>
    );
  }
};
```

Then we can start to pull away the state management into redux
```js
const ADD = 'ADD';

const addMessage = (message) => {
  return {
    type: ADD,
    message: message
  }
}

const messageReducer = (state = [], action) => {
  if(action.type === ADD){
    return [...state, action.message]
  } else {
    return state
  }
}

const store = Redux.createStore(messageReducer)
```

OK! Now we have both setup, we use the `react-redux` package from npm to connect them. There's two key features: Provider and connector. The Provider is a wrapper component that wraps your React app. This wrapper then allows you to access the Redux `store` and `dispatch` functions throughout your component tree. Provider takes 2 props, the redux store and the child components of your app.
```js
const Provider = ReactRedux.Provider;

class AppWrapper extends React.Component {
  render(){
    return (<Provider store={store}>
   <DisplayMessages/>
  </Provider>
    )
  }
};
```

The Provider component allows you to *provide* state and dispatch to your react components, but you need to specific which state and actions you want. To do this by creating two function `mapStateToProps()` and `mapDispatchToProps()`. In these functions you say which parts of state you want to have access to and which action creators you need to dispatch.

`mapStateToProps` takes state as an argument and returns an object which maps that state to specific property names. Then these properties will be accessible to your component via `props`
Similarly, `mapDispatchToProps` takes dispatch as an argument and returns an object that maps dispatch actions to property names, which become component props.
```js
const mapStateToProps = (state) => {
  return {
    messages: state
  }
};

const mapDispatchToProps = (dispatch) => {
  return {
    submitNewMessage: (message) => {
      dispatch(addMessage(message));
    }
  }
};
```


Finally, you connect these functions to your react component using the `connect()` method of the ReactRedux object which takes two optional args, mapStateToProps and mapDispatchToProps. You immediately call the result with your component and assigned it to a component which represents the connected component. Phew!
```js
const connect = ReactRedux.connect;
const ConnectedComponent = connect(mapStateToProps,mapDispatchToProps)(Presentational)
```


Here is our connected 'Messages' after extracting local state into redux and connecting!
```js
// Redux:
const ADD = 'ADD';

const addMessage = (message) => {
  return {
    type: ADD,
    message: message
  }
};

const messageReducer = (state = [], action) => {
  switch (action.type) {
    case ADD:
      return [
        ...state,
        action.message
      ];
    default:
      return state;
  }
};

const store = Redux.createStore(messageReducer);

// React:
const Provider = ReactRedux.Provider;
const connect = ReactRedux.connect;

// Change code below this line
class Presentational extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '' //remove messages from state
    }
    this.handleChange = this.handleChange.bind(this);
    this.submitMessage = this.submitMessage.bind(this);
  }
  handleChange(event) {
    this.setState({
      input: event.target.value  //removed message from state
    });
  }
  submitMessage() {
    this.props.submitNewMessage(this.state.input)  //using the props to dispatch submitNewMessage
    this.setState((state) => ({
      input: ''  //removed message from state
    }));
  }
  render() {
    return (
      <div>
        <h2>Type in a new Message:</h2>
        <input
          value={this.state.input}
          onChange={this.handleChange}/><br/>
        <button onClick={this.submitMessage}>Submit</button>
        <ul>
          {this.props.messages.map( (message, idx) => { //Changed from this.state to now it is props
              return (
                 <li key={idx}>{message}</li>
              )
            })
          }
        </ul>
      </div>
    );
  }
};

const mapStateToProps = (state) => {
  return {messages: state}
};

const mapDispatchToProps = (dispatch) => {
  return {
    submitNewMessage: (message) => {
      dispatch(addMessage(message))
    }
  }
};

const Container = connect(mapStateToProps, mapDispatchToProps)(Presentational);

class AppWrapper extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <Container/>
      </Provider>
    );
  }
};

```


Boilerplate React Redux for future reference:
```
// import React from 'react'
// import ReactDOM from 'react-dom'
// import { Provider, connect } from 'react-redux'
// import { createStore, combineReducers, applyMiddleware } from 'redux'
// import thunk from 'redux-thunk'

// import rootReducer from './redux/reducers'
// import App from './components/App'

// const store = createStore(
//   rootReducer,
//   applyMiddleware(thunk)
// );

// ReactDOM.render(
//   <Provider store={store}>
//     <App/>
//   </Provider>,
//   document.getElementById('root')
// );
```
