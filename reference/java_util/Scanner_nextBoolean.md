#### nextBoolean

```
public boolean nextBoolean()
```
Scans the next token of the input into a boolean value and returns
that value. This method will throw `InputMismatchException`
if the next token cannot be translated into a valid boolean value.
If the match is successful, the scanner advances past the input that
matched.
Returns:
the boolean scanned from the input
Throws:
`InputMismatchException` - if the next token is not a valid boolean
`NoSuchElementException` - if input is exhausted
`IllegalStateException` - if this scanner is closed

