# RouteAI
Open source new kind of AI Api, one endpoint to rule them all 

## Description
This project implements an intelligent routing system using OpenAI's API for data analysis, Kafka for message queuing, Redis for endpoint management, and Traefik for load balancing. The system is monitored using Prometheus and log data is managed using Loguru.

```
RouteAI/
│
├── api_gateway.py
├── message_queue.py
├── ai_model.py
├── endpoint_registry.py
├── load_balancer.py
├── monitor_logging.py
├── main.py
├── requirements.txt
└── README.md
```

## Overall Architecture with OpenAI Integration
```
[Client] --> [API Gateway (FastAPI)] --> [Message Queue (Kafka-python)] --> [AI Model (OpenAI API)] --> [Dynamic Endpoint Registry (Redis)]
                                                                                                     |
                                                                                                     v
                                                                                             [Load Balancer (Traefik/NGINX configurations)]
                                                                                                     |
        ---------------------------------------------------------------------------------------------------------------------------------
        |                          |                       |                                            |
[Endpoint 1]           [Endpoint 2]         [Endpoint 3]                    [Endpoint N]

```


## Installation

1. Clone the repository:
2. git clone <repository_url>
cd intelligent_router


2. Install the required dependencies:
pip install -r requirements.txt


3. Set up environment variables:
export OPENAI_API_KEY='your_openai_api_key'


## Running the Application

1. Start the API Gateway:
python main.py


2. Ensure Kafka and Redis services are running.
3. Configure and start Traefik for load balancing.

## Usage

Send a POST request to the API Gateway with JSON data:
POST /data
Content-Type: application/json

{
"key": "value"
}


## License
This project is licensed under the MIT License.
