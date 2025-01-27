#### skip

```
public Scanner skip(String pattern)
```
Skips input that matches a pattern constructed from the specified
string.An invocation of this method of the form skip(pattern)
behaves in exactly the same way as the invocation
skip(Pattern.compile(pattern)).
Parameters:
`pattern` - a string specifying the pattern to skip over
Returns:
this scanner
Throws:
`IllegalStateException` - if this scanner is closed

