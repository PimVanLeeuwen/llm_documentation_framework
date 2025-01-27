#### lookup

```
public static Locale lookup(List<Locale.LanguageRange> priorityList,
                            Collection<Locale> locales)
```
Returns a `Locale` instance for the best-matching language
tag using the lookup mechanism defined in RFC 4647.
Parameters:
`priorityList` - user's Language Priority List in which each language
tag is sorted in descending order based on priority or weight
`locales` - `Locale` instances used for matching
Returns:
the best matching `Locale` instance chosen based on
priority or weight, or `null` if nothing matches.
Throws:
`NullPointerException` - if `priorityList` or `tags` is
`null`
Since:
1.8

