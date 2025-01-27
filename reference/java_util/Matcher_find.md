#### find

```
public boolean find(int start)
```
Resets this matcher and then attempts to find the next subsequence of
the input sequence that matches the pattern, starting at the specified
index.If the match succeeds then more information can be obtained via the
start, end, and group methods, and subsequent
invocations of the `find()` method will start at the first
character not matched by this match.
Parameters:
`start` - the index to start searching for a match
Returns:
true if, and only if, a subsequence of the input
sequence starting at the given index matches this matcher's
pattern
Throws:
`IndexOutOfBoundsException` - If start is less than zero or if start is greater than the
length of the input sequence.

