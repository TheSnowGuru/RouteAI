![image](https://github.com/TheSnowGuru/RouteAI/assets/5313475/3e35a997-7737-49c8-80ba-d138a1b1bd94)

## Description

Welcome to RouteAI, the open-source wizard that makes API integration a breeze! Forget about those boring, tedious setups. With RouteAI, you just need a prompt, and voila! Get your payload and response served on a golden plate. It’s like having a magical butler for your APIs, ready to do all the heavy lifting while you sip your coffee and relax.

## Project Structure

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
├── payload_storage.py
├── README.md
├── test_api.py
├── utils.py
└── diff_generator.py
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

### New Feature: Token-Efficient Diff Generation

Say goodbye to wasting tokens! Our diff generation feature only sends changes, making your API interactions faster and cheaper. It's like sending just the juicy bits and skipping the fluff.

### New Feature: Learning and Saving API Call Payloads

RouteAI is smart enough to remember your API calls. Once it learns, it won't bug the AI model again. It just knows what to do, kind of like a well-trained pet but way cooler and more useful.

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd intelligent_router
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Set up environment variables:

```bash
export OPENAI_API_KEY='your_openai_api_key'
```

## Environment Variables

Make sure these variables are in your `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=1
```

## Running the Application

1. Start the API Gateway:

    ```bash
    python main.py
    ```

2. Make sure Kafka and Redis services are up and running.

3. Configure and start Traefik for load balancing. (It’s not as hard as it sounds, promise!)

## Testing the API

Want to see RouteAI in action? Use our `test_api.py` script. It’s like giving RouteAI a test drive, but without the hassle of insurance.

### Steps to Test

1. Ensure the API Gateway is running:

    ```bash
    python main.py
    ```

2. Run the test script:

    ```bash
    python test_api.py
    ```

Watch in amazement as the script sends various payloads and prints the responses.

## Usage

### Learning and Saving API Call Payloads

RouteAI learns your API calls so well, it feels like it’s reading your mind. Repeated calls are handled instantly using saved payloads. No more redundant API calls—just pure efficiency.

Send a POST request to the API Gateway with JSON data:

```http
POST /data
Content-Type: application/json

{
  "key": "value"
}
```


## License
This project is licensed under the MIT License.
