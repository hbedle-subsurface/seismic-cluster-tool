# Starts the Seismic Facies Clustering Tool (the page is in core.app_main).
import sys
sys.modules.pop('core.app_main', None)   # Streamlit re-runs the page
import core.app_main  # noqa: E402,F401
