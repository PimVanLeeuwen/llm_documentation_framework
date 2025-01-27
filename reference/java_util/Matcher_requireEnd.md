#### requireEnd

```
public boolean requireEnd()
```
Returns true if more input could change a positive match into a
negative one.If this method returns true, and a match was found, then more
input could cause the match to be lost. If this method returns false
and a match was found, then more input might change the match but the
match won't be lost. If a match was not found, then requireEnd has no
meaning.
Returns:
true iff more input could change a positive match into a
negative one.
Since:
1.5




