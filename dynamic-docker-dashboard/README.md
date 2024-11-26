Dynamic Docker Dashboard for Container Monitoring

A Flask-based web application for managing and monitoring Docker containers and system resources in real time. This dashboard enables users to create, view, and manage Docker containers, monitor system resource usage, and view container logs, all through a simple and intuitive web interface.
Features
1. Container Management

    Create new Docker containers by specifying:
        Container Name
        Image Name
        Ports
        Initial Status (Running/Stopped)
    View a list of all existing containers, including their:
        Image
        Name
        Ports
        Creation Time
        Status

2. Real-Time Monitoring

    System Monitoring:
        CPU Usage
        Memory Usage
        Disk Usage
    Container Resource Monitoring:
        CPU, Memory, and Network Usage of each running container (via docker stats).

3. Alerts System

    Proactively monitors system resources and Docker container performance.
    Generates alerts for:
        High CPU usage
        High Memory usage
        Low Disk Space
        Example conditions for unhealthy containers

4. Logs Viewer

    Fetch and display logs for individual containers using docker logs.
    Allows filtering logs by container name for troubleshooting.

Technology Stack
Backend:

    Flask (Python)
    psutil for system resource monitoring
    Subprocess for executing Docker commands

Frontend:

    HTML/CSS for a user-friendly interface
    Dynamic dropdowns and tab-based navigation

Tools:

    Docker for container management
    docker stats, docker ps, and docker logs commands

Prerequisites

    Install Docker
    Ensure Docker is installed and running on your system. Follow the Docker installation guide if needed.

    Install Python
    Ensure Python (>= 3.6) is installed. Check with:

python --version

Install Required Packages
Install the dependencies using pip:

    pip install flask psutil

    Run Docker Daemon
    Ensure the Docker daemon is running before starting the application.

Setup and Usage

    Clone the Repository:

git clone https://github.com/yourusername/docker-dashboard.git
cd docker-dashboard

Run the Flask App:

python app.py

Access the Dashboard: Open your browser and go to:

    http://127.0.0.1:5000/

    Explore Features:
        Navigate to different tabs for managing and monitoring containers and resources.
        Monitor logs, resource usage, and system alerts in real-time.

Project Structure

docker-dashboard/
├── templates/
│   ├── index.html                # Home Page
│   ├── Create_container.html     # Create Container Page
│   ├── All_container-list.html   # List Containers Page
│   ├── container_monitoring.html # Container Logs & Resource Monitoring
│   ├── system_monitoring.html    # System Monitoring Page
│   ├── alert.html                # Alerts Page
├── static/
│   ├── css/                      # Stylesheets
│       ├── style.css             # Main Stylesheet
├── app.py                        # Flask Application Code
├── README.md                     # Project Documentation

Screenshots
1. Home Page

2. Container List

3. Real-Time Monitoring

Future Enhancements

    Live Updates:
        Use a WebSocket or AJAX-based solution for dynamic updates without refreshing the page.
    Authentication:
        Add a login system  