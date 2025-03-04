# 🚀 Dashboard of Hong Kong Passenger Traffic Tracker

Welcome to the **Hong Kong Passenger Traffic Tracker**—your one-stop dashboard for uncovering the latest trends in cross-border movement! Whether you're a policymaker, researcher, or just plain curious, we've got the data you need to make sense of the ebb and flow of passengers.

## 📖 The Problem

Hong Kong’s control points see a staggering amount of cross-border movement daily. But with raw data scattered across multiple sources, identifying trends and making informed decisions can feel like looking for a needle in a haystack. Without clear visualizations, optimizing transportation, resource allocation, and policy planning is a serious challenge—especially when travel restrictions keep changing!

## 💡 The Solution

Enter our **interactive dashboard**! With dynamic filters, historical comparisons, and real-time insights, we make it easier than ever to track cross-border trends. Whether it's managing peak hours, adjusting resources, or keeping up with shifting traveler patterns, our dashboard helps decision-makers navigate Hong Kong’s dynamic passenger flow with confidence.

## 💻 How to Use It

Our dashboard offers three key filters to help you refine your data exploration:

- **📅 Date Filter** – Select specific dates or date ranges to analyze passenger traffic trends over time.
- **🚪 Control Point Filter** – Focus on specific entry and exit points to see how traffic varies across different locations.
- **🛂 Travel Type Filter** – Segment travelers by category (Hong Kong residents, Mainland visitors, and others) to understand movement patterns.

Simply adjust these filters to uncover insights and trends in Hong Kong's passenger flow!

### 🌍 Dashboard

Click [here](https://five32-group-10.onrender.com/) to check out the live dashboard!

### 🎬 Demo

<img src="img/demo.gif" alt="Demo GIF" width="600">

## 🛠 Developer Guide

1. **Clone this GitHub repository**
   Run the following command to clone the repository:

   ```bash
   git clone git@github.com:UBC-MDS/DSCI-532_2025_10_hong-kong-tracker.git
   ```

2. **Create the virtual environment**
   Use Conda to set up and activate the environment:

   ```bash
   conda env create -f environment.yaml
   conda activate 532
   ```

3. **Modify imports and enable debug mode**

   - In `app.py` and `callbacks.py`, **remove** `src` from the imports, specifically from:

     ```python
     src.callbacks
     src.travel_method
     src.passenger_origin
     src.passenger_count
     ```
  
   - In `app.py`, **set** `debug = True` at the bottom.

   **Note:** Before pushing changes, revert these modifications to ensure a successful deployment.

4. **Run the application**
   From the project root directory, execute:

   ```bash
   python src/app.py
   ```

5. **Access the application**
   Open your browser and go to:

   ```
   http://127.0.0.1:8080/
   ```

   to see the dashboard in action!

## 👥 Meet the Team

We’re a team of passionate data scientists on a mission to make data-driven decision-making easier:

- **Nelli Hovhannisyan**
- **Paramveer Singh**
- **Hankun Xiao**
- **Yichun Liu**

## 🎭 Contributing

Want to improve the dashboard or add new features? Check out our [contributing guidelines](https://github.com/UBC-MDS/DSCI-532_2025_10_hong-kong-tracker/blob/main/CONTRIBUTING.md) before getting started.

By contributing, you agree to follow our Code of Conduct—let’s keep it collaborative and fun! 🚀

## 📚 License

This project is licensed under the [MIT license](https://github.com/UBC-MDS/DSCI-532_2025_10_hong-kong-tracker/blob/main/LICENSE.md).

The **Daily Passenger Traffic dataset**, sourced from **DATA.GOV.HK**, is free to use for both commercial and non-commercial purposes, following the official [Terms of Use](https://data.gov.hk/en/terms-and-conditions).

## 💬 Need Help?

If you run into any issues, have feature suggestions, or just want to say hi, drop us an issue on [GitHub Issues](https://github.com/UBC-MDS/DSCI-532_2025_10_hong-kong-tracker/issues). We’d love to hear from you! 😊

## 📖 References

Data sourced from: [Hong Kong Daily Passenger Traffic Dataset](https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic).
