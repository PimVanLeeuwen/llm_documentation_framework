#### forLanguageTag

```
public static Locale forLanguageTag(String languageTag)
```
Returns a locale for the specified IETF BCP 47 language tag string.If the specified language tag contains any ill-formed subtags,
the first such subtag and all following subtags are ignored. Compare
to `Locale.Builder.setLanguageTag(java.lang.String)` which throws an exception
in this case.The following conversions are performed:The language code "und" is mapped to language "".The language codes "he", "yi", and "id" are mapped to "iw",
"ji", and "in" respectively. (This is the same canonicalization
that's done in Locale's constructors.)The portion of a private use subtag prefixed by "lvariant",
if any, is removed and appended to the variant field in the
result locale (without case normalization). If it is then
empty, the private use subtag is discarded:
```

     Locale loc;
     loc = Locale.forLanguageTag("en-US-x-lvariant-POSIX");
     loc.getVariant(); // returns "POSIX"
     loc.getExtension('x'); // returns null

     loc = Locale.forLanguageTag("de-POSIX-x-URP-lvariant-Abc-Def");
     loc.getVariant(); // returns "POSIX_Abc_Def"
     loc.getExtension('x'); // returns "urp"
 
```
When the languageTag argument contains an extlang subtag,
the first such subtag is used as the language, and the primary
language subtag and other extlang subtags are ignored:
```

     Locale.forLanguageTag("ar-aao").getLanguage(); // returns "aao"
     Locale.forLanguageTag("en-abc-def-us").toString(); // returns "abc_US"
 
```
Case is normalized except for variant tags, which are left
unchanged. Language is normalized to lower case, script to
title case, country to upper case, and extensions to lower
case.If, after processing, the locale would exactly match either
ja\_JP\_JP or th\_TH\_TH with no extensions, the appropriate
extensions are added as though the constructor had been called:
```

    Locale.forLanguageTag("ja-JP-x-lvariant-JP").toLanguageTag();
    // returns "ja-JP-u-ca-japanese-x-lvariant-JP"
    Locale.forLanguageTag("th-TH-x-lvariant-TH").toLanguageTag();
    // returns "th-TH-u-nu-thai-x-lvariant-TH"
 
```
This implements the 'Language-Tag' production of BCP47, and
so supports grandfathered (regular and irregular) as well as
private use language tags. Stand alone private use tags are
represented as empty language and extension 'x-whatever',
and grandfathered tags are converted to their canonical replacements
where they exist.Grandfathered tags with canonical replacements are as follows:

grandfathered tagmodern replacementart-lojbanjboi-amiamii-bnnbnni-hakhaki-klingontlhi-luxlbi-navajonvi-pwnpwni-taotaoi-taytayi-tsutsuno-boknbno-nynnnsgn-BE-FRsfbsgn-BE-NLvgtsgn-CH-DEsggzh-guoyucmnzh-hakkahakzh-min-nannanzh-xianghsn
Grandfathered tags with no modern replacement will be
converted as follows:

grandfathered tagconverts tocel-gaulishxtg-x-cel-gaulishen-GB-oeden-GB-x-oedi-defaulten-x-i-defaulti-enochianund-x-i-enochiani-mingosee-x-i-mingozh-minnan-x-zh-min
For a list of all grandfathered tags, see the
IANA Language Subtag Registry (search for "Type: grandfathered").Note: there is no guarantee that `toLanguageTag`
and `forLanguageTag` will round-trip.
Parameters:
`languageTag` - the language tag
Returns:
The locale that best represents the language tag.
Throws:
`NullPointerException` - if `languageTag` is `null`
Since:
1.7
See Also:
`toLanguageTag()`,
`Locale.Builder.setLanguageTag(String)`

