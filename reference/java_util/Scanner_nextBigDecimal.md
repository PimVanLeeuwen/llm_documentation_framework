#### nextBigDecimal

```
public BigDecimal nextBigDecimal()
```
Scans the next token of the input as a `BigDecimal`.If the next token matches the Decimal regular expression defined
above then the token is converted into a BigDecimal value as if
by removing all group separators, mapping non-ASCII digits into ASCII
digits via the `Character.digit`, and passing the
resulting string to the `BigDecimal(String)`
constructor.
Returns:
the BigDecimal scanned from the input
Throws:
`InputMismatchException` - if the next token does not match the Decimal
regular expression, or is out of range
`NoSuchElementException` - if the input is exhausted
`IllegalStateException` - if this scanner is closed

