#### end

```
int end(int group)
```
Returns the offset after the last character of the subsequence
captured by the given group during this match.Capturing groups are indexed from left
to right, starting at one. Group zero denotes the entire pattern, so
the expression m.end(0) is equivalent to
m.end().
Parameters:
`group` - The index of a capturing group in this matcher's pattern
Returns:
The offset after the last character captured by the group,
or -1 if the match was successful
but the group itself did not match anything
Throws:
`IllegalStateException` - If no match has yet been attempted,
or if the previous match operation failed
`IndexOutOfBoundsException` - If there is no capturing group in the pattern
with the given index

