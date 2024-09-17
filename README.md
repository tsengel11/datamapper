
# DataMapper

DataMapper is a versatile and user-friendly application designed to seamlessly bridge the gap between APIs and databases. It empowers users to dynamically map API JSON objects to database records, convert database queries into API requests, and manage these processes through intuitive webhooks and schedulers. Whether you're looking to automate data synchronization, streamline data integration workflows, or build robust data pipelines, DataMapper provides the tools and flexibility you need.

## Key Features

### Dynamic Field Mapping

- **Intuitive Interface**: Easily map fields from API JSON objects to corresponding database columns using a graphical user interface.
- **Custom Transformations**: Apply transformation rules to data during the mapping process to ensure data integrity and consistency.
- **Multiple Mappings**: Support for multiple API endpoints and database tables, allowing for complex integration scenarios.

### Scheduler Control

- **Flexible Scheduling**: Schedule tasks to run at specified intervals (e.g., every minute, hourly, daily) to automate data synchronization.
- **Enable/Disable Tasks**: Toggle scheduler tasks on or off directly from the user interface.
- **Task Management**: Monitor and manage all scheduled tasks with ease.

### Webhook Handling

- **Real-Time Data Processing**: Receive and handle webhook events from external services in real-time.
- **Custom Actions**: Define actions to be triggered upon receiving specific webhook events, such as updating database records or initiating API requests.
- **Secure Webhooks**: Ensure secure communication with webhook sources through authentication and validation mechanisms.

### RESTful API

- **Comprehensive Endpoints**: Access all functionalities programmatically through a well-documented RESTful API.
- **Authentication**: Secure your API endpoints with robust authentication methods (e.g., OAuth2, JWT).
- **Scalability**: Designed to handle high volumes of requests and data seamlessly.

### User-Friendly Frontend

- **React-Based Interface**: A responsive and interactive frontend built with React, providing a smooth user experience.
- **Real-Time Updates**: Instant feedback and updates as you configure mappings, manage schedulers, and handle webhooks.
- **Accessible Design**: Designed for users of all technical backgrounds with clear navigation and intuitive controls.

### Extensible Architecture

- **Modular Design**: Easily extend and customize the application to fit unique requirements or integrate additional services.
- **Open Source**: Built with open-source technologies, allowing for community contributions and transparency.

## Technology Stack

### Backend

- **FastAPI**: A high-performance web framework for building APIs with Python.
- **SQLAlchemy**: An ORM (Object-Relational Mapper) for managing database interactions.
- **APScheduler**: A robust scheduler for managing timed tasks.
- **SQLite**: A lightweight, file-based database for simplicity (can be replaced with other databases as needed).
- **Pydantic**: For data validation and settings management using Python type annotations.

### Frontend

- **React**: A JavaScript library for building user interfaces.
- **Axios**: For making HTTP requests to the backend API.
- **React Hook Form**: For managing form state and validation.

### Other Tools

- **Uvicorn**: An ASGI server for running FastAPI applications.
- **Docker (Optional)**: For containerizing the application to ensure consistent environments across development and production.

## Project Structure

```
DataMapper/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── database.py
│   │   ├── crud.py
│   │   └── scheduler.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FieldMappingForm.js
│   │   │   ├── FieldMappingList.js
│   │   │   ├── SchedulerControl.js
│   │   │   └── WebhookHandler.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── styles.css
│   ├── package.json
│   └── README.md
├── docker-compose.yml (optional for containerization)
└── README.md
```

## Getting Started

### Prerequisites

#### Backend:
- Python 3.7+
- pip (Python package installer)

