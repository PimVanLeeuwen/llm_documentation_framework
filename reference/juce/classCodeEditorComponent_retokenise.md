#### retokenise()


 void CodeEditorComponent::retokenise ( int startIndex, 
 
 int endIndex ) 

Rebuilds the syntax highlighting for a section of text.This happens automatically any time the CodeDocument is edited, but this method lets you change text colours even when the CodeDocument hasn't changed.For example, you could use this to highlight tokens as the cursor moves. To do so you'll need to tell your custom CodeTokeniser where the token you want to highlight is, and make it return a special type of token. Then you should call this method supplying the range of the highlighted text.See alsoCodeTokeniser