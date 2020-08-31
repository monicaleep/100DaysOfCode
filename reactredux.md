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

OK! Now we have both, we use the `react-redux` package from npm to connect them. There's two key features: Provider and connect/ The Provider is a wrapper component that wraps your React app. This wrapper then allows you to access the Redux `store` and `dispatch` functions throughout your component tree. Provider takes 2 props, the redux store and the child components of your app.
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
