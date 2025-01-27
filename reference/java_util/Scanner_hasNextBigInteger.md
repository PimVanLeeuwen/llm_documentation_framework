#### hasNextBigInteger

```
public boolean hasNextBigInteger(int radix)
```
Returns true if the next token in this scanner's input can be
interpreted as a `BigInteger` in the specified radix using
the `nextBigInteger()` method. The scanner does not advance past
any input.
Parameters:
`radix` - the radix used to interpret the token as an integer
Returns:
true if and only if this scanner's next token is a valid
`BigInteger`
Throws:
`IllegalStateException` - if this scanner is closed

