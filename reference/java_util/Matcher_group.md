#### group

```
public String group(String name)
```
Returns the input subsequence captured by the given
named-capturing group during the previous
match operation.If the match was successful but the group specified failed to match
any part of the input sequence, then null is returned. Note
that some groups, for example (a\*), match the empty string.
This method will return the empty string when such a group successfully
matches the empty string in the input.
Parameters:
`name` - The name of a named-capturing group in this matcher's pattern
Returns:
The (possibly empty) subsequence captured by the named group
during the previous match, or null if the group
failed to match part of the input
Throws:
`IllegalStateException` - If no match has yet been attempted,
or if the previous match operation failed
`IllegalArgumentException` - If there is no capturing group in the pattern
with the given name
Since:
1.7

