# Exoplanet Transit Photometry
# Step 3: Clean and normalise the light curve

import lightkurve as lk
import matplotlib.pyplot as plt

print("Downloading TESS light curve for WASP-39...")
search_result = lk.search_lightcurve("WASP-39", mission="TESS", sector=51, author="SPOC", exptime=120)
lc = search_result.download()

# Remove NaN values and normalise flux
lc_clean = lc.remove_nans().normalize()

# Remove outliers beyond 3 sigma
lc_clean = lc_clean.remove_outliers(sigma=3)

print("Cleaned light curve:")
print(lc_clean)

# Plot cleaned light curve
lc_clean.plot()
plt.title("WASP-39 Cleaned and Normalised Light Curve - TESS Sector 51")
plt.savefig("wasp39_clean_lightcurve.png", dpi=150)
plt.show()
print("Plot saved as wasp39_clean_lightcurve.png")