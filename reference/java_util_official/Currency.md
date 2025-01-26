

Currency (Java Platform SE 8 )













<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Currency (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":9,"i1":10,"i2":10,"i3":10,"i4":10,"i5":9,"i6":9,"i7":10,"i8":10,"i9":10,"i10":10};
var tabs = {65535:["t0","All Methods"],1:["t1","Static Methods"],2:["t2","Instance Methods"],8:["t4","Concrete Methods"]};
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
java.utilClass Currency
java.lang.Objectjava.util.Currency
All Implemented Interfaces:
Serializable


```
public final class Currency
extends Object
implements Serializable
```
Represents a currency. Currencies are identified by their ISO 4217 currency
codes. Visit the 
ISO web site for more information.The class is designed so that there's never more than one
`Currency` instance for any given currency. Therefore, there's
no public constructor. You obtain a `Currency` instance using
the `getInstance` methods.Users can supersede the Java runtime currency data by means of the system
property `java.util.currency.data`. If this system property is
defined then its value is the location of a properties file, the contents of
which are key/value pairs of the ISO 3166 country codes and the ISO 4217
currency data respectively. The value part consists of three ISO 4217 values
of a currency, i.e., an alphabetic code, a numeric code, and a minor unit.
Those three ISO 4217 values are separated by commas.
The lines which start with '#'s are considered comment lines. An optional UTC
timestamp may be specified per currency entry if users need to specify a
cutover date indicating when the new data comes into effect. The timestamp is
appended to the end of the currency properties and uses a comma as a separator.
If a UTC datestamp is present and valid, the JRE will only use the new currency
properties if the current UTC date is later than the date specified at class
loading time. The format of the timestamp must be of ISO 8601 format :
`'yyyy-MM-dd'T'HH:mm:ss'`. For example,`#Sample currency properties
JP=JPZ,999,0`will supersede the currency data for Japan.`#Sample currency properties with cutover date
JP=JPZ,999,0,2014-01-01T00:00:00`will supersede the currency data for Japan if `Currency` class is loaded after
1st January 2014 00:00:00 GMT.Where syntactically malformed entries are encountered, the entry is ignored
and the remainder of entries in file are processed. For instances where duplicate
country code entries exist, the behavior of the Currency information for that
`Currency` is undefined and the remainder of entries in file are processed.
Since:
1.4
See Also:
Serialized Form

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`static Set<Currency>``getAvailableCurrencies()`
Gets the set of available currencies.`String``getCurrencyCode()`
Gets the ISO 4217 currency code of this currency.`int``getDefaultFractionDigits()`
Gets the default number of fraction digits used with this currency.`String``getDisplayName()`
Gets the name that is suitable for displaying this currency for
the default `DISPLAY` locale.`String``getDisplayName(Locale locale)`
Gets the name that is suitable for displaying this currency for
the specified locale.`static Currency``getInstance(Locale locale)`
Returns the `Currency` instance for the country of the
given locale.`static Currency``getInstance(String currencyCode)`
Returns the `Currency` instance for the given currency code.`int``getNumericCode()`
Returns the ISO 4217 numeric code of this currency.`String``getSymbol()`
Gets the symbol of this currency for the default
`DISPLAY` locale.`String``getSymbol(Locale locale)`
Gets the symbol of this currency for the specified locale.`String``toString()`
Returns the ISO 4217 currency code of this currency.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Method Detail

#### getInstance

```
public static Currency getInstance(String currencyCode)
```
Returns the `Currency` instance for the given currency code.
Parameters:
`currencyCode` - the ISO 4217 code of the currency
Returns:
the `Currency` instance for the given currency code
Throws:
`NullPointerException` - if `currencyCode` is null
`IllegalArgumentException` - if `currencyCode` is not
a supported ISO 4217 code.

#### getInstance

```
public static Currency getInstance(Locale locale)
```
Returns the `Currency` instance for the country of the
given locale. The language and variant components of the locale
are ignored. The result may vary over time, as countries change their
currencies. For example, for the original member countries of the
European Monetary Union, the method returns the old national currencies
until December 31, 2001, and the Euro from January 1, 2002, local time
of the respective countries.The method returns `null` for territories that don't
have a currency, such as Antarctica.
Parameters:
`locale` - the locale for whose country a `Currency`
instance is needed
Returns:
the `Currency` instance for the country of the given
locale, or `null`
Throws:
`NullPointerException` - if `locale` or its country
code is `null`
`IllegalArgumentException` - if the country of the given `locale`
is not a supported ISO 3166 country code.

#### getAvailableCurrencies

```
public static Set<Currency> getAvailableCurrencies()
```
Gets the set of available currencies. The returned set of currencies
contains all of the available currencies, which may include currencies
that represent obsolete ISO 4217 codes. The set can be modified
without affecting the available currencies in the runtime.
Returns:
the set of available currencies. If there is no currency
available in the runtime, the returned set is empty.
Since:
1.7

#### getCurrencyCode

```
public String getCurrencyCode()
```
Gets the ISO 4217 currency code of this currency.
Returns:
the ISO 4217 currency code of this currency.

#### getSymbol

```
public String getSymbol()
```
Gets the symbol of this currency for the default
`DISPLAY` locale.
For example, for the US Dollar, the symbol is "$" if the default
locale is the US, while for other locales it may be "US$". If no
symbol can be determined, the ISO 4217 currency code is returned.This is equivalent to calling
`getSymbol(Locale.getDefault(Locale.Category.DISPLAY))`.
Returns:
the symbol of this currency for the default
`DISPLAY` locale

#### getSymbol

```
public String getSymbol(Locale locale)
```
Gets the symbol of this currency for the specified locale.
For example, for the US Dollar, the symbol is "$" if the specified
locale is the US, while for other locales it may be "US$". If no
symbol can be determined, the ISO 4217 currency code is returned.
Parameters:
`locale` - the locale for which a display name for this currency is
needed
Returns:
the symbol of this currency for the specified locale
Throws:
`NullPointerException` - if `locale` is null

#### getDefaultFractionDigits

```
public int getDefaultFractionDigits()
```
Gets the default number of fraction digits used with this currency.
For example, the default number of fraction digits for the Euro is 2,
while for the Japanese Yen it's 0.
In the case of pseudo-currencies, such as IMF Special Drawing Rights,
-1 is returned.
Returns:
the default number of fraction digits used with this currency

#### getNumericCode

```
public int getNumericCode()
```
Returns the ISO 4217 numeric code of this currency.
Returns:
the ISO 4217 numeric code of this currency
Since:
1.7

#### getDisplayName

```
public String getDisplayName()
```
Gets the name that is suitable for displaying this currency for
the default `DISPLAY` locale.
If there is no suitable display name found
for the default locale, the ISO 4217 currency code is returned.This is equivalent to calling
`getDisplayName(Locale.getDefault(Locale.Category.DISPLAY))`.
Returns:
the display name of this currency for the default
`DISPLAY` locale
Since:
1.7

#### getDisplayName

```
public String getDisplayName(Locale locale)
```
Gets the name that is suitable for displaying this currency for
the specified locale. If there is no suitable display name found
for the specified locale, the ISO 4217 currency code is returned.
Parameters:
`locale` - the locale for which a display name for this currency is
needed
Returns:
the display name of this currency for the specified locale
Throws:
`NullPointerException` - if `locale` is null
Since:
1.7

#### toString

```
public String toString()
```
Returns the ISO 4217 currency code of this currency.
Overrides:
`toString` in class `Object`
Returns:
the ISO 4217 currency code of this currency




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

