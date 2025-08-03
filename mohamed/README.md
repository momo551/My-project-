# Fashion Site - Django E-commerce Application

A fully functional e-commerce website for a fashion store built with Django.

## Features

- User authentication (registration, login, profile management)
- Product categories and browsing
- Product listings with search functionality
- Shopping cart system
- Checkout process with Stripe payment integration
- Order management
- Admin panel for managing products, categories, and orders
- Responsive design using Bootstrap
- Comprehensive test suite

## Requirements

- Python 3.8+
- Django 5.2
- Pillow 10.0.0
- Stripe 8.0.0

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mohamed
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Stripe keys:
   ```
   STRIPE_PUBLISHABLE_KEY=pk_test_...
   STRIPE_SECRET_KEY=sk_test_...
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Collect static files:
   ```
   python manage.py collectstatic
   ```

8. Run the development server:
   ```
   python manage.py runserver
   ```

## Project Structure

```
mohamed/
├── accounts/          # User authentication and profiles
├── cart/              # Shopping cart functionality
├── fashion_site/      # Main project settings
├── orders/            # Order management and checkout
├── products/          # Product models and views
├── static/            # CSS, JavaScript, and images
├── templates/         # HTML templates
├── manage.py          # Django management script
├── requirements.txt   # Project dependencies
└── README.md          # This file
```

## Testing

Run the test suite:
```
python manage.py test
```

## Admin Panel

Access the admin panel at `/admin/` to manage:
- Products
- Categories
- Orders
- User accounts

## Stripe Integration

To enable Stripe payments:

1. Sign up for a Stripe account at https://stripe.com
2. Obtain your publishable and secret keys
3. Add them to your `.env` file
4. Update the payment processing views in `orders/views.py` with actual Stripe integration

## Responsive Design

The site uses Bootstrap 5 for responsive design. All pages are mobile-friendly and will adapt to different screen sizes.

## Customization

You can customize the look and feel by modifying:
- Templates in the `templates/` directory
- CSS in `static/css/style.css`
- JavaScript in `static/js/script.js`

## License

This project is open source and available under the MIT License.
