#### getAlternateDisplayNames()


 virtual StringArray AudioProcessor::getAlternateDisplayNames ( ) const virtual 
 

Returns a list of alternative names to use for this processor.Some hosts truncate the name of your AudioProcessor when there isn't enough space in the GUI to show the full name. Overriding this method, allows the host to choose an alternative name (such as an abbreviation) to better fit the available space.