#### nextDouble

```
public double nextDouble()
```
Scans the next token of the input as a double.
This method will throw `InputMismatchException`
if the next token cannot be translated into a valid double value.
If the translation is successful, the scanner advances past the input
that matched.If the next token matches the Float regular expression defined above
then the token is converted into a double value as if by
removing all locale specific prefixes, group separators, and locale
specific suffixes, then mapping non-ASCII digits into ASCII
digits via `Character.digit`, prepending a
negative sign (-) if the locale specific negative prefixes and suffixes
were present, and passing the resulting string to
`Double.parseDouble`. If the token matches
the localized NaN or infinity strings, then either "Nan" or "Infinity"
is passed to `Double.parseDouble` as
appropriate.
Returns:
the double scanned from the input
Throws:
`InputMismatchException` - if the next token does not match the Float
regular expression, or is out of range
`NoSuchElementException` - if the input is exhausted
`IllegalStateException` - if this scanner is closed

