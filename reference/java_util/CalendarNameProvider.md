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
