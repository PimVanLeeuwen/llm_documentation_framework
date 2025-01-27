#### findInLine

```
public String findInLine(Pattern pattern)
```
Attempts to find the next occurrence of the specified pattern ignoring
delimiters. If the pattern is found before the next line separator, the
scanner advances past the input that matched and returns the string that
matched the pattern.
If no such pattern is detected in the input up to the next line
separator, then `null` is returned and the scanner's
position is unchanged. This method may block waiting for input that
matches the pattern.Since this method continues to search through the input looking
for the specified pattern, it may buffer all of the input searching for
the desired token if no line separators are present.
Parameters:
`pattern` - the pattern to scan for
Returns:
the text that matched the specified pattern
Throws:
`IllegalStateException` - if this scanner is closed

