# WebApp Essentials

WebApp Essentials is a simple web application built using FastAPI, SQLModel, and Docker. This project serves as a starting point for building web applications with these technologies.

A walkthrough of the project can be found at: [WebApp Essentials: a simple app using FastAPI, SQLModel, and Docker](https://medium.com/@japheth.yates/webapp-essentials-a-simple-app-using-fastapi-sqlmodel-and-docker-242cb7a85552).

## Getting Started

To get started with the `webapp_essentials` project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/webapp_essentials.git
    ```

2. Install the project dependencies using poetry:

    ```bash
    cd webapp_essentials
    poetry install
    ```

    or using pip:
    ```bash
    cd webapp_essentials
    pip install -r requirements.txt 

3. Run the application:

    ```bash
    make run
    ```
    or using full command:
    ```bash
    docker compose up --build -d
    ``` 

    The application will start running on `http://localhost:8004/docs#/`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
