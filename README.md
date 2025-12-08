# FastAPI Tutorial

A comprehensive guide for learning backend development with FastAPI from beginning to end.

## 📖 About

This repository contains a complete tutorial series for learning FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. 

## 🎯 Who Is This For? 

- Beginners who want to learn backend development
- Python developers looking to build modern APIs
- Anyone interested in learning FastAPI from scratch
- Developers wanting to understand RESTful API development

## ✨ Features

- **Comprehensive Learning Path**: Structured lessons from basics to advanced topics
- **Hands-on Examples**: Practical code examples for each concept
- **Best Practices**: Industry-standard patterns and practices
- **Database Integration**: Learn to work with databases using SQLAlchemy
- **Authentication & Authorization**: Implement secure API endpoints
- **Testing**: Write tests for your APIs
- **Deployment**: Learn how to deploy your FastAPI applications

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Basic knowledge of Python programming

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kusiyaitkrishna/fastapitutorial.git
cd fastapitutorial
```

2.  Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000` in your browser to see the application running.

## 📚 Tutorial Structure

### Module 1: Introduction
- What is FastAPI? 
- Setting up your development environment
- Your first FastAPI application
- Understanding automatic API documentation

### Module 2: Core Concepts
- Path parameters
- Query parameters
- Request body
- Response models
- Data validation with Pydantic

### Module 3: Database Integration
- Setting up SQLAlchemy
- Database models
- CRUD operations
- Database migrations with Alembic

### Module 4: Advanced Features
- Dependency injection
- Background tasks
- File uploads
- WebSockets
- Middleware

### Module 5: Security
- Authentication
- OAuth2 with JWT tokens
- Password hashing
- API key security

### Module 6: Testing & Deployment
- Writing tests with pytest
- Test coverage
- Docker containerization
- Deployment strategies

## 🛠️ Built With

- **FastAPI** - The web framework
- **Pydantic** - Data validation
- **SQLAlchemy** - ORM for database operations
- **Alembic** - Database migrations
- **Uvicorn** - ASGI server
- **Mako** - Template engine

## 📝 Documentation

Each module contains its own README with detailed explanations and examples. The code is well-commented to help you understand each concept.

FastAPI also provides automatic interactive API documentation:
- **Swagger UI**: Available at `http://127.0. 0.1:8000/docs`
- **ReDoc**: Available at `http://127.0. 0.1:8000/redoc`

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  Feel free to check the issues page. 

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📖 Additional Resources

- [Official FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SQLAlchemy Documentation](https://docs. sqlalchemy.org/)

## 📧 Contact

Krishna - [@kusiyaitkrishna](https://github.com/kusiyaitkrishna)

Project Link: [https://github.com/kusiyaitkrishna/fastapitutorial](https://github.com/kusiyaitkrishna/fastapitutorial)

## ⭐ Show Your Support

Give a ⭐️ if this project helped you learn FastAPI! 

## 📄 License

This project is open source and available for educational purposes.

---

**Happy Learning!  🚀**
