#### next

```
public String next(Pattern pattern)
```
Returns the next token if it matches the specified pattern. This
method may block while waiting for input to scan, even if a previous
invocation of `hasNext(Pattern)` returned `true`.
If the match is successful, the scanner advances past the input that
matched the pattern.
Parameters:
`pattern` - the pattern to scan for
Returns:
the next token
Throws:
`NoSuchElementException` - if no more tokens are available
`IllegalStateException` - if this scanner is closed

