#### useDelimiter

```
public Scanner useDelimiter(String pattern)
```
Sets this scanner's delimiting pattern to a pattern constructed from
the specified `String`.An invocation of this method of the form
useDelimiter(pattern) behaves in exactly the same way as the
invocation useDelimiter(Pattern.compile(pattern)).Invoking the `reset()` method will set the scanner's delimiter
to the default.
Parameters:
`pattern` - A string specifying a delimiting pattern
Returns:
this scanner

