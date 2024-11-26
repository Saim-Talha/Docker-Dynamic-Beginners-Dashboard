import time

from flask import Flask,render_template,request
import os
import subprocess
import json
import psutil

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_container", methods=['GET','POST'])
def create_container():
    if request.method == "POST":
        container_name= request.form.get('container_name')
        image_name= request.form.get('image')
        ports= request.form.get('ports')
        status= request.form.get('status')

        try:
            if status == 'Running':
                os.system(f"docker run -dit --name {container_name} -p {ports} {image_name}")
                msg="Container created successfully"
                return render_template("Create_container.html",msg=msg)

            else:
                os.system(f"docker run -dit --name {container_name} -p {ports} {image_name}")
                os.system(f"docker stop {container_name}")
                msg = "Created container successfully"

                return render_template("Create_container.html",msg=msg)
        except Exception as e:
            msg=f"An error occured {e}"
            return render_template(render_template("Create_container.html",msg=msg))
    return render_template("Create_container.html")


@app.route("/container_list", methods=["GET"])
def container_list():
    try:
        # Safely execute the Docker command
        result = subprocess.run(
            ["docker", "ps", "-a", "--format", "{{json .}}"],
            capture_output=True,
            text=True,
            check=True
        )
        data = result.stdout.strip()

        # Parse the JSON output
        containers = []
        if data:  # Ensure there's output to process
            lines = data.split("\n")
            for line in lines:
                container = json.loads(line)  # Convert JSON string to a dictionary
                containers.append({
                    "image": container.get("Image", "N/A"),
                    "name": container.get("Names", "N/A"),
                    "ports": container.get("Ports", "None"),
                    "created_at": container.get("CreatedAt", "N/A"),
                    "status": container.get("Status", "N/A"),
                })

        # Pass structured data to the template
        return render_template("All_container-list.html", containers=containers)

    except subprocess.CalledProcessError as e:
        # Handle errors with the Docker command
        error_message = f"Error running Docker command: {e}"
        return render_template("error.html", error=error_message)

    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        error_message = f"Error parsing Docker output: {e}"
        return render_template("error.html", error=error_message)


@app.route('/system_monitoring')
def system_monitoring():
    # Get CPU and memory usage
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/')
    free_space = disk_usage.percent

    while True:
        time.sleep(1)
        return render_template('system_monitoring.html', cpu=cpu_usage, memory=mem_usage,storage=free_space)

def check_system_alerts():
    """Check system metrics and generate alerts if thresholds are exceeded."""
    alerts = []

    # Define thresholds
    cpu_threshold = 80  # CPU usage above 80%
    memory_threshold = 90  # Memory usage above 90%
    disk_threshold = 90  # Disk usage above 90%

    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > cpu_threshold:
        alerts.append(f"High CPU usage detected: {cpu_usage:.2f}% (Threshold: {cpu_threshold}%)")

    # Check memory usage
    memory = psutil.virtual_memory()
    if memory.percent > memory_threshold:
        alerts.append(f"High memory usage detected: {memory.percent:.2f}% (Threshold: {memory_threshold}%)")

    # Check disk usage
    disk = psutil.disk_usage('/')
    if disk.percent > disk_threshold:
        alerts.append(f"Low disk space: {100 - disk.percent:.2f}% free (Threshold: {disk_threshold}% used)")

    # Check Docker-specific alerts (e.g., container crashes)
    # Example logic: Placeholder for future Docker-specific alerts
    # alerts.append("Docker-specific alert: Example container stopped unexpectedly.")

    return alerts

@app.route('/alerts')
def alerts_page():
    """Render the alerts page."""
    alerts = check_system_alerts()
    return render_template('alert.html', alerts=alerts)

@app.route('/logs')
def fetch_logs():
    container_name = request.args.get('container_name', '')
    logs = []
    if container_name:
        try:
            result = subprocess.run(
                ['docker', 'logs', container_name],
                capture_output=True,
                text=True,
                check=True
            )
            logs = result.stdout.splitlines()
        except subprocess.CalledProcessError as e:
            logs = [f"Error fetching logs: {e}"]

    return render_template('container_monitoring.html', logs=logs, resource_usage=None, alerts=None)

@app.route('/container_monitoring')
def monitoring_dashboard():
    resource_usage = []
    alerts = []
    try:
        # Fetch resource usage from `docker stats`
        result = subprocess.run(
            ['docker', 'stats', '--no-stream', '--format', '{{json .}}'],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().splitlines()
        for line in lines:
            data = json.loads(line)
            resource_usage.append({
                'name': data.get('Name', 'N/A'),
                'cpu': data.get('CPUPerc', '0%'),
                'memory': data.get('MemPerc', '0%'),
                'network': data.get('NetIO', 'N/A'),
            })

        # Identify unhealthy containers (example condition)
        for container in resource_usage:
            if float(container['cpu'].strip('%')) > 80:  # Example alert condition
                alerts.append(f"High CPU usage in container {container['name']} ({container['cpu']}%)")

    except subprocess.CalledProcessError as e:
        alerts.append(f"Error fetching container stats: {e}")

    return render_template('container_monitoring.html', logs=None, resource_usage=resource_usage, alerts=alerts)


if __name__ == '__main__':
    app.run(debug=True)
