

CalendarDataProvider (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="CalendarDataProvider (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":6};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"]};
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
java.util.spiClass CalendarDataProvider
java.lang.Objectjava.util.spi.LocaleServiceProviderjava.util.spi.CalendarDataProvider
```
public abstract class CalendarDataProvider
extends LocaleServiceProvider
```
An abstract class for service providers that provide locale-dependent `Calendar` parameters.
Since:
1.8
See Also:
`CalendarNameProvider`

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `CalendarDataProvider()`
Sole constructor.

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`abstract int``getFirstDayOfWeek(Locale locale)`
Returns the first day of a week in the given `locale`.`abstract int``getMinimalDaysInFirstWeek(Locale locale)`
Returns the minimal number of days required in the first week of a
year.

### Methods inherited from class java.util.spi.LocaleServiceProvider

`getAvailableLocales, isSupportedLocale`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### CalendarDataProvider

```
protected CalendarDataProvider()
```
Sole constructor. (For invocation by subclass constructors, typically
implicit.)

### Method Detail

#### getFirstDayOfWeek

```
public abstract int getFirstDayOfWeek(Locale locale)
```
Returns the first day of a week in the given `locale`. This
information is required by `Calendar` to support operations on the
week-related calendar fields.
Parameters:
`locale` - the desired locale
Returns:
the first day of a week; one of `Calendar.SUNDAY` ..
`Calendar.SATURDAY`,
or 0 if the value isn't available for the `locale`
Throws:
`NullPointerException` - if `locale` is `null`.
See Also:
`Calendar.getFirstDayOfWeek()`,
First Week

#### getMinimalDaysInFirstWeek

```
public abstract int getMinimalDaysInFirstWeek(Locale locale)
```
Returns the minimal number of days required in the first week of a
year. This information is required by `Calendar` to determine the
first week of a year. Refer to the description of  how `Calendar` determines
the first week.
Parameters:
`locale` - the desired locale
Returns:
the minimal number of days of the first week,
or 0 if the value isn't available for the `locale`
Throws:
`NullPointerException` - if `locale` is `null`.
See Also:
`Calendar.getMinimalDaysInFirstWeek()`




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

