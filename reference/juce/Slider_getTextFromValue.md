#### getTextFromValue()


 virtual String Slider::getTextFromValue ( double value ) virtual 
 

Turns the slider's current value into a text string.Subclasses can override this to customise the formatting of the textentry box.The default implementation just turns the value into a string, using a number of decimal places based on the range interval. If a suffix string has been set using setTextValueSuffix(), this will be appended to the text.See alsogetValueFromText