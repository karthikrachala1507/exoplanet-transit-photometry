# Exoplanet Transit Photometry
# Step 2: Download light curve and plot it

import lightkurve as lk
import matplotlib.pyplot as plt

# Search for WASP-39
print("Downloading TESS light curve for WASP-39...")
search_result = lk.search_lightcurve("WASP-39", mission="TESS", sector=51, author="SPOC", exptime=120)

# Download the light curve
lc = search_result.download()
print("Download complete.")
print(lc)

# Plot the raw light curve
lc.plot()
plt.title("WASP-39 Raw Light Curve - TESS Sector 51")
plt.savefig("wasp39_raw_lightcurve.png", dpi=150)
plt.show()
print("Plot saved as wasp39_raw_lightcurve.png")