#### getNextBestLayoutInLayoutList()


template<size\_t numLayouts> 

 BusesLayout AudioProcessor::getNextBestLayoutInLayoutList ( const BusesLayout & layouts, 
 
 const short(&) channelLayoutList[numLayouts][2] ) 

Returns the next best layout which is contained in a channel layout map.You can use this method to help you implement getNextBestLayout. For example:BusesLayout getNextBestLayout (const BusesLayout& layouts) override
{
 return getNextBestLayoutInLayoutList (layouts, {{1,1},{2,2}});
}
AudioProcessor::getNextBestLayoutInLayoutListBusesLayout getNextBestLayoutInLayoutList(const BusesLayout &layouts, const short(&channelLayoutList)[numLayouts][2])Returns the next best layout which is contained in a channel layout map.Definition juce\_AudioProcessor.h:813