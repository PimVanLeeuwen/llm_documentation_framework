#### getTextValue()


 Value & TextEditor::getTextValue ( ) 
 

Returns a Value object that can be used to get or set the text.Bear in mind that this operate quite slowly if your text box contains large amounts of text, as it needs to dynamically build the string that's involved. It's best used for small text boxes.