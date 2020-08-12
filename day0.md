### Promises in Javascript
Promises are used in asynchronous code, they represent an eventual outcome. While waiting for the outcome, a promise is considered pending but eventually it will either resolve (success) or reject (failure).
To construct a promise you use the *new* keyword to construct a Promise, and pass in as a parameter an **executor function** which runs when the constructor is called. The executor function itself takes two functions as parameters, resolve and reject, which handle how the promise responds. Under the hood, if resolve is invoked, the Promise's state is changed to fulfilled. Likewise, if reject is invoked, the Promise is rejected

We don't *usually* construct a promise ourself, rather use the output.
Each Promise comes with a `.then()` method which you can use to say what will happen after a Promise resolves (or rejects). `.then()` takes two parameters which are functions - first is `onFulfilled` and second is `onRejected` , which are nicely self-explanatory. These are also referred to as success handler and failure handler. The function `then()` always **returns** a Promise. If no appropriate handler is called inside `then` the Promise it returns will have the same resolved value and the Promise it was called on. What?! This means you can chain `.then()` together or chain `then()` followed by a `catch()` to concisely handle any rejection. Example:
```js
myPromise
  .then((resolvedValue) => {
    console.log(resolvedValue);
  })
  .catch((rejectionReason) => {
    console.log(rejectionReason);
  });
  ```
We can also chain promises together:
```js
firstPromiseFunction()
.then((firstResolveVal) => {
  return secondPromiseFunction(firstResolveVal);
})
.then((secondResolveVal) => {
  console.log(secondResolveVal);
});
```
What does the above code do? We invoke the firstPromiseFunction which returns a promise. We invoke `then` on the returned value with an anonymous function as the success handler. Inside the `then` we return a **new** Promise which is the result of invoking the secondPromiseFunction passing firstResolveVal as a parameter. In the second `then`, when second promise has resolved, the second promise's resolved value is output to the console. This is quite a mouthful!

There are two main bad practices which can happen using Promises. First is nesting them - this is bad because it reminds you of the callback hell!
The second main error you can make is forgetting to `return` a Promise from inside your `then()` successHandler call, this will cause the wrong Promise resolution to be passed to subsequent `then` calls which can make troubleshooting very difficult.

**Promise.any()** can be used to handle multiple Promises, without regard to order. Promise.all() accepts an Array of Promises as its argument and returns a single Promise. The returned Promise is either Resolved (if all resolve) or if Rejected if any single Promise in the Array rejects. The example given:
```js
let myPromises = Promise.all([returnsPromOne(), returnsPromTwo(), returnsPromThree()]);

myPromises
  .then((arrayOfValues) => {
    console.log(arrayOfValues);
  })
  .catch((rejectionReason) => {
    console.log(rejectionReason);
  });
  ```
  This is taking advantage of *concurrency* in our application by allowing all three Promises to run at once.
