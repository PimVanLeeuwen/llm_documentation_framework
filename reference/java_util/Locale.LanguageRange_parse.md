#### parse

```
public static List<Locale.LanguageRange> parse(String ranges,
                                               Map<String,List<String>> map)
```
Parses the given `ranges` to generate a Language Priority
List, and then customizes the list using the given `map`.
This method is equivalent to
`mapEquivalents(parse(ranges), map)`.
Parameters:
`ranges` - a list of comma-separated language ranges or a list
of language ranges in the form of the "Accept-Language" header
defined in RFC
2616
`map` - a map containing information to customize language ranges
Returns:
a Language Priority List with customization. The list is
modifiable.
Throws:
`NullPointerException` - if `ranges` is null
`IllegalArgumentException` - if a language range or a weight
found in the given `ranges` is ill-formed
See Also:
`parse(String)`,
`mapEquivalents(java.util.List<java.util.Locale.LanguageRange>, java.util.Map<java.lang.String, java.util.List<java.lang.String>>)`

