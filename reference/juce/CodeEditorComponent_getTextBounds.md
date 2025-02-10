#### getTextBounds()


 RectangleList< int > CodeEditorComponent::getTextBounds ( Range< int > textRange ) const overridevirtual 
 

Returns the bounding box for a range of text in the editor.As the range may span multiple lines, this method returns a RectangleList.The bounds are relative to the component's topleft and may extend beyond the bounds of the component if the text is long and word wrapping is disabled.Implements TextInputTarget.