% Module deliberately misspelt to avoid conflict with system module with same
-module(erlaang).
-export([hello_world/0]).

hello_world() -> io:fwrite("Hello World\n").
