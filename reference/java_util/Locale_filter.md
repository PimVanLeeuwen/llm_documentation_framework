#### filter

```
public static List<Locale> filter(List<Locale.LanguageRange> priorityList,
                                  Collection<Locale> locales)
```
Returns a list of matching `Locale` instances using the filtering
mechanism defined in RFC 4647. This is equivalent to
`filter(List, Collection, FilteringMode)` when `mode` is
`Locale.FilteringMode.AUTOSELECT_FILTERING`.
Parameters:
`priorityList` - user's Language Priority List in which each language
tag is sorted in descending order based on priority or weight
`locales` - `Locale` instances used for matching
Returns:
a list of `Locale` instances for matching language tags
sorted in descending order based on priority or weight, or an empty
list if nothing matches. The list is modifiable.
Throws:
`NullPointerException` - if `priorityList` or `locales`
is `null`
Since:
1.8

