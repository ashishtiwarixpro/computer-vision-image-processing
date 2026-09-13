# Computer Vision Unit II Programming Assignment

Name: Ashish Tiwari |
Enrollment Number: 2402309021 |
Class/Section: BCA Sec-A, Sem-5 |
Programs Completed: 15/15

## About This Assignment

This repository contains all 15 required Computer Vision programs
for the BCA 5th Semester Unit II programming assignment.

Each numbered folder contains:
- `program.py` — Python/OpenCV source code
- `input.jpg` — input image used by the program
- Required generated output file(s)

All programs use relative file paths so that each program can be
run independently from its own folder.

## Programs

| # | Folder | Topic |
|---|--------|-------|
| 1 | `01_Grayscale` | Grayscale Conversion and Image Information |
| 2 | `02_Brightness` | Controlled Brightness Enhancement |
| 3 | `03_Contrast_Stretching` | Contrast Stretching |
| 4 | `04_Histogram` | Histogram Analysis |
| 5 | `05_Histogram_Equalization` | Histogram Equalization with Before/After Comparison |
| 6 | `06_Mean_Filter` | Mean Filtering |
| 7 | `07_Gaussian_Filter` | Gaussian Smoothing |
| 8 | `08_Median_Filter` | Salt-and-Pepper Noise Reduction |
| 9 | `09_Filter_Comparison` | Mean vs Gaussian vs Median |
| 10 | `10_Sharpening` | Image Sharpening Using a Custom Kernel |
| 11 | `11_Smoothing_vs_Sharpening` | Smoothing vs Sharpening Comparison |
| 12 | `12_DFT` | 2D DFT Computation |
| 13 | `13_Magnitude_Spectrum` | Magnitude Spectrum |
| 14 | `14_Frequency_LPF` | Frequency-Domain Low-Pass Filtering |
| 15 | `15_Frequency_HPF` | Frequency-Domain High-Pass Filtering |

## Output Files

The required output filenames are:

| Program | Required Output |
|---|---|
| 1 | `output.png` |
| 2 | `output.png` |
| 3 | `output.png` |
| 4 | `output.png` |
| 5 | `output.png`, `histogram_comparison.png` |
| 6 | `output.png` |
| 7 | `output.png` |
| 8 | `output.png` |
| 9 | `output_mean.png`, `output_gaussian.png`, `output_median.png` |
| 10 | `output.png` |
| 11 | `output_smooth.png`, `output_sharp.png` |
| 12 | `output.png` |
| 13 | `output.png` |
| 14 | `output.png` |
| 15 | `output.png` |

## Notes on Input Images

The same base portrait image (`input.jpg`) is used across all program
folders. For Programs 8 and 9, which specifically require an input
image that visibly contains salt-and-pepper (impulse) noise, the
program itself adds this noise to the base image and overwrites
`input.jpg` in that folder before applying the filter(s), so the
submitted input file meets the stated requirement.

## How to Run

Open a terminal inside the required program folder.

For example:

```bash
cd 01_Grayscale
python program.py
```

Each program is self-contained and only needs the `input.jpg` file
present in its own folder.
