#### nextLine

```
public String nextLine()
```
Advances this scanner past the current line and returns the input
that was skipped.
This method returns the rest of the current line, excluding any line
separator at the end. The position is set to the beginning of the next
line.Since this method continues to search through the input looking
for a line separator, it may buffer all of the input searching for
the line to skip if no line separators are present.
Returns:
the line that was skipped
Throws:
`NoSuchElementException` - if no line was found
`IllegalStateException` - if this scanner is closed

