# Vendor Management System API

## Overview

This Django-based Vendor Management System API provides endpoints to manage vendors, purchase orders, and track performance metrics.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django
- Django REST framework

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/TUSHAR-VERMA-star/Vendor-Management-System.git
    ```

2. **Change directory:**

    ```bash
    cd venderSystem
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - **Windows**

        ```bash
        venv\Scripts\activate
        ```

    - **Linux/Mac**

        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Vendors

- **GET /api/vendors/:** List all vendors.
- **POST /api/vendors/:** Create a new vendor.
- **GET /api/vendors/{id}/:** Retrieve details of a specific vendor.
- **PUT /api/vendors/{id}/:** Update a vendor.
- **DELETE /api/vendors/{id}/:** Delete a vendor.

### Purchase Orders

- **GET /api/purchase_orders/:** List all purchase orders.
- **POST /api/purchase_orders/:** Create a new purchase order.
- **GET /api/purchase_orders/{id}/:** Retrieve details of a specific purchase order.
- **PUT /api/purchase_orders/{id}/:** Update a purchase order.
- **DELETE /api/purchase_orders/{id}/:** Delete a purchase order.

### Vendor Performance

- **GET /api/vendors/{vendor_id}/performance/:** Retrieve performance metrics for a specific vendor.

### Acknowledge Purchase Order

- **POST /api/purchase_orders/{po_id}/acknowledge/:** Acknowledge a purchase order and update relevant metrics.

## Usage

Provide examples and details on how to use the API endpoints. Include sample requests and responses.

```json
Example POST request for creating a vendor:
{
    "name": "Daniel White",
    "contact_details": "7890123456",
    "address": "456 Oak Street",
    "vendor_code": "07",
    "on_time_delivery_rate": 92.5,
    "quality_rating_avg": 4.5,
    "average_response_time": 11.8,
    "fulfillment_rate": 96.2
}
OR
{
    "name": "Daniel White",
    "contact_details": "7890123456",
    "address": "456 Oak Street",
}

Example POST request for creating a purchase order:
{
    "po_number": "PO004",
    "vendor": 4,
    "order_date": "2023-12-18T14:00:00Z",
    "delivery_date": "2023-12-25T14:00:00Z",
    "items": [{"name": "Accessory C", "quantity": 8, "price": 18.0}],
    "quantity": 8,
    "status": "pending",
    "quality_rating": null,
    "issue_date": "2023-12-18T13:00:00Z",
    "acknowledgment_date": "2023-12-18T15:30:00Z"
}
