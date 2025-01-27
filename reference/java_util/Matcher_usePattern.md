#### usePattern

```
public Matcher usePattern(Pattern newPattern)
```
Changes the Pattern that this Matcher uses to
find matches with.This method causes this matcher to lose information
about the groups of the last match that occurred. The
matcher's position in the input is maintained and its
last append position is unaffected.
Parameters:
`newPattern` - The new pattern used by this matcher
Returns:
This matcher
Throws:
`IllegalArgumentException` - If newPattern is null
Since:
1.5

