#### setLocale

```
public Locale.Builder setLocale(Locale locale)
```
Resets the `Builder` to match the provided
`locale`. Existing state is discarded.All fields of the locale must be well-formed, see `Locale`.Locales with any ill-formed fields cause
`IllformedLocaleException` to be thrown, except for the
following three cases which are accepted for compatibility
reasons:Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"Locale("no", "NO", "NY") is treated as "nn-NO"
Parameters:
`locale` - the locale
Returns:
This builder.
Throws:
`IllformedLocaleException` - if `locale` has
any ill-formed fields.
`NullPointerException` - if `locale` is null.

