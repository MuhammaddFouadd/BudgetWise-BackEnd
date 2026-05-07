# 💰 BudgetWise Backend

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" alt="Django" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase" />
</div>

<br />

A comprehensive and robust Django REST API backend designed for personal finance management. **BudgetWise** empowers users to track expenses, set budget limits, manage savings goals, and analyze their financial health with precision.

---

## 🌟 Key Features

- **🔐 Secure Authentication**: Robust session-based authentication with customizable user profiles and multi-currency support.
- **💸 Transaction Tracking**: Log, categorize, and monitor incomes and expenses seamlessly.
- **📊 Smart Analytics**: Generate real-time financial summaries, cash flow trends, and category-based breakdown reports.
- **🎯 Budget & Savings Planning**: Set dynamic monthly budgets, category-specific spending limits, and track progress towards savings goals.
- **🔔 Proactive Notifications**: Receive automated alerts for budget thresholds, upcoming bills, and important financial updates.

## 🏗️ System Architecture

```mermaid
graph TD
    Client([Frontend App / Browser]) -->|HTTP REST API| API[Django Routing & Middleware]
    
    subgraph BudgetWise Core System
        API --> Auth[Accounts App <br/> User Auth & Profiles]
        API --> Finance[Finance App <br/> Transactions & Budgets]
        API --> Planning[Planning App <br/> Goals & Limits]
        API --> Analytics[Analytics App <br/> Data Aggregation]
        API --> Notifications[Notifications App <br/> Alerts]
    end
    
    Auth --> DB[(PostgreSQL Database <br/> Hosted on Supabase)]
    Finance --> DB
    Planning --> DB
    Analytics -.-> Finance
    Notifications --> DB
```

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10+
- PostgreSQL (or local SQLite for dev)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/BudgetWise-BackEnd.git
   cd BudgetWise-BackEnd
   ```

2. **Set up the virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.myenv` file in the project root to securely store your connection strings:
   ```env
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

5. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create an Admin Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   > [!TIP]
   > Access the live admin panel at [https://budget-wise-back-end.vercel.app/admin/](https://budget-wise-back-end.vercel.app/admin/) or locally at `http://localhost:8000/admin/`.

## 📚 API Documentation

BudgetWise implements standard OpenAPI specifications. You can access the live documentation here:

- 🌍 **Production Swagger UI**: [https://budget-wise-back-end.vercel.app/api/docs/](https://budget-wise-back-end.vercel.app/api/docs/)
- 📖 **[Detailed Manual API Docs](./API_DOCUMENTATION.md)**: A comprehensive guide for frontend integration.
- 🔴 **ReDoc**: [https://budget-wise-back-end.vercel.app/api/redoc/](https://budget-wise-back-end.vercel.app/api/redoc/)
- 💻 **Local Docs**: `http://localhost:8000/api/docs/` (when running locally)

## 🧪 Testing

To ensure system integrity, run the built-in test suite:
```bash
python manage.py test
```