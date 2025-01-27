```
public static final class Locale.LanguageRange
extends Object
```
This class expresses a Language Range defined in
RFC 4647 Matching of
Language Tags. A language range is an identifier which is used to
select language tag(s) meeting specific requirements by using the
mechanisms described in Locale
Matching. A list which represents a user's preferences and consists
of language ranges is called a Language Priority List.There are two types of language ranges: basic and extended. In RFC
4647, the syntax of language ranges is expressed in
ABNF as follows:
```

     basic-language-range    = (1*8ALPHA *("-" 1*8alphanum)) / "*"
     extended-language-range = (1*8ALPHA / "*")
                               *("-" (1*8alphanum / "*"))
     alphanum                = ALPHA / DIGIT
 
```
For example, `"en"` (English), `"ja-JP"` (Japanese, Japan),
`"*"` (special language range which matches any language tag) are
basic language ranges, whereas `"*-CH"` (any languages,
Switzerland), `"es-*"` (Spanish, any regions), and
`"zh-Hant-*"` (Traditional Chinese, any regions) are extended
language ranges.
Since:
1.8
See Also:
`Locale.filter(java.util.List<java.util.Locale.LanguageRange>, java.util.Collection<java.util.Locale>, java.util.Locale.FilteringMode)`,
`Locale.filterTags(java.util.List<java.util.Locale.LanguageRange>, java.util.Collection<java.lang.String>, java.util.Locale.FilteringMode)`,
`Locale.lookup(java.util.List<java.util.Locale.LanguageRange>, java.util.Collection<java.util.Locale>)`,
`Locale.lookupTag(java.util.List<java.util.Locale.LanguageRange>, java.util.Collection<java.lang.String>)`
