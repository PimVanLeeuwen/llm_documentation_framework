#### appendNumbersToDuplicates()


 void StringArray::appendNumbersToDuplicates ( bool ignoreCaseWhenComparing, 
 
 bool appendNumberToFirstInstance, 
 CharPointer\_UTF8 preNumberString = CharPointer\_UTF8(nullptr), 
 CharPointer\_UTF8 postNumberString = CharPointer\_UTF8(nullptr) ) 

Adds numbers to the strings in the array, to make each string unique.This will add numbers to the ends of groups of similar strings. e.g. if there are two "moose" strings, they will become "moose (1)" and "moose (2)"Parameters

 ignoreCaseWhenComparing whether the comparison used is caseinsensitive 
 
 appendNumberToFirstInstance whether the first of a group of similar strings also has a number appended to it. 
 preNumberString when adding a number, this string is added before the number. If you pass nullptr, a default string will be used, which adds brackets around the number. 
 postNumberString this string is appended after any numbers that are added. If you pass nullptr, a default string will be used, which adds brackets around the number.