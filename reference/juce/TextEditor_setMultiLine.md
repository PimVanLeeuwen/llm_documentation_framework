#### setMultiLine()


 void TextEditor::setMultiLine ( bool shouldBeMultiLine, 
 
 bool shouldWordWrap = true ) 

Puts the editor into either multi or singleline mode.By default, the editor will be in singleline mode, so use this if you need a multiline editor.See also the setReturnKeyStartsNewLine() method, which will also need to be turned on if you want a multiline editor with linebreaks.Parameters

 shouldBeMultiLine whether the editor should be multi or singleline. 
 
 shouldWordWrap sets whether long lines should be broken up in multiline editors. If this is false and scrollbars are enabled a horizontal scrollbar will be shown. 



See alsoisMultiLine, setReturnKeyStartsNewLine, setScrollbarsShown