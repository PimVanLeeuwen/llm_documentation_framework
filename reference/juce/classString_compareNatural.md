#### compareNatural()


 int String::compareNatural ( StringRef other, bool isCaseSensitive = false ) const noexcept 
 

Compares two strings, taking into account textual characteristics like numbers and spaces.This comparison is caseinsensitive and can detect words and embedded numbers in the strings, making it good for sorting humanreadable lists of things like filenames.Returns0 if the two strings are identical; negative if this string comes before the other one alphabetically, or positive if it comes after it. Referenced by File::NaturalFileComparator::compareElements().