# Seismic Facies Clustering Tool

Unsupervised seismic facies clustering for teaching and research: load seismic
attribute volumes (3D or 2D, SEG-Y), prepare and scale them, reduce dimensions
(PCA, ICA, t-SNE and more), cluster (K-means, GMM, HDBSCAN and more), compare
models, and export the results as SEG-Y.

## Use it

* **In your browser:** https://hbedle-subsurface.github.io/seismic-cluster-tool/
  Nothing to install; your data never leave your computer. Best for cropped
  volumes up to about 600 MB in total. Crop larger volumes in the browser
  with the [SEG-Y Cropper](https://hbedle-subsurface.github.io/segy-cropper/).
* **Download (Windows):** the latest zip under
  [Releases](../../releases/latest). Unzip and double-click
  `Start Seismic Cluster Tool.bat`. No installation and no Python needed; it
  uses every processor core and handles full surveys.

`Getting_Started.html`, in the download and on the website, walks through
each step.

## Credits

Built for teaching by Dr. April Moreno-Ward, Dr. Heather Bedle, Matheus Nilo,
Aniq Ahmad, and Hilmi Putra, University of Oklahoma, with the
[AASPI](https://www.ou.edu/mcee/labs/aaspi) consortium.

**To cite:** A. Moreno-Ward, H. Bedle, M. Nilo, A. Ahmad, and H. Putra, 2026,
Seismic Facies Clustering Tool (version 6.7): SSRN, [article link to follow].

Free to use, including in teaching and research. If you use it in a course,
a talk, or a publication, please credit the tool and link back to it.
Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Built on open-source software; the list of components and their licenses is
in `OPEN_SOURCE_COMPONENTS.txt` in the download and on the website.

## Privacy

The website records only that the page was opened: no cookie, no account,
and no personal information. The download makes one network request, a check
for a newer version, and sends nothing from the tool.
