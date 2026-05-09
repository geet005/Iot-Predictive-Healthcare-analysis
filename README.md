Predictive Patient Health Monitoring System
An IoT-based healthcare monitoring system that simulates patient vitals, predicts future heart rate trends using Machine Learning, and visualizes health insights through a Streamlit dashboard.

Features
•Simulated patient health data
•Heart rate prediction using Linear Regression
•Risk detection and alerts
•Interactive Streamlit dashboard
•Health trend visualization

Tech Stack
•Python
•Pandas
•NumPy
•Scikit-learn
•Matplotlib
•Streamlit

Project Structure
├── project.py          # ML model and prediction system
├── dash.py             # Streamlit dashboard
├── health_data.csv     # Simulated patient data

Run the Project
pip install pandas numpy matplotlib scikit-learn streamlit
python project.py
streamlit run dash.py

Risk Detection
High-risk cases are detected when:
•Heart Rate > 110 bpm
•SpO₂ < 92%
•Temperature > 38°C

Future Improvements
•Real IoT sensor integration
•Real-time health monitoring
•Advanced ML/DL prediction models
•SMS/Email alert system
•Cloud database integration
•Mobile app support

