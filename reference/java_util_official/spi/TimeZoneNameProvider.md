

TimeZoneNameProvider (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="TimeZoneNameProvider (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":10};
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
java.util.spiClass TimeZoneNameProvider
java.lang.Objectjava.util.spi.LocaleServiceProviderjava.util.spi.TimeZoneNameProvider
```
public abstract class TimeZoneNameProvider
extends LocaleServiceProvider
```
An abstract class for service providers that
provide localized time zone names for the
`TimeZone` class.
The localized time zone names available from the implementations of
this class are also the source for the
`DateFormatSymbols.getZoneStrings()` method.
Since:
1.6

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `TimeZoneNameProvider()`
Sole constructor.

### Method Summary

All Methods Instance Methods Abstract Methods Concrete Methods Modifier and TypeMethod and Description`abstract String``getDisplayName(String ID,
boolean daylight,
int style,
Locale locale)`
Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale.`String``getGenericDisplayName(String ID,
int style,
Locale locale)`
Returns a generic name for the given time zone `ID` that's suitable
for presentation to the user in the specified `locale`.

### Methods inherited from class java.util.spi.LocaleServiceProvider

`getAvailableLocales, isSupportedLocale`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### TimeZoneNameProvider

```
protected TimeZoneNameProvider()
```
Sole constructor. (For invocation by subclass constructors, typically
implicit.)

### Method Detail

#### getDisplayName

```
public abstract String getDisplayName(String ID,
                                      boolean daylight,
                                      int style,
                                      Locale locale)
```
Returns a name for the given time zone ID that's suitable for
presentation to the user in the specified locale. The given time
zone ID is "GMT" or one of the names defined using "Zone" entries
in the "tz database", a public domain time zone database at
ftp://elsie.nci.nih.gov/pub/.
The data of this database is contained in a file whose name starts with
"tzdata", and the specification of the data format is part of the zic.8
man page, which is contained in a file whose name starts with "tzcode".If `daylight` is true, the method should return a name
appropriate for daylight saving time even if the specified time zone
has not observed daylight saving time in the past.
Parameters:
`ID` - a time zone ID string
`daylight` - if true, return the daylight saving name.
`style` - either `TimeZone.LONG` or
`TimeZone.SHORT`
`locale` - the desired locale
Returns:
the human-readable name of the given time zone in the
given locale, or null if it's not available.
Throws:
`IllegalArgumentException` - if `style` is invalid,
or `locale` isn't one of the locales returned from
`getAvailableLocales()`.
`NullPointerException` - if `ID` or `locale`
is null
See Also:
`TimeZone.getDisplayName(boolean, int, java.util.Locale)`

#### getGenericDisplayName

```
public String getGenericDisplayName(String ID,
                                    int style,
                                    Locale locale)
```
Returns a generic name for the given time zone `ID` that's suitable
for presentation to the user in the specified `locale`. Generic
time zone names are neutral from standard time and daylight saving
time. For example, "PT" is the short generic name of time zone ID `America/Los_Angeles`, while its short standard time and daylight saving
time names are "PST" and "PDT", respectively. Refer to
`getDisplayName`
for valid time zone IDs.The default implementation of this method returns `null`.
Parameters:
`ID` - a time zone ID string
`style` - either `TimeZone.LONG` or
`TimeZone.SHORT`
`locale` - the desired locale
Returns:
the human-readable generic name of the given time zone in the
given locale, or `null` if it's not available.
Throws:
`IllegalArgumentException` - if `style` is invalid,
or `locale` isn't one of the locales returned from
`getAvailableLocales()`.
`NullPointerException` - if `ID` or `locale`
is `null`
Since:
1.8




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

