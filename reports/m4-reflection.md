# Milestone 3 Reflection

Since **Milestone 3**, our team has implemented and refined several key components of our dashboard to enhance functionality, usability, and visual clarity. Below is a breakdown of what has been added and refined:  

#### **Implemented Features & Refinements**

- **Auto-adjust map zooming range** – Improved usability by dynamically adjusting zoom based on the data range.  
- **Caching mechanism** – Implemented caching to enhance performance and reduce load times.  
- **Banner enhancements**:
  - Added a banner when loading to improve user feedback during data retrieval.  
  - Introduced a banner for cases where passenger count is **0** to provide clearer messaging.  
- **Visualization improvements**:
  - **Color legend added** for the passenger flow over time chart to improve interpretability.  
  - **Updated volume of entry representation** to reduce unnecessary zeros, making the numbers more readable.  
- **Peer review feedback addressed**, refining multiple aspects based on external input.  
- **UI/UX Improvements**:
  - Updated the **favicon and tab title** to improve branding and consistency.  

#### **Deviations from Peer Feedbacks & Justifications**

There are no deviations from the initial proposal, but some peer feedbacks which were not addressed are as follows

- **Tooltip information on the map**: While additional metrics in the map tooltips were suggested, we chose to keep them minimal to avoid cluttering the interface. This ensures the map remains clear and easy to interpret.  
- **Graph controls placement**: We maintained unified controls instead of separating them for the map, prioritizing consistency over potential aesthetic improvements.  
- **Scrolling vs. tabs/pages**: Rather than dividing the dashboard into separate sections or tabs, we refined the layout to fit key insights onto one page. This approach reduces navigation complexity and keeps all data readily accessible.  

#### **Known Corner Cases & Limitations**

- **Arrow key navigation conflict**: The calendar feature responds to arrow keys, but this also triggers page scrolling. We are aware of this but are not addressing it at this stage, as modifying default browser behavior could introduce unintended side effects.  
- **Tooltip granularity**: While more detailed tooltips could provide deeper insights, we opted for a simpler version to prevent information overload.  
- **Dashboard growth considerations**: If the dashboard expands further, restructuring with tabs or collapsible sections may become necessary to maintain clarity and usability.  

#### **Reflection & Future Improvements**

**What the dashboard does well:**  

- Provides a **clear, data-driven overview** of passenger flow trends.  
- **Optimized performance** with caching for faster interactions.  
- **Improved user experience** with refined visual elements and better data representation.  

**Limitations & Future Enhancements:**  

- If more data visualizations are added, **layout adjustments** (such as tabs or collapsible sections) may be necessary.  
- The **tooltip system** could be enhanced with conditional toggling to balance detail and readability.  
- **Interactive elements** (e.g., additional filtering options for different passenger categories) could improve the user experience further.  

With more time, we would focus on refining **interactive filtering, predictive insights, and additional visual enhancements** to make the dashboard even more comprehensive and user-friendly.
