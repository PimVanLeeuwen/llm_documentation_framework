#### joining

```
public static Collector<CharSequence,?,String> joining(CharSequence delimiter,
                                                       CharSequence prefix,
                                                       CharSequence suffix)
```
Returns a `Collector` that concatenates the input elements,
separated by the specified delimiter, with the specified prefix and
suffix, in encounter order.
Parameters:
`delimiter` - the delimiter to be used between each element
`prefix` - the sequence of characters to be used at the beginning
of the joined result
`suffix` - the sequence of characters to be used at the end
of the joined result
Returns:
A `Collector` which concatenates CharSequence elements,
separated by the specified delimiter, in encounter order

