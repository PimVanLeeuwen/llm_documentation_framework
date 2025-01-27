#### lookupTag

```
public static String lookupTag(List<Locale.LanguageRange> priorityList,
                               Collection<String> tags)
```
Returns the best-matching language tag using the lookup mechanism
defined in RFC 4647.
Parameters:
`priorityList` - user's Language Priority List in which each language
tag is sorted in descending order based on priority or weight
`tags` - language tangs used for matching
Returns:
the best matching language tag chosen based on priority or
weight, or `null` if nothing matches.
Throws:
`NullPointerException` - if `priorityList` or `tags` is
`null`
Since:
1.8




