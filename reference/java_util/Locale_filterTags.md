#### filterTags

```
public static List<String> filterTags(List<Locale.LanguageRange> priorityList,
                                      Collection<String> tags)
```
Returns a list of matching languages tags using the basic filtering
mechanism defined in RFC 4647. This is equivalent to
`filterTags(List, Collection, FilteringMode)` when `mode`
is `Locale.FilteringMode.AUTOSELECT_FILTERING`.
Parameters:
`priorityList` - user's Language Priority List in which each language
tag is sorted in descending order based on priority or weight
`tags` - language tags
Returns:
a list of matching language tags sorted in descending order
based on priority or weight, or an empty list if nothing matches.
The list is modifiable.
Throws:
`NullPointerException` - if `priorityList` or `tags` is
`null`
Since:
1.8

