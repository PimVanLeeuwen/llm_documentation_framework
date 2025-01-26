

CurrencyNameProvider (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="CurrencyNameProvider (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":6};
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
java.util.spiClass CurrencyNameProvider
java.lang.Objectjava.util.spi.LocaleServiceProviderjava.util.spi.CurrencyNameProvider
```
public abstract class CurrencyNameProvider
extends LocaleServiceProvider
```
An abstract class for service providers that
provide localized currency symbols and display names for the
`Currency` class.
Note that currency symbols are considered names when determining
behaviors described in the
`LocaleServiceProvider`
specification.
Since:
1.6

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `CurrencyNameProvider()`
Sole constructor.

### Method Summary

All Methods Instance Methods Abstract Methods Concrete Methods Modifier and TypeMethod and Description`String``getDisplayName(String currencyCode,
Locale locale)`
Returns a name for the currency that is appropriate for display to the
user.`abstract String``getSymbol(String currencyCode,
Locale locale)`
Gets the symbol of the given currency code for the specified locale.

### Methods inherited from class java.util.spi.LocaleServiceProvider

`getAvailableLocales, isSupportedLocale`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### CurrencyNameProvider

```
protected CurrencyNameProvider()
```
Sole constructor. (For invocation by subclass constructors, typically
implicit.)

### Method Detail

#### getSymbol

```
public abstract String getSymbol(String currencyCode,
                                 Locale locale)
```
Gets the symbol of the given currency code for the specified locale.
For example, for "USD" (US Dollar), the symbol is "$" if the specified
locale is the US, while for other locales it may be "US$". If no
symbol can be determined, null should be returned.
Parameters:
`currencyCode` - the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
`locale` - the desired locale
Returns:
the symbol of the given currency code for the specified locale, or null if
the symbol is not available for the locale
Throws:
`NullPointerException` - if `currencyCode` or
`locale` is null
`IllegalArgumentException` - if `currencyCode` is not in
the form of three upper-case letters, or `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
See Also:
`Currency.getSymbol(java.util.Locale)`

#### getDisplayName

```
public String getDisplayName(String currencyCode,
                             Locale locale)
```
Returns a name for the currency that is appropriate for display to the
user. The default implementation returns null.
Parameters:
`currencyCode` - the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
`locale` - the desired locale
Returns:
the name for the currency that is appropriate for display to the
user, or null if the name is not available for the locale
Throws:
`IllegalArgumentException` - if `currencyCode` is not in
the form of three upper-case letters, or `locale` isn't
one of the locales returned from
`getAvailableLocales()`.
`NullPointerException` - if `currencyCode` or
`locale` is `null`
Since:
1.7




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

