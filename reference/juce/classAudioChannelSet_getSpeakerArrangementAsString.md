#### getSpeakerArrangementAsString()


 String AudioChannelSet::getSpeakerArrangementAsString ( ) const 
 

Returns a string containing a whitespaceseparated list of speaker types corresponding to each channel.For example in a 5.1 arrangement, the string may be "L R C Lfe Ls Rs". If the speaker arrangement is unknown, the returned string will be empty.