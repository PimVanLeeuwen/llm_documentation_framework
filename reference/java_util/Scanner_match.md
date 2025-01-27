#### match

```
public MatchResult match()
```
Returns the match result of the last scanning operation performed
by this scanner. This method throws `IllegalStateException`
if no match has been performed, or if the last match was
not successful.The various `next`methods of `Scanner`
make a match result available if they complete without throwing an
exception. For instance, after an invocation of the `nextInt()`
method that returned an int, this method returns a
`MatchResult` for the search of the
Integer regular expression
defined above. Similarly the `findInLine(java.lang.String)`,
`findWithinHorizon(java.lang.String, int)`, and `skip(java.util.regex.Pattern)` methods will make a
match available if they succeed.
Returns:
a match result for the last match operation
Throws:
`IllegalStateException` - If no match result is available

