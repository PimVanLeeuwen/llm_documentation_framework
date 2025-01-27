#### formatTo

```
void formatTo(Formatter formatter,
              int flags,
              int width,
              int precision)
```
Formats the object using the provided `formatter`.
Parameters:
`formatter` - The `formatter`. Implementing classes may call
`formatter.out()` or `formatter.locale()` to obtain the `Appendable` or `Locale` used by this
formatter respectively.
`flags` - The flags modify the output format. The value is interpreted as
a bitmask. Any combination of the following flags may be set:
`FormattableFlags.LEFT_JUSTIFY`, `FormattableFlags.UPPERCASE`, and `FormattableFlags.ALTERNATE`. If no flags are set, the default
formatting of the implementing class will apply.
`width` - The minimum number of characters to be written to the output.
If the length of the converted value is less than the
width then the output will be padded by
'  ' until the total number of characters
equals width. The padding is at the beginning by default. If
the `FormattableFlags.LEFT_JUSTIFY` flag is set then the
padding will be at the end. If width is -1
then there is no minimum.
`precision` - The maximum number of characters to be written to the output.
The precision is applied before the width, thus the output will
be truncated to precision characters even if the
width is greater than the precision. If
precision is -1 then there is no explicit
limit on the number of characters.
Throws:
`IllegalFormatException` - If any of the parameters are invalid. For specification of all
possible formatting errors, see the Details section of the
formatter class specification.




