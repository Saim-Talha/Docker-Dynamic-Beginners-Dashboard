# Dynamic Docker Dashboard for Container Monitoring

A Flask-based web application for managing and monitoring Docker containers and system resources in real time. This dashboard provides a simple and intuitive interface to streamline container management, monitor system metrics, and track resource utilization effectively.

---

## Table of Contents

- Features
- Technology Stack
- Prerequisites
- Setup and Usage
- Project Structure
- Screenshots
- Future Enhancements
-  Contributing
- License

---

## Features

### **1. Container Management**
- **Create Containers**:  
  Create Docker containers with the ability to specify:
  - Container Name
  - Image Name
  - Ports
  - Initial Status (Running or Stopped)

- **View Containers**:  
  Display a list of all containers along with:
  - Image Name
  - Container Name
  - Ports Mapped
  - Creation Time
  - Current Status

### **2. Real-Time Monitoring**
- **System Monitoring**:
  - CPU Usage
  - Memory Usage
  - Disk Space Utilization
- **Container Monitoring**:
  - CPU, Memory, and Network usage of each container using `docker stats`.

### **3. Alerts System**
- Proactive alerts for:
  - High CPU Usage
  - High Memory Usage
  - Low Disk Space
- Threshold-based monitoring to ensure system health and performance.

### **4. Logs Viewer**
- Fetch and display logs for individual containers using the `docker logs` command.
- Ability to filter logs by container name for troubleshooting.

---

## Technology Stack

### **Backend**:
- **Flask**: Lightweight Python web framework.
- **psutil**: Library for monitoring system resources.
- **Subprocess**: For executing Docker CLI commands.

### **Frontend**:
- HTML/CSS for a simple and clean UI.

### **Tools**:
- Docker: For containerized applications.
- Flask Templates: To dynamically render pages.

---

## Prerequisites

1. **Install Docker**  
   Ensure Docker is installed on your system.  
   [Docker Installation Guide](https://docs.docker.com/get-docker/)

2. **Install Python**  
   Make sure Python 3.6 or later is installed. Check using:  
   ```bash
   python --version
