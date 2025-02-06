# InventoryZen

InventoryZen is a comprehensive inventory management system designed to help businesses efficiently track and manage their inventory, suppliers, orders, and customers. Built using modern web technologies, it provides a robust platform for managing stock levels, processing orders, and generating reports.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Management**: Secure user registration and authentication with role-based access control.
- **Product Management**: Add, update, and delete products with detailed information including name, manufacturer, stock levels, and descriptions.
- **Inventory Tracking**: Real-time tracking of product stock levels across multiple locations.
- **Sales Management**: Record and manage sales transactions, including product details, store location, quantity sold, and total sales amount.
- **Purchase Management**: Track purchase records with details such as purchase date, product, quantity purchased, and total purchase amount.
- **Store Management**: Manage multiple store locations with detailed information including title, name, category, address, and associated images.

## Technologies Used

- **Backend**: Node.js, Express.js
- **Database**: MongoDB with Mongoose ORM
- **Authentication**: JSON Web Tokens (JWT) for secure session management
- **Frontend**: React.js (if applicable)
- **Libraries**:
  - bcryptjs
  - connect-mongo
  - body-parser
  - cors
  - dotenv
  - express-session
  - express-validator
  - jsonwebtoken
  - mongoose
  - nodemon
  - validator
  - multer

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kunwar-Yuvraj/InventoryZen.git
   cd InventoryZen
   ```
2. **Install dependencies**:
   ```bash
   npm install
   ```
3. **Set up environment variables**:
   Create a `.env` file in the root directory and add the following variables:
   ```env
   PORT=5000
   JWT_SECRET=your-jwt-secret-key
   MONGO_URI=your-mongodb-connection-string
   ```
4. **Start the application**:
   ```bash
   npm run dev
   ```
   The application will be accessible at `http://localhost:5000`.

## Usage

- **User Registration and Authentication**: Users can register and log in to the system securely. Access to different functionalities is controlled based on user roles.
- **Managing Products**: Users can add new products, update existing product details, and delete products as needed.
- **Tracking Inventory**: The system provides real-time updates on product stock levels, helping users maintain optimal inventory across multiple store locations.
- **Handling Sales and Purchases**: Users can record sales transactions and purchases, keeping track of inventory flow.
- **Store Management**: Users can manage multiple store locations, including adding and updating store details.
- **Reporting and Analytics**: (If available) The system may generate reports and analytics for sales, inventory, and store performance.

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - User login
- `GET /api/auth/user` - Get authenticated user details

### Products
- `GET /api/products` - Get all products
- `POST /api/products` - Add a new product
- `GET /api/products/:id` - Get product by ID
- `PUT /api/products/:id` - Update product details
- `DELETE /api/products/:id` - Delete a product

### Inventory
- `GET /api/inventory` - Get inventory details
- `POST /api/inventory` - Add inventory records
- `PUT /api/inventory/:id` - Update inventory records

### Sales
- `GET /api/sales` - Get all sales transactions
- `POST /api/sales` - Add a new sale transaction

### Purchases
- `GET /api/purchases` - Get all purchase records
- `POST /api/purchases` - Record a new purchase

### Stores
- `GET /api/stores` - Get all stores
- `POST /api/stores` - Add a new store
- `PUT /api/stores/:id` - Update store details
- `DELETE /api/stores/:id` - Delete a store

## Contributing

Contributions are welcome! If you’d like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or support, reach out via [GitHub Issues](https://github.com/Kunwar-Yuvraj/InventoryZen/issues).

