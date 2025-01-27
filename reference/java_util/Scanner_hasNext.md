#### hasNext

```
public boolean hasNext(Pattern pattern)
```
Returns true if the next complete token matches the specified pattern.
A complete token is prefixed and postfixed by input that matches
the delimiter pattern. This method may block while waiting for input.
The scanner does not advance past any input.
Parameters:
`pattern` - the pattern to scan for
Returns:
true if and only if this scanner has another token matching
the specified pattern
Throws:
`IllegalStateException` - if this scanner is closed

