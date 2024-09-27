
# **Sea Level Predictor**

This project analyzes the global average sea level changes since 1880 using a dataset from CSIRO and NOAA. It fits a linear regression model to predict future sea level changes through the year 2050. The project includes functions for plotting historical data, fitting regression models, and visualizing predictions.

## **Project Structure**

- `sea_level_predictor.py`: Contains the core functions for reading the dataset, generating scatter plots, performing regression analysis, and saving plots.
- `main.py`: The main script used to generate the plot and run the unit tests.
- `test_module.py`: Unit tests to ensure the functionality of the code in `sea_level_predictor.py`.
- `epa-sea-level.csv`: The dataset containing sea level changes from 1880 to the most recent year, used in the analysis.

## **Dataset Information**

### Source:
The dataset used in this project is available from the [EPA Sea Level Data](https://datahub.io/core/sea-level-rise/r/epa-sea-level.csv). It includes global average sea level changes over time, measured by:
- **CSIRO Adjusted Sea Level (inches)**: Sea level changes adjusted for the global average.
- **Year**: The year corresponding to the sea level data.

### Columns:
- **Year**: The year of the measurement (from 1880 onward).
- **CSIRO Adjusted Sea Level**: Global average sea level, adjusted by the CSIRO (in inches).

## **Setup and Installation**

To run the project, you will need Python 3 installed on your machine along with the following Python packages:
- `pandas`
- `matplotlib`
- `scipy`

You can install these dependencies using pip:
```bash
pip install pandas matplotlib scipy
```

## **How to Run the Code**

1. **Clone the Repository**:
   Clone the repository or download the project files to your local machine.

2. **Download the Dataset**:
   Make sure the dataset `epa-sea-level.csv` is in the same directory as the project files. You can download it from [this link](https://datahub.io/core/sea-level-rise/r/epa-sea-level.csv).

3. **Run the Main Script**:
   To generate the sea level plot and run the unit tests, execute `main.py`:
   ```bash
   python main.py
   ```

   This will:
   - Generate a scatter plot of sea level data with two lines of best fit (1880–2050 and 2000–2050).
   - Save the plot as `sea_level_plot.png`.
   

## **Functionality**

### **Plot Generation**:
- **draw_sea_level_plot(filepath)**: Reads the dataset, creates a scatter plot, fits two lines of best fit (for 1880-2050 and 2000-2050), and saves the resulting plot as a PNG file.


## **Sample Plot Output**

The generated plot will look similar to this:

- **Blue dots**: Represent the historical sea level data points.
- **Red line**: Line of best fit for the data from 1880 to 2050.
- **Green line**: Line of best fit for the data from 2000 to 2050, showing more recent trends.
