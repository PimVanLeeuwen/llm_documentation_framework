

java.util.spi (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="java.util.spi (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->




compact3Package java.util.spi
Service provider classes for the classes in the java.util package.
See: Description

Interface Summary InterfaceDescriptionResourceBundleControlProviderAn interface for service providers that provide implementations of `ResourceBundle.Control`.

Class Summary ClassDescriptionCalendarDataProviderAn abstract class for service providers that provide locale-dependent `Calendar` parameters.CalendarNameProviderAn abstract class for service providers that provide localized string
representations (display names) of `Calendar` field values.CurrencyNameProviderAn abstract class for service providers that
provide localized currency symbols and display names for the
`Currency` class.LocaleNameProviderAn abstract class for service providers that
provide localized names for the
`Locale` class.LocaleServiceProvider
This is the super class of all the locale sensitive service provider
interfaces (SPIs).TimeZoneNameProviderAn abstract class for service providers that
provide localized time zone names for the
`TimeZone` class.

Package java.util.spi DescriptionService provider classes for the classes in the java.util package.

Since:
1.6



Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->



 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

