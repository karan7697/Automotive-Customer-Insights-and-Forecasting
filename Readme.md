# Automotive Customer Insights and Sales Forecasting

## Project Overview
This project involves engineering a data analysis solution with time series analysis and feature engineering to provide actionable insights into customer behavior, vehicle preferences, and market trends. The goal is to increase customer retention, boost sales, and improve decision-making.

## Tech Stack
- **Snowflake**: Data warehousing
- **Feature Engineering**: Creating meaningful features from raw data
- **Scikit-Learn**: Machine learning
- **Prophet**: Time series forecasting

## Project Structure
- **data/**: Contains datasets used in the project
- **notebooks/**: Jupyter notebooks for exploratory data analysis (EDA) and model development
- **src/**: Source code for data processing, feature engineering, model training, and evaluation
- **requirements.txt**: List of dependencies
- **config/**: Configuration files
- **results/**: Results of the analysis and models

## How to Run
1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/automotive-customer-insights.git
    ```
2. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```
3. Configure the Snowflake connection in `config/snowflake_config.py`.
4. Run the data processing and model training scripts
    ```bash
    python src/data_processing.py
    python src/feature_engineering.py
    python src/model_training.py
    ```

## Results
- Customer behavior insights
- Vehicle preferences analysis
- Sales forecasting

## License
This project is licensed under the KP License.
