#### startsWithChar()


 bool String::startsWithChar ( juce\_wchar character ) const noexcept 
 

Tests whether the string begins with a particular character.If the character is 0, this will always return false. Uses a casesensitive comparison.Referenced by StandalonePluginHolder::getFilePatterns().