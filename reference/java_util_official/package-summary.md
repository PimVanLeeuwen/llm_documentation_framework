

java.util (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="java.util (Java Platform SE 8 )";
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




Package java.util
Contains the collections framework, legacy collection classes, event model,
date and time facilities, internationalization, and miscellaneous utility
classes (a string tokenizer, a random-number generator, and a bit array).
See: Description

Interface Summary InterfaceDescriptionCollection<E>The root interface in the collection hierarchy.Comparator<T>A comparison function, which imposes a total ordering on some
collection of objects.Deque<E>A linear collection that supports element insertion and removal at
both ends.Enumeration<E>An object that implements the Enumeration interface generates a
series of elements, one at a time.EventListenerA tagging interface that all event listener interfaces must extend.FormattableThe Formattable interface must be implemented by any class that
needs to perform custom formatting using the 's' conversion
specifier of `Formatter`.Iterator<E>An iterator over a collection.List<E>An ordered collection (also known as a sequence).ListIterator<E>An iterator for lists that allows the programmer
to traverse the list in either direction, modify
the list during iteration, and obtain the iterator's
current position in the list.Map<K,V>An object that maps keys to values.Map.Entry<K,V>A map entry (key-value pair).NavigableMap<K,V>A `SortedMap` extended with navigation methods returning the
closest matches for given search targets.NavigableSet<E>A `SortedSet` extended with navigation methods reporting
closest matches for given search targets.ObserverA class can implement the `Observer` interface when it
wants to be informed of changes in observable objects.PrimitiveIterator<T,T\_CONS>A base type for primitive specializations of `Iterator`.PrimitiveIterator.OfDoubleAn Iterator specialized for `double` values.PrimitiveIterator.OfIntAn Iterator specialized for `int` values.PrimitiveIterator.OfLongAn Iterator specialized for `long` values.Queue<E>A collection designed for holding elements prior to processing.RandomAccessMarker interface used by List implementations to indicate that
they support fast (generally constant time) random access.Set<E>A collection that contains no duplicate elements.SortedMap<K,V>A `Map` that further provides a total ordering on its keys.SortedSet<E>A `Set` that further provides a total ordering on its elements.Spliterator<T>An object for traversing and partitioning elements of a source.Spliterator.OfDoubleA Spliterator specialized for `double` values.Spliterator.OfIntA Spliterator specialized for `int` values.Spliterator.OfLongA Spliterator specialized for `long` values.Spliterator.OfPrimitive<T,T\_CONS,T\_SPLITR extends Spliterator.OfPrimitive<T,T\_CONS,T\_SPLITR>>A Spliterator specialized for primitive values.

Class Summary ClassDescriptionAbstractCollection<E>This class provides a skeletal implementation of the Collection
interface, to minimize the effort required to implement this interface.AbstractList<E>This class provides a skeletal implementation of the `List`
interface to minimize the effort required to implement this interface
backed by a "random access" data store (such as an array).AbstractMap<K,V>This class provides a skeletal implementation of the Map
interface, to minimize the effort required to implement this interface.AbstractMap.SimpleEntry<K,V>An Entry maintaining a key and a value.AbstractMap.SimpleImmutableEntry<K,V>An Entry maintaining an immutable key and value.AbstractQueue<E>This class provides skeletal implementations of some `Queue`
operations.AbstractSequentialList<E>This class provides a skeletal implementation of the List
interface to minimize the effort required to implement this interface
backed by a "sequential access" data store (such as a linked list).AbstractSet<E>This class provides a skeletal implementation of the Set
interface to minimize the effort required to implement this
interface.ArrayDeque<E>Resizable-array implementation of the `Deque` interface.ArrayList<E>Resizable-array implementation of the List interface.ArraysThis class contains various methods for manipulating arrays (such as
sorting and searching).Base64This class consists exclusively of static methods for obtaining
encoders and decoders for the Base64 encoding scheme.Base64.DecoderThis class implements a decoder for decoding byte data using the
Base64 encoding scheme as specified in RFC 4648 and RFC 2045.Base64.EncoderThis class implements an encoder for encoding byte data using
the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.BitSetThis class implements a vector of bits that grows as needed.CalendarThe `Calendar` class is an abstract class that provides methods
for converting between a specific instant in time and a set of `calendar fields` such as `YEAR`, `MONTH`,
`DAY_OF_MONTH`, `HOUR`, and so on, and for
manipulating the calendar fields, such as getting the date of the next
week.Calendar.Builder`Calendar.Builder` is used for creating a `Calendar` from
various date-time parameters.CollectionsThis class consists exclusively of static methods that operate on or return
collections.CurrencyRepresents a currency.DateThe class `Date` represents a specific instant
in time, with millisecond precision.Dictionary<K,V>The `Dictionary` class is the abstract parent of any
class, such as `Hashtable`, which maps keys to values.DoubleSummaryStatisticsA state object for collecting statistics such as count, min, max, sum, and
average.EnumMap<K extends Enum<K>,V>A specialized `Map` implementation for use with enum type keys.EnumSet<E extends Enum<E>>A specialized `Set` implementation for use with enum types.EventListenerProxy<T extends EventListener>An abstract wrapper class for an `EventListener` class
which associates a set of additional parameters with the listener.EventObject
The root class from which all event state objects shall be derived.FormattableFlagsFomattableFlags are passed to the `Formattable.formatTo()` method and modify the output format for Formattables.FormatterAn interpreter for printf-style format strings.GregorianCalendar`GregorianCalendar` is a concrete subclass of
`Calendar` and provides the standard calendar system
used by most of the world.HashMap<K,V>Hash table based implementation of the Map interface.HashSet<E>This class implements the Set interface, backed by a hash table
(actually a HashMap instance).Hashtable<K,V>This class implements a hash table, which maps keys to values.IdentityHashMap<K,V>This class implements the Map interface with a hash table, using
reference-equality in place of object-equality when comparing keys (and
values).IntSummaryStatisticsA state object for collecting statistics such as count, min, max, sum, and
average.LinkedHashMap<K,V>Hash table and linked list implementation of the Map interface,
with predictable iteration order.LinkedHashSet<E>Hash table and linked list implementation of the Set interface,
with predictable iteration order.LinkedList<E>Doubly-linked list implementation of the `List` and `Deque`
interfaces.ListResourceBundle`ListResourceBundle` is an abstract subclass of
`ResourceBundle` that manages resources for a locale
in a convenient and easy to use list.LocaleA `Locale` object represents a specific geographical, political,
or cultural region.Locale.Builder`Builder` is used to build instances of `Locale`
from values configured by the setters.Locale.LanguageRangeThis class expresses a Language Range defined in
RFC 4647 Matching of
Language Tags.LongSummaryStatisticsA state object for collecting statistics such as count, min, max, sum, and
average.ObjectsThis class consists of `static` utility methods for operating
on objects.ObservableThis class represents an observable object, or "data"
in the model-view paradigm.Optional<T>A container object which may or may not contain a non-null value.OptionalDoubleA container object which may or may not contain a `double` value.OptionalIntA container object which may or may not contain a `int` value.OptionalLongA container object which may or may not contain a `long` value.PriorityQueue<E>An unbounded priority queue based on a priority heap.PropertiesThe `Properties` class represents a persistent set of
properties.PropertyPermissionThis class is for property permissions.PropertyResourceBundle`PropertyResourceBundle` is a concrete subclass of
`ResourceBundle` that manages resources for a locale
using a set of static strings from a property file.RandomAn instance of this class is used to generate a stream of
pseudorandom numbers.ResourceBundleResource bundles contain locale-specific objects.ResourceBundle.Control`ResourceBundle.Control` defines a set of callback methods
that are invoked by the `ResourceBundle.getBundle` factory
methods during the bundle loading process.ScannerA simple text scanner which can parse primitive types and strings using
regular expressions.ServiceLoader<S>A simple service-provider loading facility.SimpleTimeZone`SimpleTimeZone` is a concrete subclass of `TimeZone`
that represents a time zone for use with a Gregorian calendar.SpliteratorsStatic classes and methods for operating on or creating instances of
`Spliterator` and its primitive specializations
`Spliterator.OfInt`, `Spliterator.OfLong`, and
`Spliterator.OfDouble`.Spliterators.AbstractDoubleSpliteratorAn abstract `Spliterator.OfDouble` that implements
`trySplit` to permit limited parallelism.Spliterators.AbstractIntSpliteratorAn abstract `Spliterator.OfInt` that implements `trySplit` to
permit limited parallelism.Spliterators.AbstractLongSpliteratorAn abstract `Spliterator.OfLong` that implements `trySplit`
to permit limited parallelism.Spliterators.AbstractSpliterator<T>An abstract `Spliterator` that implements `trySplit` to
permit limited parallelism.SplittableRandomA generator of uniform pseudorandom values applicable for use in
(among other contexts) isolated parallel computations that may
generate subtasks.Stack<E>The `Stack` class represents a last-in-first-out
(LIFO) stack of objects.StringJoiner`StringJoiner` is used to construct a sequence of characters separated
by a delimiter and optionally starting with a supplied prefix
and ending with a supplied suffix.StringTokenizerThe string tokenizer class allows an application to break a
string into tokens.TimerA facility for threads to schedule tasks for future execution in a
background thread.TimerTaskA task that can be scheduled for one-time or repeated execution by a Timer.TimeZone`TimeZone` represents a time zone offset, and also figures out daylight
savings.TreeMap<K,V>A Red-Black tree based `NavigableMap` implementation.TreeSet<E>A `NavigableSet` implementation based on a `TreeMap`.UUIDA class that represents an immutable universally unique identifier (UUID).Vector<E>The `Vector` class implements a growable array of
objects.WeakHashMap<K,V>Hash table based implementation of the Map interface, with
weak keys.

Enum Summary EnumDescriptionFormatter.BigDecimalLayoutFormEnum for `BigDecimal` formatting.Locale.CategoryEnum for locale categories.Locale.FilteringModeThis enum provides constants to select a filtering mode for locale
matching.

Exception Summary ExceptionDescriptionConcurrentModificationExceptionThis exception may be thrown by methods that have detected concurrent
modification of an object when such modification is not permissible.DuplicateFormatFlagsExceptionUnchecked exception thrown when duplicate flags are provided in the format
specifier.EmptyStackExceptionThrown by methods in the `Stack` class to indicate
that the stack is empty.FormatFlagsConversionMismatchExceptionUnchecked exception thrown when a conversion and flag are incompatible.FormatterClosedExceptionUnchecked exception thrown when the formatter has been closed.IllegalFormatCodePointExceptionUnchecked exception thrown when a character with an invalid Unicode code
point as defined by `Character.isValidCodePoint(int)` is passed to the
`Formatter`.IllegalFormatConversionExceptionUnchecked exception thrown when the argument corresponding to the format
specifier is of an incompatible type.IllegalFormatExceptionUnchecked exception thrown when a format string contains an illegal syntax
or a format specifier that is incompatible with the given arguments.IllegalFormatFlagsExceptionUnchecked exception thrown when an illegal combination flags is given.IllegalFormatPrecisionExceptionUnchecked exception thrown when the precision is a negative value other than
-1, the conversion does not support a precision, or the value is
otherwise unsupported.IllegalFormatWidthExceptionUnchecked exception thrown when the format width is a negative value other
than -1 or is otherwise unsupported.IllformedLocaleExceptionThrown by methods in `Locale` and `Locale.Builder` to
indicate that an argument is not a well-formed BCP 47 tag.InputMismatchExceptionThrown by a `Scanner` to indicate that the token
retrieved does not match the pattern for the expected type, or
that the token is out of range for the expected type.InvalidPropertiesFormatExceptionThrown to indicate that an operation could not complete because
the input did not conform to the appropriate XML document type
for a collection of properties, as per the `Properties`
specification.MissingFormatArgumentExceptionUnchecked exception thrown when there is a format specifier which does not
have a corresponding argument or if an argument index refers to an argument
that does not exist.MissingFormatWidthExceptionUnchecked exception thrown when the format width is required.MissingResourceExceptionSignals that a resource is missing.NoSuchElementExceptionThrown by various accessor methods to indicate that the element being requested
does not exist.TooManyListenersException
The  `TooManyListenersException`  Exception is used as part of
the Java Event model to annotate and implement a unicast special case of
a multicast Event Source.UnknownFormatConversionExceptionUnchecked exception thrown when an unknown conversion is given.UnknownFormatFlagsExceptionUnchecked exception thrown when an unknown flag is given.

Error Summary ErrorDescriptionServiceConfigurationErrorError thrown when something goes wrong while loading a service provider.

Package java.util DescriptionContains the collections framework, legacy collection classes, event model,
date and time facilities, internationalization, and miscellaneous utility
classes (a string tokenizer, a random-number generator, and a bit array).Package SpecificationCollections Framework Overview
Collections Framework Annotated OutlineRelated DocumentationFor overviews, tutorials, examples, guides, and tool documentation, please see:
Collections Framework TutorialCollections
Framework Design FAQ
Since:
JDK1.0



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

