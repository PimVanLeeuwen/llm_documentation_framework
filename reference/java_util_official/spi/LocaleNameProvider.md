

LocaleNameProvider (Java Platform SE 8 )









<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="LocaleNameProvider (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":6,"i2":10,"i3":6};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"],8:["t4","Concrete Methods"]};
var altColor = "altColor";
var rowColor = "rowColor";
var tableTab = "tableTab";
var activeTableTab = "activeTableTab";

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method




compact1, compact2, compact3
java.util.spiClass LocaleNameProvider
java.lang.Objectjava.util.spi.LocaleServiceProviderjava.util.spi.LocaleNameProvider
```
public abstract class LocaleNameProvider
extends LocaleServiceProvider
```
An abstract class for service providers that
provide localized names for the
`Locale` class.
Since:
1.6

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `LocaleNameProvider()`
Sole constructor.

### Method Summary

All Methods Instance Methods Abstract Methods Concrete Methods Modifier and TypeMethod and Description`abstract String``getDisplayCountry(String countryCode,
Locale locale)`
Returns a localized name for the given 
IETF BCP47 region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.`abstract String``getDisplayLanguage(String languageCode,
Locale locale)`
Returns a localized name for the given 
IETF BCP47 language code and the given locale that is appropriate for
display to the user.`String``getDisplayScript(String scriptCode,
Locale locale)`
Returns a localized name for the given 
IETF BCP47 script code and the given locale that is appropriate for
display to the user.`abstract String``getDisplayVariant(String variant,
Locale locale)`
Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.

### Methods inherited from class java.util.spi.LocaleServiceProvider

`getAvailableLocales, isSupportedLocale`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### LocaleNameProvider

```
protected LocaleNameProvider()
```
Sole constructor. (For invocation by subclass constructors, typically
implicit.)

### Method Detail

#### getDisplayLanguage

```
public abstract String getDisplayLanguage(String languageCode,
                                          Locale locale)
```
Returns a localized name for the given 
IETF BCP47 language code and the given locale that is appropriate for
display to the user.
For example, if `languageCode` is "fr" and `locale`
is en\_US, getDisplayLanguage() will return "French"; if `languageCode`
is "en" and `locale` is fr\_FR, getDisplayLanguage() will return "anglais".
If the name returned cannot be localized according to `locale`,
(say, the provider does not have a Japanese name for Croatian),
this method returns null.
Parameters:
`languageCode` - the language code string in the form of two to eight
lower-case letters between 'a' (U+0061) and 'z' (U+007A)
`locale` - the desired locale
Returns:
the name of the given language code for the specified locale, or null if it's not
available.
Throws:
`NullPointerException` - if `languageCode` or `locale` is null
`IllegalArgumentException` - if `languageCode` is not in the form of
two or three lower-case letters, or `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
See Also:
`Locale.getDisplayLanguage(java.util.Locale)`

#### getDisplayScript

```
public String getDisplayScript(String scriptCode,
                               Locale locale)
```
Returns a localized name for the given 
IETF BCP47 script code and the given locale that is appropriate for
display to the user.
For example, if `scriptCode` is "Latn" and `locale`
is en\_US, getDisplayScript() will return "Latin"; if `scriptCode`
is "Cyrl" and `locale` is fr\_FR, getDisplayScript() will return "cyrillique".
If the name returned cannot be localized according to `locale`,
(say, the provider does not have a Japanese name for Cyrillic),
this method returns null. The default implementation returns null.
Parameters:
`scriptCode` - the four letter script code string in the form of title-case
letters (the first letter is upper-case character between 'A' (U+0041) and
'Z' (U+005A) followed by three lower-case character between 'a' (U+0061)
and 'z' (U+007A)).
`locale` - the desired locale
Returns:
the name of the given script code for the specified locale, or null if it's not
available.
Throws:
`NullPointerException` - if `scriptCode` or `locale` is null
`IllegalArgumentException` - if `scriptCode` is not in the form of
four title case letters, or `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
Since:
1.7
See Also:
`Locale.getDisplayScript(java.util.Locale)`

#### getDisplayCountry

```
public abstract String getDisplayCountry(String countryCode,
                                         Locale locale)
```
Returns a localized name for the given 
IETF BCP47 region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.
For example, if `countryCode` is "FR" and `locale`
is en\_US, getDisplayCountry() will return "France"; if `countryCode`
is "US" and `locale` is fr\_FR, getDisplayCountry() will return "Etats-Unis".
If the name returned cannot be localized according to `locale`,
(say, the provider does not have a Japanese name for Croatia),
this method returns null.
Parameters:
`countryCode` - the country(region) code string in the form of two
upper-case letters between 'A' (U+0041) and 'Z' (U+005A) or the UN M.49 area code
in the form of three digit letters between '0' (U+0030) and '9' (U+0039).
`locale` - the desired locale
Returns:
the name of the given country code for the specified locale, or null if it's not
available.
Throws:
`NullPointerException` - if `countryCode` or `locale` is null
`IllegalArgumentException` - if `countryCode` is not in the form of
two upper-case letters or three digit letters, or `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
See Also:
`Locale.getDisplayCountry(java.util.Locale)`

#### getDisplayVariant

```
public abstract String getDisplayVariant(String variant,
                                         Locale locale)
```
Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.
If the name returned cannot be localized according to `locale`,
this method returns null.
Parameters:
`variant` - the variant string
`locale` - the desired locale
Returns:
the name of the given variant string for the specified locale, or null if it's not
available.
Throws:
`NullPointerException` - if `variant` or `locale` is null
`IllegalArgumentException` - if `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
See Also:
`Locale.getDisplayVariant(java.util.Locale)`




Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method


 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

