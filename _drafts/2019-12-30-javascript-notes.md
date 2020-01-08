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

equality
- `==` type coercion therefore `10 == '10'` will be true
- `===` no type coercion therefore `10 === '10'` will be false
- `!=` and `!==` would be the counter to the above

`typeof`operator returns the datatype of the object.

Switch statement
A switch statement tests a value and can have many `case` statements which define various possible values. Statements are executed from the first matched case value until a break is encountered.
```js
function switchOfStuff(val) {
  var answer = "";
  switch (val) {
    case "a":
      answer = "apple";
      break;
    case "b":
      answer = "bird";
      break;
    case "c":
      answer = "cat";
      break;
    default:
      answer = "stuff"
  }
  return answer;
}

switchOfStuff(1);
```

statements will be executed until a break is encountered, therefore it can be used as:
```js
function sequentialSizes(val) {
  var answer = "";
  switch (val) {
    case 1:
    case 2:
    case 3:
      answer = "Low";
      break;
    case 4:
    case 5:
    case 6:
      answer = "Mid";
      break;
    case 7:
    case 8:
    case 9:
      answer = "High";
      break;
  }
  return answer;
}

sequentialSizes(1);
```

JavaScript objects
- similar to python dictionaries.
- objects can be accessed by dot-notation `myDog.name;` or bracket-notation `myDog["name"];`
- add a property same way used to modify them `myDog.says = "woof";`
- remove property `delete myDog.says;`
- can be used for lookup instead of switch statement:
```js
function phoneticLookup(val) {
  var result = "";

  var lookup = {
    "alpha": "Adams",
    "bravo": "Boston",
    "charlie": "Chicago",
    "delta": "Denver",
    "echo": "Easy",
    "foxtrot": "Frank"
  };
  result = lookup[val];

  return result;
}

phoneticLookup("charlie");
```

test if object has property
```js
var myObj = {
  gift: "pony",
  pet: "kitten",
  bed: "sleigh"
};

function checkObj(checkProp) {
  // Your Code Here
  if (myObj.hasOwnProperty(checkProp)) {
    return myObj[checkProp];
  }
  return "Not Found";
}

checkObj("gift");
```

Loops
while
for
do...while
- guarantee loop runs once
```js
var myArray = [];
var i = 10;

do {
  myArray.push(i);
  i++;
} while (i < 5);
```
