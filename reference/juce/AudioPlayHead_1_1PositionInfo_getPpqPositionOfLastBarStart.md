#### getPpqPositionOfLastBarStart()


 Optional< double > AudioPlayHead::PositionInfo::getPpqPositionOfLastBarStart ( ) const 
 

The position of the start of the last bar, in units of quarternotes.This is the time from the start of the timeline to the start of the current bar, in ppq units.Note this value may be unavailable on some hosts, e.g. ProTools.