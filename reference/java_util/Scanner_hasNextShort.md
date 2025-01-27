#### hasNextShort

```
public boolean hasNextShort(int radix)
```
Returns true if the next token in this scanner's input can be
interpreted as a short value in the specified radix using the
`nextShort()` method. The scanner does not advance past any input.
Parameters:
`radix` - the radix used to interpret the token as a short value
Returns:
true if and only if this scanner's next token is a valid
short value in the specified radix
Throws:
`IllegalStateException` - if this scanner is closed

