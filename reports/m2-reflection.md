### **Reflection on Dashboard Implementation**

Our group has successfully implemented several key features from our proposal.  
We have incorporated **interactive filters**, allowing users to select a **time period, control points, and arrival or departure status**.  

The **Net Passenger Flow chart** has been implemented as a **stacked area chart**  
to distinguish inflow (arrivals) and outflow (departures).  

Additionally, the **Passenger Count graph** is displayed as a **grouped bar chart**, showing variations over time.  
The **Passenger Origin and Travel Type charts** are presented as **horizontal bar charts**,  
effectively visualizing different passenger categories.  

Finally, the **Volume of Control Point Traffic Map** has been implemented using **Dash Leaflet**,  
displaying control points with **circle markers** that scale based on passenger volume.  

---

### **Outstanding Features**

While much of the dashboard has been implemented, some features are still in development.  
One limitation is the **layout of visualizations**, as some charts appear **compressed**, reducing readability.  

The **map component**, though functional, does not **dynamically adjust its size optimally**,  
which can impact user experience.  

We also plan to enhance interactivity by adding **hover effects and tooltips**  
to provide more detailed data insights when users interact with graphs.  

---

### **Deviations from Proposal & Justifications**

One key change was the introduction of a **collapsible sidebar**.  
Initially, our design had a **fixed sidebar**, but we found that it **took up too much space**,  
especially on smaller screens.  

Implementing a **collapsible sidebar** allows for a better balance  
between filtering options and visualization space.  

Another change was the **use of a grid layout for graphs** instead of stacking them vertically.  
The original design required **excessive scrolling**, which was inefficient for data exploration.  
By utilizing a **grid structure**, we improved readability and allowed multiple graphs to be viewed simultaneously.  

We also made **adjustments to data processing**  
to ensure consistency in control point names and handle missing dates.  
These modifications made the visualizations **more accurate and reliable**.  


---

### **Strengths of the Dashboard**

Despite these challenges, our dashboard has several strengths.  

The **interactive filtering system** makes data exploration smooth,  
and we have followed **effective visualization practices**  
by using **clear labels, color differentiation, and appropriate chart types**.  

The dashboard’s **modular structure** ensures that it can be **extended with additional features** in the future.  

---

### **Future Improvements**

Moving forward, we plan to refine the **layout and responsiveness**,  
ensuring that graphs **adjust dynamically** to different screen sizes.  

Additionally, improving the **map’s usability**  
by enabling direct **filtering within the geographic interface**  
would enhance functionality.  
We would try to do this if time permits. 

---

### **Conclusion**

In summary, our dashboard effectively visualizes **passenger traffic in Hong Kong**,  
but further refinements are needed to improve **responsiveness, performance, and interactivity**.  

By addressing these areas, we can ensure a **more seamless and informative user experience**.  