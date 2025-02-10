#### copyXmlToBinary()


 static void AudioProcessor::copyXmlToBinary ( const XmlElement & xml, juce::MemoryBlock & destData ) static 
 

Helper function that just converts an xml element into a binary blob.Use this in your processor's getStateInformation() method if you want to store its state as xml.Then use getXmlFromBinary() to reverse this operation and retrieve the XML from a binary blob.