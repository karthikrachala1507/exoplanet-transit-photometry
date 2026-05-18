# Exoplanet Transit Photometry
# Step 5: Measure transit depth and duration

import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np

print("Downloading TESS light curve for WASP-39...")
search_result = lk.search_lightcurve("WASP-39", mission="TESS", sector=51, author="SPOC", exptime=120)
lc = search_result.download()

# Clean and normalise
lc_clean = lc.remove_nans().normalize().remove_outliers(sigma=3)

# Known period and epoch
period = 4.0552941  # days
t0 = 2692.9743      # BTJD

# Fold
lc_folded = lc_clean.fold(period=period, epoch_time=t0)

# Bin the folded light curve to smooth it
lc_binned = lc_folded.bin(time_bin_size=0.01)

# Measure transit depth
in_transit = lc_binned.flux[np.abs(lc_binned.time.value) < 0.1]
out_of_transit = lc_binned.flux[np.abs(lc_binned.time.value) > 0.3]

transit_depth = 1 - np.median(in_transit)
baseline = np.median(out_of_transit)

print(f"\n--- Transit Measurements ---")
print(f"Transit Depth: {transit_depth:.4f} ({transit_depth*100:.2f}%)")
print(f"Baseline Flux: {baseline:.4f}")
print(f"Period Used: {period} days")

# Plot binned folded transit
lc_binned.plot()
plt.title("WASP-39b Binned Phase-Folded Transit")
plt.savefig("wasp39_binned_transit.png", dpi=150)
plt.show()
print("\nPlot saved as wasp39_binned_transit.png")