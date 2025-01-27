#### nextBigInteger

```
public BigInteger nextBigInteger(int radix)
```
Scans the next token of the input as a `BigInteger`.If the next token matches the Integer regular expression defined
above then the token is converted into a BigInteger value as if
by removing all group separators, mapping non-ASCII digits into ASCII
digits via the `Character.digit`, and passing the
resulting string to the `BigInteger(String, int)` constructor with the specified radix.
Parameters:
`radix` - the radix used to interpret the token
Returns:
the BigInteger scanned from the input
Throws:
`InputMismatchException` - if the next token does not match the Integer
regular expression, or is out of range
`NoSuchElementException` - if the input is exhausted
`IllegalStateException` - if this scanner is closed

