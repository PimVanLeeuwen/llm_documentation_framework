#### createFromDescription()


 static KeyPress KeyPress::createFromDescription ( const String & textVersion ) static 
 

Converts a textual key description to a KeyPress.This attempts to decode a textual version of a keypress, e.g. "ctrl + c" or "spacebar".This isn't designed to cope with any kind of input, but should be given the strings that are created by the getTextDescription() method.If the string can't be parsed, the object returned will be invalid.See alsogetTextDescription