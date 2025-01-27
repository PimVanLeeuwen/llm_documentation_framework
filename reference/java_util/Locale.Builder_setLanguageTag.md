#### setLanguageTag

```
public Locale.Builder setLanguageTag(String languageTag)
```
Resets the Builder to match the provided IETF BCP 47
language tag. Discards the existing state. Null and the
empty string cause the builder to be reset, like `clear()`. Grandfathered tags (see `Locale.forLanguageTag(java.lang.String)`) are converted to their canonical
form before being processed. Otherwise, the language tag
must be well-formed (see `Locale`) or an exception is
thrown (unlike `Locale.forLanguageTag`, which
just discards ill-formed and following portions of the
tag).
Parameters:
`languageTag` - the language tag
Returns:
This builder.
Throws:
`IllformedLocaleException` - if `languageTag` is ill-formed
See Also:
`Locale.forLanguageTag(String)`

