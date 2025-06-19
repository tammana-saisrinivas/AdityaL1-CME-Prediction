# solar_gnss_analysis.py

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.stats import ttest_ind

# --------------------------
# Simulate Data (Example) -- Replace this with actual SunPy/Astropy data fetching if needed
# Quiet Period Data (Low Solar Activity)
quiet_flux = np.random.normal(loc=1e-7, scale=1e-8, size=100)  # Low flux values
quiet_time = pd.date_range(start='2024-04-01', periods=100, freq='h')
quiet_df = pd.DataFrame({'time': quiet_time, 'flux': quiet_flux})

# Flare Period Data (High Solar Activity)
flare_flux = np.random.normal(loc=1e-5, scale=1e-6, size=100)  # High flux values (solar flare)
flare_time = pd.date_range(start='2024-05-10', periods=100, freq='h')
flare_df = pd.DataFrame({'time': flare_time, 'flux': flare_flux})

# --------------------------
# Plot Time Series Comparison
plt.figure(figsize=(12, 6))
plt.plot(quiet_df['time'], quiet_df['flux'], label='Quiet Period', color='blue')
plt.plot(flare_df['time'], flare_df['flux'], label='Flare Period', color='red')
plt.xlabel('Time')
plt.ylabel('X-ray Flux (W/m^2)')
plt.title('GOES X-ray Flux: Quiet vs Flare Period')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/quiet_vs_flare_timeseries.png', dpi=300)
plt.show()

# --------------------------
# Statistical Comparison (T-test)
t_stat, p_value = ttest_ind(quiet_df['flux'], flare_df['flux'])
print("T-test Results:")
print(f"  T-statistic: {t_stat:.4f}")
print(f"  P-value: {p_value:.4e}")

# --------------------------
# Combine Data for Clustering (KMeans)
combined_df = pd.concat([quiet_df, flare_df], ignore_index=True)
X = combined_df['flux'].values.reshape(-1, 1)  # Feature for clustering

kmeans = KMeans(n_clusters=2, random_state=42)
combined_df['cluster'] = kmeans.fit_predict(X)

# Plot KMeans Clustering
plt.figure(figsize=(12, 6))
plt.scatter(combined_df['time'], combined_df['flux'], c=combined_df['cluster'], cmap='viridis')
plt.xlabel('Time')
plt.ylabel('X-ray Flux (W/m^2)')
plt.title('KMeans Clustering of Solar Activity Periods')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/kmeans_clusters.png', dpi=300)
plt.show()

# --------------------------
# Save Data as CSV for Documentation
quiet_df.to_csv('data/quiet_period_flux.csv', index=False)
flare_df.to_csv('data/flare_period_flux.csv', index=False)
combined_df.to_csv('data/combined_flux_clusters.csv', index=False)

print("\nCSV files saved in 'data/' folder.")
print("Plots saved in 'plots/' folder.")
