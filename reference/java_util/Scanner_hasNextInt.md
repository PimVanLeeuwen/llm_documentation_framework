#### hasNextInt

```
public boolean hasNextInt(int radix)
```
Returns true if the next token in this scanner's input can be
interpreted as an int value in the specified radix using the
`nextInt()` method. The scanner does not advance past any input.
Parameters:
`radix` - the radix used to interpret the token as an int value
Returns:
true if and only if this scanner's next token is a valid
int value
Throws:
`IllegalStateException` - if this scanner is closed

