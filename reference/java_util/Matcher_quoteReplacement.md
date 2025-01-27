#### quoteReplacement

```
public static String quoteReplacement(String s)
```
Returns a literal replacement `String` for the specified
`String`.
This method produces a `String` that will work
as a literal replacement `s` in the
`appendReplacement` method of the `Matcher` class.
The `String` produced will match the sequence of characters
in `s` treated as a literal sequence. Slashes ('\') and
dollar signs ('$') will be given no special meaning.
Parameters:
`s` - The string to be literalized
Returns:
A literal string replacement
Since:
1.5

