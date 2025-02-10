#### matchesWildcard()


 bool String::matchesWildcard ( StringRef wildcard, bool ignoreCase ) const noexcept 
 

Returns true if the string matches this simple wildcard expression.So for example String ("abcdef").matchesWildcard ("\*DEF", true) would return true.This isn't a fullblown regex though! The only wildcard characters supported are "\*" and "?". It's mainly intended for filename pattern matching.