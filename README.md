# Solar Activity Visualization and Its Potential Impact on GNSS Accuracy

This project investigates the variations in solar activity during quiet and flare periods using GOES X-ray flux data and explores its potential implications on the reliability of GNSS (Global Navigation Satellite Systems). The analysis employs Python libraries such as SunPy, Astropy, Pandas, Matplotlib, and Scikit-Learn.

## 📌 Objectives
- To visualize and compare solar X-ray flux during quiet and flare periods.
- To statistically assess the difference between these periods using a T-test.
- To apply KMeans clustering to classify and distinguish solar activity levels.
- To discuss potential impacts of high solar activity on GNSS signal integrity — relevant for aerospace, UAVs, and navigation systems.

## 🛠️ Tools & Technologies Used
- **Python 3.x**
- **Pandas** — Data handling
- **Matplotlib** — Visualization
- **Scikit-Learn** — Machine Learning (KMeans Clustering)
- **SunPy/Astropy** — Solar data fetching (planned)
- **Scipy** — Statistical testing (T-test)

## 📊 Features
- Comparative visualization of quiet vs flare periods.
- Statistical significance testing (T-test) between periods.
- Unsupervised clustering (KMeans) for solar activity classification.
- Generation of publication-quality plots for research papers.
- Output data saved as CSV files for reproducibility.


## 📈 Example Outputs
- **Quiet vs Flare Period X-ray Flux Time Series**
- **KMeans Clustering Scatter Plot**

*(Plots are available in the `/plots` folder)*

## 📂 Data Availability
All processed data files (`quiet_period_flux.csv`, `flare_period_flux.csv`, `combined_flux_clusters.csv`) are available in the `/data` directory.

## 🚀 Potential Applications
- GNSS performance risk estimation during high solar activity.
- Aerospace and UAV operational planning during space weather events.
- Educational material for space weather impact studies.

## 📖 Paper Reference
The results of this project are being prepared for submission to the *Episodes* Journal (Scopus-indexed) under the title:

> "Comparative Visualization and Trend Analysis of Solar Quiet and Flare Periods: Implications for GNSS Signal Integrity"

## ⚠️ Limitations
- GNSS signal error measurements were not directly analyzed — future work may integrate ionospheric TEC and GNSS performance data.
- Data used here are simulated for method demonstration; actual GOES XRS data can be fetched via SunPy/Astropy.

## 📜 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🤝 Acknowledgements
- GOES Satellite Data (NOAA SWPC)
- SunPy and Astropy Python Libraries

