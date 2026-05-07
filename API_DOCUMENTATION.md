# 🔌 BudgetWise API Documentation

> [!NOTE]
> **Base URL:** `https://budget-wise-back-end.vercel.app/`
> **Interactive Docs:** Test these endpoints live via Swagger UI at [https://budget-wise-back-end.vercel.app/api/docs/](https://budget-wise-back-end.vercel.app/api/docs/).

---

## 🔐 1. Authentication

The backend uses **Session Authentication**. For frontend applications (e.g. `localhost:3000`), CORS is enabled and you must send requests with credentials.

> [!IMPORTANT]  
> In your frontend API fetch calls, you must include `credentials: "include"` to ensure the session cookie is passed!

| Endpoint                | Method  | Description                                 |
| ----------------------- | ------- | ------------------------------------------- |
| `/auth/login/`          | `POST`  | Authenticate user and establish a session   |
| `/auth/logout/`         | `POST`  | Destroy the current session                 |
| `/auth/`                | `POST`  | Register a new user                         |
| `/auth/me/`             | `GET`   | Retrieve current authenticated user profile |
| `/auth/update_profile/` | `PATCH` | Update specific user profile fields         |

### Example Payloads

**Login Request:**

```json
{
  "email": "user@example.com",
  "password": "secret_password"
}
```

**Register Request:**

```json
{
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "secret_password"
}
```

---

## 💸 2. Finance Endpoints

All finance endpoints require the user to be fully authenticated.

### Categories

Manage transaction categories (e.g., Food, Salary, Rent).

| Endpoint                    | Method   | Description                           |
| --------------------------- | -------- | ------------------------------------- |
| `/finance/categories/`      | `GET`    | List all user & predefined categories |
| `/finance/categories/`      | `POST`   | Create a custom category              |
| `/finance/categories/{id}/` | `PATCH`  | Edit an existing category             |
| `/finance/categories/{id}/` | `DELETE` | Remove a category                     |

### Transactions

Track all income and expenses.

| Endpoint                      | Method   | Description          | Parameters / Queries                               |
| ----------------------------- | -------- | -------------------- | -------------------------------------------------- |
| `/finance/transactions/`      | `GET`    | List transactions    | `?type=expense`, `?category=3`, `?date_from=Y-M-D` |
| `/finance/transactions/`      | `POST`   | Create a transaction | Requires `type`, `amount`, `date`                  |
| `/finance/transactions/{id}/` | `PATCH`  | Edit a transaction   |                                                    |
| `/finance/transactions/{id}/` | `DELETE` | Delete a transaction |                                                    |

### Budgets & Limits

Plan your monthly spending limits.

| Endpoint                           | Method | Description                                                     |
| ---------------------------------- | ------ | --------------------------------------------------------------- |
| `/finance/budgets/`                | `GET`  | List monthly budgets (includes `spent` and `remaining` amounts) |
| `/finance/budgets/`                | `POST` | Create a new budget period                                      |
| `/finance/budget-category-limits/` | `GET`  | View spending limits assigned to specific categories            |
| `/planning/budget-limit/`          | `POST` | Set a new spending limit for a specific category                |

### Savings Goals

Set targets and track financial growth.

| Endpoint                                  | Method | Description                                           |
| ----------------------------------------- | ------ | ----------------------------------------------------- |
| `/finance/savings-goals/`                 | `GET`  | List savings goals alongside their current `progress` |
| `/finance/savings-goals/`                 | `POST` | Create a new savings goal                             |
| `/finance/savings-goals/{id}/contribute/` | `POST` | Add funds towards a specific goal                     |

---

## 📈 3. Analytics Endpoints

Extract insights from user financial data.

| Endpoint                        | Method | Description                                                                                |
| ------------------------------- | ------ | ------------------------------------------------------------------------------------------ |
| `/analytics/dashboard-summary/` | `GET`  | Returns an aggregate of `total_balance`, `monthly_income/expenses`, and `budget_warnings`. |
| `/analytics/budget-alert/`      | `GET`  | Retrieves category warnings with `progress_percentage` and `status_color`.                 |
| `/analytics/reports/`           | `GET`  | Fetch detailed chart data. Filter with `?start_date=` and `?end_date=`.                    |
| `/finance/reports/monthly/`     | `GET`  | Returns quick monthly totals (`?month=X&year=YYYY`).                                       |
| `/finance/reports/by_category/` | `GET`  | Returns totals grouped by category.                                                        |

---

## 🔔 4. Notifications

Manage systemic alerts for the user.

| Endpoint                                       | Method | Description                           |
| ---------------------------------------------- | ------ | ------------------------------------- |
| `/notifications/notifications/`                | `GET`  | List all notifications                |
| `/notifications/notifications/{id}/mark_read/` | `POST` | Mark a specific notification as read  |
| `/notifications/notifications/mark_all_read/`  | `POST` | Mark all unread notifications as read |

---

> [!TIP]
> Use tools like **Postman** or **Insomnia** to interact with these endpoints locally by sending the session cookie in your request headers.
