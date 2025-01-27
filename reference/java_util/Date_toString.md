#### toString

```
public String toString()
```
Converts this `Date` object to a `String`
of the form:
```

 dow mon dd hh:mm:ss zzz yyyy
```
where:dow is the day of the week (Sun, Mon, Tue, Wed,
Thu, Fri, Sat).mon is the month (Jan, Feb, Mar, Apr, May, Jun,
Jul, Aug, Sep, Oct, Nov, Dec).dd is the day of the month (01 through
31), as two decimal digits.hh is the hour of the day (00 through
23), as two decimal digits.mm is the minute within the hour (00 through
59), as two decimal digits.ss is the second within the minute (00 through
61, as two decimal digits.zzz is the time zone (and may reflect daylight saving
time). Standard time zone abbreviations include those
recognized by the method parse. If time zone
information is not available, then zzz is empty -
that is, it consists of no characters at all.yyyy is the year, as four decimal digits.
Overrides:
`toString` in class `Object`
Returns:
a string representation of this date.
See Also:
`toLocaleString()`,
`toGMTString()`

