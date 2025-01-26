

CalendarNameProvider (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="CalendarNameProvider (Java Platform SE 8 )";
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
java.util.spiClass CalendarNameProvider
java.lang.Objectjava.util.spi.LocaleServiceProviderjava.util.spi.CalendarNameProvider
```
public abstract class CalendarNameProvider
extends LocaleServiceProvider
```
An abstract class for service providers that provide localized string
representations (display names) of `Calendar` field values.Calendar TypesCalendar types are used to specify calendar systems for which the `getDisplayName` and `getDisplayNames` methods provide
calendar field value names. See `Calendar.getCalendarType()` for details.Calendar FieldsCalendar fields are specified with the constants defined in `Calendar`. The following are calendar-common fields and their values to be
supported for each calendar system.

FieldValueDescription`Calendar.MONTH``Calendar.JANUARY` to `Calendar.UNDECIMBER`Month numbering is 0-based (e.g., 0 - January, ..., 11 -
December). Some calendar systems have 13 months. Month
names need to be supported in both the formatting and
stand-alone forms if required by the supported locales. If there's
no distinction in the two forms, the same names should be returned
in both of the forms.`Calendar.DAY_OF_WEEK``Calendar.SUNDAY` to `Calendar.SATURDAY`Day-of-week numbering is 1-based starting from Sunday (i.e., 1 - Sunday,
..., 7 - Saturday).`Calendar.AM_PM``Calendar.AM` to `Calendar.PM`0 - AM, 1 - PM
The following are calendar-specific fields and their values to be supported.

Calendar TypeFieldValueDescription`"gregory"``Calendar.ERA`0`GregorianCalendar.BC` (BCE)1`GregorianCalendar.AD` (CE)`"buddhist"``Calendar.ERA`0BC (BCE)1B.E. (Buddhist Era)`"japanese"``Calendar.ERA`0Seireki (Before Meiji)1Meiji2Taisho3Showa4Heisei`Calendar.YEAR`1the first year in each era. It should be returned when a long
style (`Calendar.LONG_FORMAT` or `Calendar.LONG_STANDALONE`) is
specified. See also the 
Year representation in `SimpleDateFormat`.`"roc"``Calendar.ERA`0Before R.O.C.1R.O.C.`"islamic"``Calendar.ERA`0Before AH1Anno Hijrah (AH)
Calendar field value names for `"gregory"` must be consistent with
the date-time symbols provided by `DateFormatSymbolsProvider`.Time zone names are supported by `TimeZoneNameProvider`.
Since:
1.8
See Also:
`CalendarDataProvider`,
`Locale.getUnicodeLocaleType(String)`

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `CalendarNameProvider()`
Sole constructor.

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`abstract String``getDisplayName(String calendarType,
int field,
int value,
int style,
Locale locale)`
Returns the string representation (display name) of the calendar
`field value` in the given `style` and
`locale`.`abstract Map<String,Integer>``getDisplayNames(String calendarType,
int field,
int style,
Locale locale)`
Returns a `Map` containing all string representations (display
names) of the `Calendar` `field` in the given `style`
and `locale` and their corresponding field values.

### Methods inherited from class java.util.spi.LocaleServiceProvider

`getAvailableLocales, isSupportedLocale`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### CalendarNameProvider

```
protected CalendarNameProvider()
```
Sole constructor. (For invocation by subclass constructors, typically
implicit.)

### Method Detail

#### getDisplayName

```
public abstract String getDisplayName(String calendarType,
                                      int field,
                                      int value,
                                      int style,
                                      Locale locale)
```
Returns the string representation (display name) of the calendar
`field value` in the given `style` and
`locale`. If no string representation is
applicable, `null` is returned.`field` is a `Calendar` field index, such as `Calendar.MONTH`. The time zone fields, `Calendar.ZONE_OFFSET` and
`Calendar.DST_OFFSET`, are not supported by this
method. `null` must be returned if any time zone fields are
specified.`value` is the numeric representation of the `field` value.
For example, if `field` is `Calendar.DAY_OF_WEEK`, the valid
values are `Calendar.SUNDAY` to `Calendar.SATURDAY`
(inclusive).`style` gives the style of the string representation. It is one
of `Calendar.SHORT_FORMAT` (`SHORT`),
`Calendar.SHORT_STANDALONE`, `Calendar.LONG_FORMAT`
(`LONG`), `Calendar.LONG_STANDALONE`,
`Calendar.NARROW_FORMAT`, or `Calendar.NARROW_STANDALONE`.For example, the following call will return `"Sunday"`.
```

 getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
                Calendar.LONG_STANDALONE, Locale.ENGLISH);
 
```

Parameters:
`calendarType` - the calendar type. (Any calendar type given by `locale`
is ignored.)
`field` - the `Calendar` field index,
such as `Calendar.DAY_OF_WEEK`
`value` - the value of the `Calendar field`,
such as `Calendar.MONDAY`
`style` - the string representation style: one of `Calendar.SHORT_FORMAT` (`SHORT`),
`Calendar.SHORT_STANDALONE`, `Calendar.LONG_FORMAT` (`LONG`),
`Calendar.LONG_STANDALONE`,
`Calendar.NARROW_FORMAT`,
or `Calendar.NARROW_STANDALONE`
`locale` - the desired locale
Returns:
the string representation of the `field value`, or `null` if the string representation is not applicable or
the given calendar type is unknown
Throws:
`IllegalArgumentException` - if `field` or `style` is invalid
`NullPointerException` - if `locale` is `null`
See Also:
`TimeZoneNameProvider`,
`Calendar.get(int)`,
`Calendar.getDisplayName(int, int, Locale)`

#### getDisplayNames

```
public abstract Map<String,Integer> getDisplayNames(String calendarType,
                                                    int field,
                                                    int style,
                                                    Locale locale)
```
Returns a `Map` containing all string representations (display
names) of the `Calendar` `field` in the given `style`
and `locale` and their corresponding field values.`field` is a `Calendar` field index, such as `Calendar.MONTH`. The time zone fields, `Calendar.ZONE_OFFSET` and
`Calendar.DST_OFFSET`, are not supported by this
method. `null` must be returned if any time zone fields are specified.`style` gives the style of the string representation. It must be
one of `Calendar.ALL_STYLES`, `Calendar.SHORT_FORMAT` (`SHORT`), `Calendar.SHORT_STANDALONE`, `Calendar.LONG_FORMAT` (`LONG`), `Calendar.LONG_STANDALONE`, `Calendar.NARROW_FORMAT`, or
`Calendar.NARROW_STANDALONE`. Note that narrow names may
not be unique due to use of single characters, such as "S" for Sunday
and Saturday, and that no narrow names are included in that case.For example, the following call will return a `Map` containing
`"January"` to `Calendar.JANUARY`, `"Jan"` to `Calendar.JANUARY`, `"February"` to `Calendar.FEBRUARY`,
`"Feb"` to `Calendar.FEBRUARY`, and so on.
```

 getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
 
```

Parameters:
`calendarType` - the calendar type. (Any calendar type given by `locale`
is ignored.)
`field` - the calendar field for which the display names are returned
`style` - the style applied to the display names; one of
`Calendar.ALL_STYLES`, `Calendar.SHORT_FORMAT`
(`SHORT`), `Calendar.SHORT_STANDALONE`, `Calendar.LONG_FORMAT`
(`LONG`), `Calendar.LONG_STANDALONE`,
`Calendar.NARROW_FORMAT`,
or `Calendar.NARROW_STANDALONE`
`locale` - the desired locale
Returns:
a `Map` containing all display names of `field` in
`style` and `locale` and their `field` values,
or `null` if no display names are defined for `field`
Throws:
`NullPointerException` - if `locale` is `null`
See Also:
`Calendar.getDisplayNames(int, int, Locale)`




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

