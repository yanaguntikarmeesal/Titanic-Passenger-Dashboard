# 🚢 Titanic Passenger Dashboard

An interactive **Titanic Passenger Data Analysis Dashboard** built with **Python, Streamlit, Pandas, NumPy, and Plotly**.

The dashboard provides an interactive way to explore Titanic passenger information, survival patterns, passenger classes, age distribution, fares, embarkation ports, and survival rates.

---

## 📌 Project Overview

The **Titanic Passenger Dashboard** is an interactive data visualization project designed to analyze passenger information from the Titanic dataset.

Users can apply filters and instantly explore how different factors such as:

* 👨‍👩‍👧 Passenger sex
* 🎟️ Passenger class
* 🎂 Age
* 💰 Fare
* 🚢 Survival status
* 📍 Embarkation port

are related to passenger survival.

The application loads the Titanic dataset from `titanic.csv` and creates derived fields for easier analysis.

---

## ✨ Features

### 🔍 Interactive Filters

The sidebar provides filters for:

* Survival Status
* Passenger Class
* Sex
* Age Range
* Fare Range

These filters dynamically update the dashboard and visualizations.

### 📊 KPI Cards

The dashboard displays important statistics including:

* Total Passengers
* Survivors
* Deaths
* Survival Rate
* Average Age
* Average Fare

The metrics are calculated dynamically according to the selected filters.

### 📈 Interactive Visualizations

The dashboard contains several Plotly visualizations:

#### 👫 Survival by Sex

Compares the number of survivors and deaths between male and female passengers.

#### 🎟️ Survival by Passenger Class

Analyzes survival across:

* 1st Class
* 2nd Class
* 3rd Class

#### 📊 Age Distribution

Displays passenger age distribution based on survival status.

#### 💰 Fare Distribution

Uses box plots to compare passenger fares between survivors and non-survivors.

#### 📍 Survival by Embarkation Port

Analyzes survival according to embarkation port.

#### 🔥 Survival Rate Heatmap

Shows survival rates based on the combination of:

* Sex
* Passenger Class

These visualizations are implemented using Plotly Express.

---

## 📋 Data Tables

The dashboard also provides:

### Survival Rate Table

Displays:

* Sex
* Passenger Class
* Survivors
* Total passengers
* Survival rate

### Sample Passenger Table

Displays sample passenger information including:

* Passenger ID
* Name
* Sex
* Age
* Class
* Fare
* Embarkation port
* Survival status

---

## 🛠️ Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| 🐍 Python    | Programming language           |
| 🎈 Streamlit | Interactive web dashboard      |
| 🐼 Pandas    | Data manipulation              |
| 🔢 NumPy     | Numerical operations           |
| 📊 Plotly    | Interactive data visualization |
| 📄 CSV       | Dataset storage                |

---

## 📂 Project Structure

```text
Titanic-Dashboard/
│
├── app.py
├── titanic.csv
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/titanic-dashboard.git
```

### 2. Open the Project Folder

```bash
cd titanic-dashboard
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📄 requirements.txt

Create a file named `requirements.txt`:

```text
streamlit
pandas
numpy
plotly
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Dataset

The project uses a Titanic passenger dataset stored as:

```text
titanic.csv
```

The application reads the CSV file using Pandas:

```python
df = pd.read_csv("titanic.csv")
```

It also creates additional labels such as:

```text
Survived_Label
Pclass_Label
```

and handles numeric conversion and missing embarkation values.

---

## 📈 Dashboard Sections

```text
🚢 Titanic Passenger Dashboard
│
├── 🔍 Sidebar Filters
│   ├── Survival Status
│   ├── Passenger Class
│   ├── Sex
│   ├── Age Range
│   └── Fare Range
│
├── 📊 KPI Metrics
│   ├── Total Passengers
│   ├── Survivors
│   ├── Deaths
│   ├── Average Age
│   └── Average Fare
│
├── 📈 Charts
│   ├── Survival by Sex
│   ├── Survival by Class
│   ├── Age Distribution
│   ├── Fare Distribution
│   └── Survival by Embarkation
│
├── 🔥 Survival Rate Heatmap
│
├── 📋 Survival Rate Table
│
└── 🧾 Sample Passengers
```

---

## 🎯 Key Analysis Questions

This dashboard can be used to answer questions such as:

1. What percentage of passengers survived?
2. Did female passengers have a higher survival rate?
3. Which passenger class had the highest survival rate?
4. How does age relate to survival?
5. How does fare relate to survival?
6. Which embarkation port had the highest number of survivors?
7. How does survival differ between male and female passengers?
8. How does passenger class affect survival?

---

## 💡 Learning Objectives

This project demonstrates practical skills in:

* Python programming
* Data cleaning
* Exploratory Data Analysis
* Pandas DataFrame operations
* Data filtering
* GroupBy operations
* Pivot tables
* Data visualization
* Interactive dashboards
* Streamlit application development
* Plotly visualization
* GitHub project development

---

## 🎨 Dashboard Design

The application includes custom CSS to create a polished dashboard interface with:

* Metric cards
* Rounded corners
* Shadows
* Hover effects
* Custom backgrounds
* Styled headings
* Responsive Streamlit layout

The dashboard is configured with a wide layout and an expanded sidebar.

---

## 🚀 Future Improvements

Possible future enhancements include:

* 🤖 Titanic survival prediction using Machine Learning
* 📥 CSV download button
* 📊 Additional statistical analysis
* 📈 More interactive charts
* 🧠 Machine Learning prediction page
* 🔮 Passenger survival prediction form
* 🌐 Deploy the dashboard on Streamlit Community Cloud
* 📱 Improve mobile responsiveness

---

## ☁️ Deployment

This project can be deployed using **Streamlit Community Cloud**.

Basic deployment steps:

1. Upload the project to GitHub.
2. Make sure `app.py`, `titanic.csv`, and `requirements.txt` are included.
3. Connect the GitHub repository to Streamlit Community Cloud.
4. Select `app.py` as the main application file.
5. Deploy the application.

---

## 📸 Dashboard Preview

Add screenshots of your dashboard here:

```text
screenshots/
├── dashboard.png
├── filters.png
└── charts.png
```

Example Markdown:

```markdown
![Titanic Dashboard](screenshots/dashboard.png)
```

---

## 👨‍💻 Author

**Yanaguntikar Meesal**

📧 Email: `yanaguntikarm@gmail.com`

---

## ⭐ Support

If you found this project useful, please consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is created for **educational and portfolio purposes**.

---

### 🚢 Titanic Passenger Dashboard

**Built with Python + Streamlit + Pandas + NumPy + Plotly**

> Explore Titanic passenger data through interactive filters, KPIs, charts, heatmaps, and tables.
