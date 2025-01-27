#### setVariant

```
public Locale.Builder setVariant(String variant)
```
Sets the variant. If variant is null or the empty string, the
variant in this `Builder` is removed. Otherwise, it
must consist of one or more well-formed
subtags, or an exception is thrown.Note: This method checks if `variant`
satisfies the IETF BCP 47 variant subtag's syntax requirements,
and normalizes the value to lowercase letters. However,
the `Locale` class does not impose any syntactic
restriction on variant, and the variant value in
`Locale` is case sensitive. To set such a variant,
use a Locale constructor.
Parameters:
`variant` - the variant
Returns:
This builder.
Throws:
`IllformedLocaleException` - if `variant` is ill-formed

