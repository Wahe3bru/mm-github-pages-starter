# JavaScript Notes (from FreeCodeCamp)

## Basic JS
statements end with a semicolon `;`

Comments
```js
// inline comment

/* multiline
   comment */
```

Variables
Variable names can be made up of numbers, letters, and `$` or `_`, but may not contain spaces or start with a number.
camelCase is the preferred

declare variables: `var myName;` or `var myName = "waheeb;"`

increment var: `myNum++;`
decrement var `myNum--;`

String
use`.length` to get length of string.
use bracket notation (zero indexed)

Arrays (like lists)
to append at the end of an array `myArray.push(["val1","val5"])`
remove last element from array use `pop()` - the popped element can be saved to a var
```js
var popped = myArray.pop()
```
`shift()` removes an element from the front of the array.
`unshift()` is like `push()` but adds elements to the front of the array.

functions
```js
function myFunction(param1, param2){
  //code here
}
```
if a variable is declared without using `var` - then it is automatically a global variable (even if created in a function). 
