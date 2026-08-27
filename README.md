# Advanced Data Analysis and Visualization in Logistics

An end-to-end Week 3 logistics analytics project using Python for exploratory data analysis, visualization, performance analysis, and operational recommendations.

## Objectives
- Perform exploratory data analysis (EDA)
- Analyze delivery times and delays
- Identify transportation cost drivers
- Compare shipping modes, regions, and product categories
- Study correlations among logistics variables
- Produce actionable logistics recommendations

## Technologies
Python • Pandas • NumPy • Matplotlib • Seaborn • Jupyter • python-docx

## Dataset
The cleaned dataset contains **2,001 shipment records** and 17 variables covering shipment details, dates, shipping modes, regions, product categories, priority, distance, weight, quantity, scheduled/actual delivery, shipping cost, sales value, delays, on-time status, and cost per unit.

## Key Findings
- **On-time delivery rate:** 52.2%
- **Delayed shipments:** 47.8%
- **Average delay among delayed shipments:** 1.50 days
- **Average shipping cost:** 94.05
- **Distance–shipping cost correlation:** 0.680
- Higher order quantities are associated with lower cost per unit.
- Regional and shipping-mode performance varies, creating opportunities for targeted improvement.

## Visualizations
1. Delivery-time distribution
2. Shipping-mode performance
3. Distance vs shipping cost
4. Regional performance
5. Monthly on-time trend
6. Product-category comparison
7. Correlation heatmap

## Repository Structure
```text
week3-logistics-data-analysis/
├── data/
├── notebooks/
├── scripts/
├── visualizations/
├── report/
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run
```bash
git clone https://github.com/YOUR_USERNAME/week3-logistics-data-analysis.git
cd week3-logistics-data-analysis
pip install -r requirements.txt
python scripts/week3_logistics_analysis.py
```

For the notebook:
```bash
jupyter notebook
```

Open `notebooks/Week3_Logistics_Analysis.ipynb`.

## Report
The complete DOC report is available under `report/`.

## Author
**Krishna Vinod**  
B.Tech – Artificial Intelligence & Data Science
