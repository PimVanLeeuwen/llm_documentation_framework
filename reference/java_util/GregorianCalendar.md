```
public class GregorianCalendar
extends Calendar
```
`GregorianCalendar` is a concrete subclass of
`Calendar` and provides the standard calendar system
used by most of the world.`GregorianCalendar` is a hybrid calendar that
supports both the Julian and Gregorian calendar systems with the
support of a single discontinuity, which corresponds by default to
the Gregorian date when the Gregorian calendar was instituted
(October 15, 1582 in some countries, later in others). The cutover
date may be changed by the caller by calling `setGregorianChange()`.Historically, in those countries which adopted the Gregorian calendar first,
October 4, 1582 (Julian) was thus followed by October 15, 1582 (Gregorian). This calendar models
this correctly. Before the Gregorian cutover, `GregorianCalendar`
implements the Julian calendar. The only difference between the Gregorian
and the Julian calendar is the leap year rule. The Julian calendar specifies
leap years every four years, whereas the Gregorian calendar omits century
years which are not divisible by 400.`GregorianCalendar` implements proleptic Gregorian and
Julian calendars. That is, dates are computed by extrapolating the current
rules indefinitely far backward and forward in time. As a result,
`GregorianCalendar` may be used for all years to generate
meaningful and consistent results. However, dates obtained using
`GregorianCalendar` are historically accurate only from March 1, 4
AD onward, when modern Julian calendar rules were adopted. Before this date,
leap year rules were applied irregularly, and before 45 BC the Julian
calendar did not even exist.Prior to the institution of the Gregorian calendar, New Year's Day was
March 25. To avoid confusion, this calendar always uses January 1. A manual
adjustment may be made if desired for dates that are prior to the Gregorian
changeover and which fall between January 1 and March 24.