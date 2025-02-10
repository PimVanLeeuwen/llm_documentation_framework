#### getText()


 String Label::getText ( bool returnActiveEditorContents = false ) const 
 

Returns the label's current text.Parameters

 returnActiveEditorContents if this is true and the label is currently being edited, then this method will return the text as it's being shown in the editor. If false, then the value returned here won't be updated until the user has finished typing and pressed the return key. 
 


Referenced by SidePanel::getTitleText().