#### nextFloat

```
public float nextFloat()
```
Scans the next token of the input as a float.
This method will throw `InputMismatchException`
if the next token cannot be translated into a valid float value as
described below. If the translation is successful, the scanner advances
past the input that matched.If the next token matches the Float regular expression defined above
then the token is converted into a float value as if by
removing all locale specific prefixes, group separators, and locale
specific suffixes, then mapping non-ASCII digits into ASCII
digits via `Character.digit`, prepending a
negative sign (-) if the locale specific negative prefixes and suffixes
were present, and passing the resulting string to
`Float.parseFloat`. If the token matches
the localized NaN or infinity strings, then either "Nan" or "Infinity"
is passed to `Float.parseFloat` as
appropriate.
Returns:
the float scanned from the input
Throws:
`InputMismatchException` - if the next token does not match the Float
regular expression, or is out of range
`NoSuchElementException` - if input is exhausted
`IllegalStateException` - if this scanner is closed

