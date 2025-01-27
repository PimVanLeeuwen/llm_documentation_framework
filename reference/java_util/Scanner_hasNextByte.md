#### hasNextByte

```
public boolean hasNextByte(int radix)
```
Returns true if the next token in this scanner's input can be
interpreted as a byte value in the specified radix using the
`nextByte()` method. The scanner does not advance past any input.
Parameters:
`radix` - the radix used to interpret the token as a byte value
Returns:
true if and only if this scanner's next token is a valid
byte value
Throws:
`IllegalStateException` - if this scanner is closed

