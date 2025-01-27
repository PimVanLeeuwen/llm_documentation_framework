#### hasNextLong

```
public boolean hasNextLong(int radix)
```
Returns true if the next token in this scanner's input can be
interpreted as a long value in the specified radix using the
`nextLong()` method. The scanner does not advance past any input.
Parameters:
`radix` - the radix used to interpret the token as a long value
Returns:
true if and only if this scanner's next token is a valid
long value
Throws:
`IllegalStateException` - if this scanner is closed

