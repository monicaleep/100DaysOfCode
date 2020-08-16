## Sass
What is Sass? It is a way to organize and add logic to CSS. It is an extension of CSS which adds features such as variables and logic. There are two types of Sass code `.scss.` and `.sass` which have slightly different syntax (e.g. `.sass` does not require semicolons to separate properties). I am using `.scss` syntax below.

Variables: Used to simply code and also avoid repetition.
```scss
$main-fonts: Arial, sans-serif;
$headings-color: green;

//To use variables:
h1 {
  font-family: $main-fonts;
  color: $headings-color;
}
```
<br>
Mixins: A defined style which can be reapplied to many elements. They can also take in variables as parameters, and are used in the styles with the `@include` keyword.

```scss
@mixin border-radius($val){
  border-radius: $val;
  -moz-border-radius: $val;
  -webkit-border-radius: $val;
  -ms-border-radius: $val;
}

#awesome {
  @include border-radius(15px);
  width: 150px;
  height: 150px;
  background-color: green;

}
```

<br>
Conditionals: Sass supports the use of conditionals. This can be combined with mixins and variables to create reusable snippets:

```scss
@mixin border-stroke($val){
  @if $val == light{
    border: 1px solid black;
  }
  @else if $val == heavy{
    border: 6px solid black;
  }
  @else{
    border:none;
  }
}
#box {
  width: 150px;
  height: 150px;
  background-color: red;
  @include border-stroke(medium);
}
```
<br>
For loops can also be used, this could be helpful when combined with a flex or grid layout, as some math can also be included inside the loop. The code snippet below will create 5 classes for `text-1`...`text-5` and each class with have the `font-size` property to be 15*j

```scss
@for $j from 1 to 6{
  .text-#{$j} {
    font-size: 15px * $j;
  }
}
```
You can use an `each` loop to iterate over an existing list. The below code will set the `div` of each `{color}-bg` class to have the correct respective background color. I can't yet think of a use case for this one..
```scss
<style type='text/scss'>
  @each $color in blue,black,red {
    .#{$color}-bg {background-color: $color};
  }
  div {
    height: 200px;
    width: 200px;
  }
</style>
<div class="blue-bg"></div>
<div class="black-bg"></div>
<div class="red-bg"></div>

```

A while loop can also be used, as in the for loop above:
```scss
$x: 1;
@while $x < 6 {
  .text-#{$x} {font-size: 15px* $x;}
  $x: $x +1;
}
```


Partials are used the scss to modularize the codebase. Partials names start with an underscore and use the .scss extension ("_partials.scss"). They are brought into a file using the ` @import "partials" ` statement, excluding the underscore.
Sass has an `extend` feature which takes rules from one element and applies them to another. Usage: `@extend .class` or `@extend h1` etc.
