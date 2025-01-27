#### setRegion

```
public Locale.Builder setRegion(String region)
```
Sets the region. If region is null or the empty string, the region
in this `Builder` is removed. Otherwise,
the region must be well-formed or an
exception is thrown.The typical region value is a two-letter ISO 3166 code or a
three-digit UN M.49 area code.The country value in the `Locale` created by the
`Builder` is always normalized to upper case.
Parameters:
`region` - the region
Returns:
This builder.
Throws:
`IllformedLocaleException` - if `region` is ill-formed

