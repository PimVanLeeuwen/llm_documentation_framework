

Locale.FilteringMode (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Locale.FilteringMode (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":9,"i1":9};
var tabs = {65535:["t0","All Methods"],1:["t1","Static Methods"],8:["t4","Concrete Methods"]};
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


Summary:Nested |Enum Constants |Field |MethodDetail:Enum Constants |Field |Method




compact1, compact2, compact3
java.utilEnum Locale.FilteringMode
java.lang.Objectjava.lang.Enum<Locale.FilteringMode>java.util.Locale.FilteringMode
All Implemented Interfaces:
Serializable, Comparable<Locale.FilteringMode>

Enclosing class:
Locale


```
public static enum Locale.FilteringMode
extends Enum<Locale.FilteringMode>
```
This enum provides constants to select a filtering mode for locale
matching. Refer to RFC 4647
Matching of Language Tags for details.As an example, think of two Language Priority Lists each of which
includes only one language range and a set of following language tags:
```

    de (German)
    de-DE (German, Germany)
    de-Deva (German, in Devanagari script)
    de-Deva-DE (German, in Devanagari script, Germany)
    de-DE-1996 (German, Germany, orthography of 1996)
    de-Latn-DE (German, in Latin script, Germany)
    de-Latn-DE-1996 (German, in Latin script, Germany, orthography of 1996)
 
```
The filtering method will behave as follows:

Filtering ModeLanguage Priority List: `"de-DE"`Language Priority List: `"de-*-DE"``AUTOSELECT_FILTERING`Performs basic filtering and returns `"de-DE"` and
`"de-DE-1996"`.Performs extended filtering and returns `"de-DE"`,
`"de-Deva-DE"`, `"de-DE-1996"`, `"de-Latn-DE"`, and
`"de-Latn-DE-1996"`.`EXTENDED_FILTERING`Performs extended filtering and returns `"de-DE"`,
`"de-Deva-DE"`, `"de-DE-1996"`, `"de-Latn-DE"`, and
`"de-Latn-DE-1996"`.Same as above.`IGNORE_EXTENDED_RANGES`Performs basic filtering and returns `"de-DE"` and
`"de-DE-1996"`.Performs basic filtering and returns `null` because
nothing matches.`MAP_EXTENDED_RANGES`Same as above.Performs basic filtering and returns `"de-DE"` and
`"de-DE-1996"` because `"de-*-DE"` is mapped to
`"de-DE"`.`REJECT_EXTENDED_RANGES`Same as above.Throws `IllegalArgumentException` because `"de-*-DE"` is
not a valid basic language range.

Since:
1.8
See Also:
`Locale.filter(List, Collection, FilteringMode)`,
`Locale.filterTags(List, Collection, FilteringMode)`

### Enum Constant Summary

Enum Constants Enum Constant and Description`AUTOSELECT_FILTERING`
Specifies automatic filtering mode based on the given Language
Priority List consisting of language ranges.`EXTENDED_FILTERING`
Specifies extended filtering.`IGNORE_EXTENDED_RANGES`
Specifies basic filtering: Note that any extended language ranges
included in the given Language Priority List are ignored.`MAP_EXTENDED_RANGES`
Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, they are mapped to the
basic language range.`REJECT_EXTENDED_RANGES`
Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, the list is rejected
and the filtering method throws `IllegalArgumentException`.

### Method Summary

All Methods Static Methods Concrete Methods Modifier and TypeMethod and Description`static Locale.FilteringMode``valueOf(String name)`
Returns the enum constant of this type with the specified name.`static Locale.FilteringMode[]``values()`
Returns an array containing the constants of this enum type, in
the order they are declared.

### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

### Enum Constant Detail

#### AUTOSELECT\_FILTERING

```
public static final Locale.FilteringMode AUTOSELECT_FILTERING
```
Specifies automatic filtering mode based on the given Language
Priority List consisting of language ranges. If all of the ranges
are basic, basic filtering is selected. Otherwise, extended
filtering is selected.

#### EXTENDED\_FILTERING

```
public static final Locale.FilteringMode EXTENDED_FILTERING
```
Specifies extended filtering.

#### IGNORE\_EXTENDED\_RANGES

```
public static final Locale.FilteringMode IGNORE_EXTENDED_RANGES
```
Specifies basic filtering: Note that any extended language ranges
included in the given Language Priority List are ignored.

#### MAP\_EXTENDED\_RANGES

```
public static final Locale.FilteringMode MAP_EXTENDED_RANGES
```
Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, they are mapped to the
basic language range. Specifically, a language range starting with a
subtag `"*"` is treated as a language range `"*"`. For
example, `"*-US"` is treated as `"*"`. If `"*"` is
not the first subtag, `"*"` and extra `"-"` are removed.
For example, `"ja-*-JP"` is mapped to `"ja-JP"`.

#### REJECT\_EXTENDED\_RANGES

```
public static final Locale.FilteringMode REJECT_EXTENDED_RANGES
```
Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, the list is rejected
and the filtering method throws `IllegalArgumentException`.

### Method Detail

#### values

```
public static Locale.FilteringMode[] values()
```
Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:
```

for (Locale.FilteringMode c : Locale.FilteringMode.values())
    System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared

#### valueOf

```
public static Locale.FilteringMode valueOf(String name)
```
Returns the enum constant of this type with the specified name.
The string must match exactly an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)
Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`IllegalArgumentException` - if this enum type has no constant with the specified name
`NullPointerException` - if the argument is null




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


Summary:Nested |Enum Constants |Field |MethodDetail:Enum Constants |Field |Method


 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

