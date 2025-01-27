#### nextShort

```
public short nextShort(int radix)
```
Scans the next token of the input as a short.
This method will throw `InputMismatchException`
if the next token cannot be translated into a valid short value as
described below. If the translation is successful, the scanner advances
past the input that matched.If the next token matches the Integer regular expression defined
above then the token is converted into a short value as if by
removing all locale specific prefixes, group separators, and locale
specific suffixes, then mapping non-ASCII digits into ASCII
digits via `Character.digit`, prepending a
negative sign (-) if the locale specific negative prefixes and suffixes
were present, and passing the resulting string to
`Short.parseShort` with the
specified radix.
Parameters:
`radix` - the radix used to interpret the token as a short value
Returns:
the short scanned from the input
Throws:
`InputMismatchException` - if the next token does not match the Integer
regular expression, or is out of range
`NoSuchElementException` - if input is exhausted
`IllegalStateException` - if this scanner is closed

