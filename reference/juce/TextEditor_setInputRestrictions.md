#### setInputRestrictions()


 void TextEditor::setInputRestrictions ( int maxTextLength, 
 
 const String & allowedCharacters = String() ) 

Sets limits on the characters that can be entered.This is just a shortcut that passes an instance of the LengthAndCharacterRestriction class to setInputFilter().Parameters

 maxTextLength if this is > 0, it sets a maximum length limit; if 0, no limit is set 
 
 allowedCharacters if this is nonempty, then only characters that occur in this string are allowed to be entered into the editor.