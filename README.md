This project consisted of finding correlated markets with the Italian Bond and then coming up with a strategy based off of the data to trade the spread of the Italian bond and the correlated market


Part 1: For trading the FBTP futures market, which other Eurex market do you think is most relevant for
getting a read on FBTP price action?


I decided to pick FGBL from EUREX markets to get a read on FBTP price moves. FGBL is a fixed income futures market product following the underlying price of medium to long-term Germany government bonds referred to as Bunds. The Bund is one of the safest government bonds in the EU with a safe haven status in Europe.  

Part 2:  . Extract price data for FBTP and your chosen market in part 1 and calculate the correlation between
the two markets. Does the correlation vary much over the period of your data?


BTP and Bund are heavily correlated bonds in Europe. Germany being the largest economy in EU and Italy being the third largest economy have a lot in common with both having government loans backed by the ECB. However, Germany being the safest economy in Europe in the investors’ perspective, makes it that during times with high volatility and change in risk sentiment, the strong correlation between the price of these two bonds breaks. This can be seen in the chart for example, during June and French elections, FOAT and FBTP were more correlated, and Bund was often reversing the moves of BTP since BTP is riskier than Bund. 

Part 3:  3. Use the data from the two markets above to calculate the spread price of the two markets. How
likely will the spread price subsequently revert to the starting mean (moving average) if the spread
price moves 20 ticks or more from the mean?

1: Finding the spread price 

The data we used were the prices traded in the FGBL and FBTP at half an hour intervals from 01/02/2024 at 08:00 to 29/08/2024 at 14:30. We got the average ATR and average price for the whole period to calculate the spread ratio. We found the best spread price to use was FGBL – FBTP. 

2: How likely will the spread price subsequently revert to the starting mean (moving average) if the spread price moves 20 ticks or more from the mean? 

To complete this we transferred our data to Python. In Python we built a function which recognized whenever the moving average differed to the spread price by 20 ticks. We then built a function which recorded whether the price reverted back to the mean in a given timeframe. Some examples of the results are: 

In the period from the 1st of February to the 29th of August there are 50 significant times where the moving average differs to the price by 20 ticks. 

Out of these 50 times the price reverts back to the mean 5 times (10%) within 3 hours, 12 times (24%) within 6 hours and 15 times (30%) with 9 hours.  

  

 

Part 4: Is there a valid strategy in going against the spread trend if it extends more than 20 ticks? 

To examine this, we messed with our original function to find the highest percentage of reversals. One strategy which seems promising was to make a mean reverting trade after the initial 20 tick drop if 2 of the next 3 candles fill closer to the mean than the previous candle. You would enter the trade after confirmation that 2 candles reverted to the mean. Using this strategy, we found that: 

We would have been able to use this strategy 19 times in the time period we looked at (Feb- Aug) 

Out of these 19 times the price reverts back to the mean 6 times (31.6%) within 3 hours, 13 times (68.4%) within 6 hours and 14 times (73.7%) with 9 hours. 

 

Using this analysis, we believe that there is a valid strategy to enter a mean reverting trade after the spread price differs to the moving average by 20 ticks and then 2 of the next 3 candles move back towards the mean. We would get out of the trade if the price falls back to below/above the original price (where spread and moving average differed by 20 ticks) or when the price reverts to the initial moving average price. If our risk limit wasn’t hit, we would give the trade 6 hours to run. 


Part 5: 

Other options in EUREX markets that could be used to track FBTP price movements are, for example, FOAT and FBON. FOAT is the French government bond with similar risk sentiment with FBTP and can be better applied to FBTP price correlation during large moves in risk-on risk-off times. FBON is the Spanish government bond and has relatively similar risk sentiment to FBTP. Picking a large European bond is important to have large volume in the futures market with similar economy and government such that investors see the bonds with similar risk. 
