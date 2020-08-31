## Redux

Redux is a state management framework for JavaScript. It is often used with React but not exclusively.
There is a single state object that is responsible for the entire state of the application. The Redux *store* is the single source of truth. Any time a piece of your app wants to update state, it must go through the Redux store.

The Redux **store** is an object which holds and manages state. You can retrieve state using the method getState
```js
const store = Redux.createStore(
  (state = 5) => state
);

// change code below this line
let currentState = store.getState()
```
State updates are triggered by *actions* which are defined in the action object. The action object carries a 'type' property that specifies the type of action that occurred. After creating an action, you need to send the action to the Redux store so it can update its state. This is done with an action creator. An action creator is a function that returns an action.
```js
const action = {
  type: 'LOGIN'
}
// Define an action creator here:
const actionCreator = () =>{
  return action
}
```
The `store.dispatch()` method is what is used to pass the action to the store.

`store.dispatch(actionCreator())`

A **reducer** function responds to the action. It takes state and action as arguments and always and only returns a new state - it is a pure function with no side effects. In Redux state is readonly, so the reducer function must always return a copy of state and never modify state directly. In this example we are returning a new state with login:true if the action type is 'login', otherwise we just return the existing state.
```js
const defaultState = {
  login: false
};

const reducer = (state = defaultState, action) => {
  if(action.type == 'LOGIN'){
    return {
      login: true
    };
  } else {
    return state;
  }
};

const store = Redux.createStore(reducer);

const loginAction = () => {
  return {
    type: 'LOGIN'
  }
};
```
The redux store object has a method called Subscribe which allows you to subscribe listener functions to the store. You pass a callback into `store.subscribe(cb)`

You may have multiple reducers which handle different parts of the state (though it is the SAME STATE as there can only be one state). These can be combined to a unified reducer using the `Redux.combineReducers` method, which takes an object whose keys are the names and values are the reducer functions:

> Typically, it is a good practice to create a reducer for each piece of application state when they are distinct or unique in some way. For example, in a note-taking app with user authentication, one reducer could handle authentication while another handles the text and notes that the user is submitting. For such an application, we might write the combineReducers() method like this:
> ```js
const rootReducer = Redux.combineReducers({
  auth: authenticationReducer,
  notes: notesReducer
});
>```

Putting it all together:
```js
const INCREMENT = 'INCREMENT'; // define a constant for increment action types
const DECREMENT = 'DECREMENT'; // define a constant for decrement action types
const defaultState = 0;
// define the counter reducer which will increment or decrement the state based on the action it receives
const counterReducer = (state = defaultState, action) => {
  if(action.type == INCREMENT){
    return state+1
  } else if (action.type == DECREMENT){
    return state-1
  } else {
    return state  //need to have the default case!
  }
};

// define an action creator for incrementing
const incAction = () => {
  return {
    type: INCREMENT,

  }
};
// define an action creator for decrementing
const decAction = () =>{
  return {
    type: DECREMENT,
  }
};

const store = Redux.createStore(counterReducer); // define the Redux store here, passing in your reducers
```
Remember that state should be immutable, including an properties that are arrays or objects. Therefore we should always return new arrays/objects and not modify previous ones. Think about using spread operator, concat, slice for arrays (NOT push, splice) and Object.assign for objects.
