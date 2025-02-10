#### setPasswordCharacter()


 void TextEditor::setPasswordCharacter ( juce\_wchar passwordCharacter ) 
 

Changes the password character used to disguise the text.Parameters

 passwordCharacter if this is not zero, this character will be used as a replacement for all characters that are drawn on screen e.g. to create a passwordstyle textbox containing circular blobs instead of text, you could set this value to 0x25cf, which is the unicode character for a black splodge (not all fonts include this, though), or 0x2022, which is a bullet (probably the best choice for linux).