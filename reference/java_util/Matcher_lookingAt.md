#### lookingAt

```
public boolean lookingAt()
```
Attempts to match the input sequence, starting at the beginning of the
region, against the pattern.Like the `matches` method, this method always starts
at the beginning of the region; unlike that method, it does not
require that the entire region be matched.If the match succeeds then more information can be obtained via the
start, end, and group methods.
Returns:
true if, and only if, a prefix of the input
sequence matches this matcher's pattern

