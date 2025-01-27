#### mapEquivalents

```
public static List<Locale.LanguageRange> mapEquivalents(List<Locale.LanguageRange> priorityList,
                                                        Map<String,List<String>> map)
```
Generates a new customized Language Priority List using the given
`priorityList` and `map`. If the given `map` is
empty, this method returns a copy of the given `priorityList`.In the map, a key represents a language range whereas a value is
a list of equivalents of it. `'*'` cannot be used in the map.
Each equivalent language range has the same weight value as its
original language range.
```

  An example of map:
    Key                            Value
      "zh" (Chinese)                 "zh",
                                     "zh-Hans"(Simplified Chinese)
      "zh-HK" (Chinese, Hong Kong)   "zh-HK"
      "zh-TW" (Chinese, Taiwan)      "zh-TW"
 
```
The customization is performed after modification using the IANA
Language Subtag Registry.For example, if a user's Language Priority List consists of five
language ranges (`"zh"`, `"zh-CN"`, `"en"`,
`"zh-TW"`, and `"zh-HK"`), the newly generated Language
Priority List which is customized using the above map example will
consists of `"zh"`, `"zh-Hans"`, `"zh-CN"`,
`"zh-Hans-CN"`, `"en"`, `"zh-TW"`, and
`"zh-HK"`.`"zh-HK"` and `"zh-TW"` aren't converted to
`"zh-Hans-HK"` nor `"zh-Hans-TW"` even if they are
included in the Language Priority List. In this example, mapping
is used to clearly distinguish Simplified Chinese and Traditional
Chinese.If the `"zh"`-to-`"zh"` mapping isn't included in the
map, a simple replacement will be performed and the customized list
won't include `"zh"` and `"zh-CN"`.
Parameters:
`priorityList` - user's Language Priority List
`map` - a map containing information to customize language ranges
Returns:
a new Language Priority List with customization. The list is
modifiable.
Throws:
`NullPointerException` - if `priorityList` is `null`
See Also:
`parse(String, Map)`

