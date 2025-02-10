#### end()


 CharPointerType String::end ( ) const 
 

Returns an iterator pointing at the terminating null of the string.Note that this has to find the terminating null before returning it, so prefer to call this once before looping and then reuse the result, rather than calling 'end()' each time through the loop.String str = ...;
 
// BEST
for (auto c : str)
 DBG (c);
 
// GOOD
for (auto ptr = str.begin(), end = str.end(); ptr != end; ++ptr)
 DBG (\*ptr);
 
std::for\_each (str.begin(), str.end(), [] (juce\_wchar c) { DBG (c); });
 
// BAD
for (auto ptr = str.begin(); ptr != str.end(); ++ptr)
 DBG (\*ptr);
StringThe JUCE String class!Definition juce\_String.h:68
String::endCharPointerType end() constReturns an iterator pointing at the terminating null of the string.Definition juce\_String.h:977
DBG#define DBG(textToWrite)Writes a string to the standard error stream.Definition juce\_PlatformDefs.h:160
juce\_wcharwchar\_t juce\_wcharA platformindependent 32bit unicode character type.Definition juce\_CharacterFunctions.h:57
References begin().Referenced by StringArray::end(), and StringArray::end().