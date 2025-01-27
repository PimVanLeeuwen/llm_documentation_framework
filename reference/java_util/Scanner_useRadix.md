#### useRadix

```
public Scanner useRadix(int radix)
```
Sets this scanner's default radix to the specified radix.A scanner's radix affects elements of its default
number matching regular expressions; see
localized numbers above.If the radix is less than `Character.MIN_RADIX`
or greater than `Character.MAX_RADIX`, then an
`IllegalArgumentException` is thrown.Invoking the `reset()` method will set the scanner's radix to
`10`.
Parameters:
`radix` - The radix to use when scanning numbers
Returns:
this scanner
Throws:
`IllegalArgumentException` - if radix is out of range

