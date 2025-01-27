#### hasNextBigDecimal

```
public boolean hasNextBigDecimal()
```
Returns true if the next token in this scanner's input can be
interpreted as a `BigDecimal` using the
`nextBigDecimal()` method. The scanner does not advance past any
input.
Returns:
true if and only if this scanner's next token is a valid
`BigDecimal`
Throws:
`IllegalStateException` - if this scanner is closed

