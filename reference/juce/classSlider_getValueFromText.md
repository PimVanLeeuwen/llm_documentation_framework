#### getValueFromText()


 virtual double Slider::getValueFromText ( const String & text ) virtual 
 

Subclasses can override this to convert a text string to a value.When the user enters something into the textentry box, this method is called to convert it to a value. The default implementation just tries to convert it to a double.See alsogetTextFromValue