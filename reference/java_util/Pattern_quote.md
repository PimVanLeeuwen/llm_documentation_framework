#### quote

```
public static String quote(String s)
```
Returns a literal pattern `String` for the specified
`String`.This method produces a `String` that can be used to
create a `Pattern` that would match the string
`s` as if it were a literal pattern.Metacharacters
or escape sequences in the input sequence will be given no special
meaning.
Parameters:
`s` - The string to be literalized
Returns:
A literal string replacement
Since:
1.5

