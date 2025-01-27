#### split

```
public String[] split(CharSequence input)
```
Splits the given input sequence around matches of this pattern.This method works as if by invoking the two-argument `split` method with the given input
sequence and a limit argument of zero. Trailing empty strings are
therefore not included in the resulting array.The input "boo:and:foo", for example, yields the following
results with these expressions:

Regex    Result:{ "boo", "and", "foo" }o{ "b", "", ":and:f" }

Parameters:
`input` - The character sequence to be split
Returns:
The array of strings computed by splitting the input
around matches of this pattern

