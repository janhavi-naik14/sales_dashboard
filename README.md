
# Sales Dashboard Project

## Overview

This project involves creating a sales dashboard that utilizes SQL queries, Excel charts, and Python Pandas for data analysis and visualization. The final interactive dashboard is built using Dash, which allows for seamless integration of graphs and insights created in a Jupyter notebook.

## Installation

To get started with this project, follow the installation steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/janhavi-naik14/sales_dashboard.git
   cd <repository-directory>
   ```

2. **Install Required Libraries**:
   Ensure you have Python installed. Then, install the necessary libraries using pip:
   ```bash
   pip install dash dash-bootstrap-components plotly pandas
   ```

3. **Run the Dash Application**:
   Navigate to the directory containing `app.py` and run the Dash application:
   ```bash
   python app.py
   ```

## Project Description

The sales dashboard project consists of the following components:

- **Data Collection and Preparation**:
  - SQL queries were used to extract sales data from the database.
  - The data was then processed and cleaned using Python Pandas.

- **Data Visualization**:
  - Excel charts were initially used to visualize the sales data.
  - Advanced visualizations were created using Plotly in a Jupyter notebook.

- **Interactive Dashboard**:
  - The final dashboard was built using Dash.
  - The graphs created in the Jupyter notebook were saved as HTML files and embedded into the Dash application for an interactive frontend experience.

## Files and Structure

- `app.py`: The main Python script to run the Dash application.
- `projectds.csv`: The dataset used for analysis.
- `scatter_plot.html`: An example HTML file of a graph created in the Jupyter notebook.
- Additional HTML files for other graphs.

## Running the Application

Once the installation is complete, you can run the Dash application by executing:
```bash
python app.py
```
Then, open your web browser and navigate to the provided URL (e.g., `http://127.0.0.1:8050`). You should see the interactive dashboard with embedded graphs and insights.

## Conclusion

This project demonstrates the integration of SQL, Excel, and Python for comprehensive sales data analysis and visualization. The interactive dashboard built with Dash provides a powerful tool for exploring and understanding sales performance.
