#### group

```
String group(int group)
```
Returns the input subsequence captured by the given group during the
previous match operation.For a matcher m, input sequence s, and group index
g, the expressions m.group(g) and
s.substring(m.start(g), m.end(g))
are equivalent.Capturing groups are indexed from left
to right, starting at one. Group zero denotes the entire pattern, so
the expression m.group(0) is equivalent to m.group().If the match was successful but the group specified failed to match
any part of the input sequence, then null is returned. Note
that some groups, for example (a\*), match the empty string.
This method will return the empty string when such a group successfully
matches the empty string in the input.
Parameters:
`group` - The index of a capturing group in this matcher's pattern
Returns:
The (possibly empty) subsequence captured by the group
during the previous match, or null if the group
failed to match part of the input
Throws:
`IllegalStateException` - If no match has yet been attempted,
or if the previous match operation failed
`IndexOutOfBoundsException` - If there is no capturing group in the pattern
with the given index

