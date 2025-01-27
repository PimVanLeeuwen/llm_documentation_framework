#### doBufferedRead()


template<typename Index , typename GetBufferedRange , typename ReadFromReservoir , typename FillReservoir > 

 static Range< Index > Reservoir::doBufferedRead ( Range< Index > rangeToRead, GetBufferedRange && getBufferedRange, ReadFromReservoir && readFromReservoir, FillReservoir && fillReservoir ) static 
 

Attempts to read the requested range from some kind of input stream, with intermediate buffering in a 'reservoir'.While there are still samples in the requested range left to read, this function will check whether the next part of the requested range is already loaded into the reservoir. If the range is available, then doBufferedRead will call readFromReservoir with the range that should be copied to the output buffer. If the range is not available, doBufferedRead will call fillReservoir to request that a new region is loaded into the reservoir. It will repeat these steps until either the entire requested region has been read, or the stream ends.This will return the range that could not be read successfully, if any. An empty range implies that the entire read was successful.Note that all ranges, including those provided as arguments to the callbacks, are relative to the original unbuffered input. That is, if getBufferedRange returns the range [200, 300), then readFromReservoir might be passed the range [250, 300) in order to copy the final 50 samples from the reservoir.Parameters

 rangeToRead the absolute position of the range that should be read 
 
 getBufferedRange a function void > Range<Index> that returns the region currently held in the reservoir 
 readFromReservoir a function Range<Index> > void that can be used to copy samples from the region in the reservoir specified in the input range 
 fillReservoir a function Index > void that is given a requested read location, and that should attempt to fill the reservoir starting at this location. After this function, getBufferedRange should return the new region contained in the managed buffer 


References Range< ValueType >::getIntersectionWith(), Range< ValueType >::getStart(), Range< ValueType >::isEmpty(), and Range< ValueType >::setStart().

The documentation for this struct was generated from the following file:juce\_Reservoir.h
### Purchase

Get JUCE
### Discover

What's New in JUCEFeatures
### Learn

DocumentaionTutorialsMade with JUCEResources
### Support

JUCE ForumNewsletterArchive
### About

Contact UsJUCE LegalJUCE Licensing FAQ
### Events

Audio Developer Conference
Visit our FacebookVisit our TwitterVisit our LinkedInVisit our YouTube channel© Raw Material Software Limited
linkedin




facebook


pinterest


youtube


rss


twitter


instagram




facebookblank


rssblank


linkedinblank


pinterest


youtube


twitter


instagram