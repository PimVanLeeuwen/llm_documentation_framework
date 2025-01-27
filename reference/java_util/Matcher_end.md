#### end

```
public int end(String name)
```
Returns the offset after the last character of the subsequence
captured by the given named-capturing
group during the previous match operation.
Parameters:
`name` - The name of a named-capturing group in this matcher's pattern
Returns:
The offset after the last character captured by the group,
or `-1` if the match was successful
but the group itself did not match anything
Throws:
`IllegalStateException` - If no match has yet been attempted,
or if the previous match operation failed
`IllegalArgumentException` - If there is no capturing group in the pattern
with the given name
Since:
1.8

