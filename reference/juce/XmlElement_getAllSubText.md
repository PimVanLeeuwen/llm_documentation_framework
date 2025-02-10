#### getAllSubText()


 String XmlElement::getAllSubText ( ) const 
 

Returns all the text from this element's child nodes.This iterates all the child elements and when it finds text elements, it concatenates their text into a big string which it returns.E.g.<xyz>hello <x>there</x> world</xyz>
xfloat xDefinition juce\_UnityPluginInterface.h:200
if you called getAllSubText on the "xyz" element, it'd return "hello there world".Note that leading and trailing whitespace will be included in the string to remove if, just call String::trim() on the result.See alsoisTextElement, getChildElementAllSubText, getText, addTextElement