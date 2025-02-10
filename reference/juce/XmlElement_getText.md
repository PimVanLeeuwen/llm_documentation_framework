#### getText()


 const String & XmlElement::getText ( ) const noexcept 
 

Returns the text for a text element.Note that if you have an element like this:<xyz>hello</xyz>
then calling getText on the "xyz" element won't return "hello", because that is actually stored in a special text subelement inside the xyz element. To get the "hello" string, you could either call getText on the (unnamed) subelement, or use getAllSubText() to do this automatically.Note that leading and trailing whitespace will be included in the string to remove if, just call String::trim() on the result.See alsoisTextElement, getAllSubText, getChildElementAllSubText