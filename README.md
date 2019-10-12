
This repository contains code that outputs "Hello World" to stdout
in various programming languages.
"Hello World" programs are typically the first code most new comers
use to interface with a programming language. Per
[this Stackoverflow answer](https://stackoverflow.com/a/12785204)
such programs were first used by Brian Kernighan and Martin Richards
at Bell Labs during 1970s and tradition has since been honored by
many new programming language books, tutorials and courses.


Ada
-----
```ada
with Ada.Text_IO;
use Ada.Text_IO;
procedure AdaHelloWorld is
begin
     Put_Line ("Hello World");
end AdaHelloWorld;
```

Bash
-----
```bash
#!/usr/bin/bash

echo "Hello World";
```

C#
-----
```c#
using System;

class Program {
  static void Main() {
    Console.WriteLine("Hello World");
  }
}
```

C++
-----
```c++
#include <iostream>

int main(int argc, char** argv) {
  std::cout << "Hello World" << std::endl;
  return 0;
}
```

C
-----
```c
#include <stdio.h>

int main(int argc, char** argv) {
  printf("Hello World\n");
  return 0;
}
```

Css
-----
```css
body::after {
  content: "Hello World";
}
```

Elixir
-----
```elixir
IO.puts "Hello World"
```

Erlang
-----
```erlang
% Module deliberately misspelt to avoid conflict with system module with same
-module(erlaang).
-export([hello_world/0]).

hello_world() -> io:fwrite("Hello World\n").
```

F#
-----
```f#
printfn "Hello World\n"
```

Golang
-----
```golang
package main;

import "fmt"

func main() {
  fmt.Println("Hello World")
}
```

Haskell
-----
```haskell
main :: IO()
main = putStrLn "Hello World"
```

Html
-----
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <h1>Hello World</h1>
</body>
</html>
```

Java
-----
```Java
class Java {

  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}
```

Javascript
-----
```javascript
console.log("Hello World");
```

Lua
-----
```lua
print("Hello World")
```

Ocaml
-----
```ocaml
open Printf;;
Printf.printf "Hello World\n";;
```

Perl
-----
```perl
#!/usr/bin/perl

print "Hello World\n"
```

Powershell
-----
```powershell
Write-Host "Hello, World"```

Processing
-----
```processing
size(128, 128);
background(0);
textAlign(CENTER, CENTER);
fill(255);
text("Hello World", width / 2, height / 2);
```

Prolog
-----
```prolog
:- initialization(main).
main :- writef("%s\n", ["Hello World"]).
```

Python
-----
```python
#!/usr/bin/env python

if __name__ == '__main__':
    print("Hello World")
```

R
-----
```r
print("Hello World")
```

Ruby
-----
```ruby
#!/usr/bin/ruby

print "Hello World\n"
```

Rust
-----
```rust
fn main() {
  println!("Hello World");
}
```

Scm_Chicken
-----
```SCM_Chicken
(print "Hello World");
```

