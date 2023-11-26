# Overview

Welcome to Toy Robot Challenge! This simple web application allows users to control a virtual toy robot through a web interface.

## Diploying on local machine:

Follow these instructions to set up and run the Flask Toy Robot Challenge on your local machine.

### Prerequisites

- Python 3.x
- Flask
- Waitress

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/harshahadu/harsha_robot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd harsha_robot
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Start toy robot program:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000].

3. You will see the web interface to control the toy robot. Use the provided buttons and controls to move the robot.

### Usage
Now you will have to position the robot on the table-top using x,y coordinates and position value.
- **Enter x value**: You are allowed to enter a value between 0 to 4.
- **Enter y value**: You are allowed to enter a value between 0 to 4.
- **position**: You will only have four possible positions to choose ['NORTH','SOUTH','EAST','WEST']
Once the above requirements are satisfied you can place the robot on the table-top by clicking on the button place.

Now the robot is placed on the table-top and you can use the action menu placed at the botom of the table to control your robot.

## Diploying on local machine with Docker:

Follow these instructions to set up and run the Flask Toy Robot Challenge on your local machine with Docker.


### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/harshahadu/harsha_robot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd harsha_robot
    ```

3. Build a docker image with Dockerfile:

    ```bash
    docker build --tag harsha_robot .
    ```
4. Run the image locally in a Docker container:

    ```bash
    docker run --detach --publish 5000:50505 harsha_robot
    ```
5. Access the application with the given url:

     http://localhost:5000 

 