#### Frontend:
- Node.js (v14 or later)
- npm (Node package manager)

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/DataMapper.git
cd DataMapper
```

#### 2. Setup the Backend

```bash
cd backend
pip install -r requirements.txt
```

#### 3. Setup the Frontend

```bash
cd ../frontend
npm install
```

## Running the Application

#### 1. Start the Backend Server
From the backend directory:

```bash
uvicorn app.main:app --reload
```

The backend API will be available at [http://localhost:8000](http://localhost:8000).

#### 2. Start the Frontend Application
From the frontend directory:

```bash
npm start
```

The React frontend will be available at [http://localhost:3000](http://localhost:3000).

### Using Docker (Optional)

For ease of deployment and to ensure consistent environments, you can containerize the application using Docker.

#### 1. Ensure Docker is Installed

Download and install Docker for your operating system.

#### 2. Build and Run Containers

From the root DataMapper directory:

```bash
docker-compose up --build
```

This will build and start both the backend and frontend services.

The application will be accessible at [http://localhost:3000](http://localhost:3000) (frontend) and [http://localhost:8000](http://localhost:8000) (backend).

## API Documentation

FastAPI provides interactive API documentation accessible at [http://localhost:8000/docs](http://localhost:8000/docs) once the backend server is running. This interface allows you to explore and test all available API endpoints.

## Usage

#### 1. Dynamic Field Mapping

**Add New Mapping**:
- Navigate to the "New Field Mapping" section in the frontend.
- Enter the API Field and the corresponding DB Field.
- Click "Add Mapping" to save the mapping.

**View Mappings**:
- All existing field mappings are listed under the "Field Mappings" section.
- Each mapping displays the relationship between API fields and database fields.

#### 2. Scheduler Control

**Enable Scheduler**:
- Go to the "Scheduler Control" section.
- Click the "Enable Scheduler" button to start automated tasks.

**Disable Scheduler**:
- Click the "Disable Scheduler" button to stop automated tasks.

**Monitor Scheduler Status**:
- The current status (Enabled/Disabled) of the scheduler is displayed.

#### 3. Webhook Handling

**Send Webhook**:
- In the "Send Webhook" section, input your JSON payload.
- Click "Send Webhook" to dispatch the payload to the backend.

**Receive Webhook**:
- The backend logs all received webhook payloads.
- Customize the backend `handle_webhook` function to define actions upon receiving specific webhook events.

## Example Use Cases

- **Data Synchronization**: Automatically fetch data from an external API and store it in your database at regular intervals.
- **Real-Time Updates**: Handle webhook events from services like GitHub, Stripe, or Slack to update your database in real-time.
- **Data Transformation**: Map and transform incoming API data to match your database schema, ensuring consistency and integrity.
- **Automated Reporting**: Schedule tasks to generate reports based on the latest data from your APIs and databases.

## Contributing

DataMapper is an open-source project, and contributions are welcome! Whether you're fixing bugs, adding new features, or improving documentation, your help is appreciated.

### How to Contribute

1. **Fork the Repository**
2. **Create a Feature Branch**

```bash
git checkout -b feature/YourFeatureName
```

3. **Commit Your Changes**

```bash
git commit -m "Add some feature"
```

4. **Push to the Branch**

```bash
git push origin feature/YourFeatureName
```

5. **Open a Pull Request**

## License

This project is licensed under the MIT License.

## Acknowledgements

- FastAPI: For providing a high-performance framework for building APIs.
- React: For enabling the creation of dynamic and responsive user interfaces.
- APScheduler: For simplifying task scheduling in Python applications.
- SQLAlchemy: For robust and flexible ORM capabilities.
- Pydantic: For efficient data validation and management.

## Future Enhancements

- Authentication & Authorization: Implement user roles and permissions to secure the application.
- Advanced Data Transformations: Support complex data transformations during the mapping process.
- Multiple Database Support: Extend support to various databases like PostgreSQL, MySQL, etc.
- Enhanced Scheduler Features: Allow users to set custom intervals and manage multiple scheduled tasks.
- Improved Webhook Management: Provide a dashboard to view, manage, and test webhooks more effectively.
- Comprehensive Logging & Monitoring: Implement detailed logging and monitoring for better observability.
- User Notifications: Notify users about task statuses, errors, or important events via email or other channels.

## Contact

For questions, suggestions, or support, please contact bayartsengelt@gmail.com
