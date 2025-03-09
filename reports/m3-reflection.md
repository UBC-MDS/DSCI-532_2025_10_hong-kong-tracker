# Milestone 3 Reflection  

In this milestone, we focused on refining our visualizations to create a more cohesive user experience and did not make significant changes from our initial proposal.

## Improvements  

1. **Consistent Visualization Library**: We addressed inconsistent formatting by standardizing on Plotly for all visualizations. Previously, we used a mix of Plotly and Altair.  
2. **Unified Dashboard Background Color**: We removed the individual background colors from charts. Now, all charts are seamlessly integrated into the dashboard background.  
3. **Simplified Color Scheme**: We simplified the Passenger Origin and Travel Method bar charts by applying a single, consistent color from our dashboard's palette. The previous version's coloring was unnecessary and caused confusion.  
4. **Improved Scorecard Clarity**: We enhanced the readability of the Volume of Entries scorecard by changing the format from decimal to percentage. We also added a disclaimer to explain the calculation method.  

## What the Dashboard Does Well  

1. **Concise and Clear Communication**: Our dashboard is clear and concise, with no complex charts. This allows us to communicate information and insights to stakeholders in a simple and straightforward manner.  
2. **Cohesive Interface**: The color theme brings a consistent user experience. There are no distracting elements within the charts.  

## Limitations  

1. **Dashboard Loading Speed**: Our dashboard processes a large dataset, and the computational power of Render.com is limited. It takes around **15 to 30 seconds** for the dashboard to fully load, compromising the user experience.  
2. **Limited Time-Series Analysis**: While our dashboard provides a general overview, it lacks in-depth time-series analysis. Additional insights, such as **monthly trends and seasonal patterns**, could be explored further.  

## Potential Future Improvements and Additions  

1. **Dashboard Loading Speed and Stability**: Our dashboard processes a large dataset, and the computational power of Render.com is limited. It takes around **15 to 30 seconds** for the dashboard to fully load. Additionally, sometimes the app does not render initially, requiring the user to apply a filter or refresh the page. This compromises the user experience.
2. **Dynamic Time-Series Insights**: We can implement dynamic time-series analysis based on the user's selected date range. For example, if a user selects a **year**, the dashboard could display a **monthly breakdown**; if a user selects a **month**, the dashboard could display a **weekly breakdown**. This would provide more in-depth insights.  