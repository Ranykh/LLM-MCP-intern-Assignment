# LLM-MCP-intern-Assignment

## Candidate Note
I’m truly excited about the opportunity to join Neuronics as an intern. This assignment was both inspiring and aligned with my technical interests—particularly in AI orchestration, real-time inference, and scalable systems. I would be thrilled to further discuss my solution, technical decisions, and potential improvements in a frontal technical interview.


## Project Overview

This repository provides a comprehensive, robust, and technically proficient solution to the intern assignment. It demonstrates the effective orchestration of an LLM agent (leveraging OpenAI's GPT integrated through LangChain) to dynamically interact with two simulated microservices—Image DB and YOLO Detector—via an MCP layer. The application efficiently fulfills user queries such as:

detect all cars in images between 11:00 and 11:05

## Technical Depth and Design Decisions

### LLM Agent for Dynamic Orchestration

The primary design decision was employing an LLM agent (LangChain), allowing the AI model to dynamically invoke appropriate tools based on free-form user queries. This approach provides significant flexibility and scalability, as it lets the AI autonomously determine the best tools and processes to fulfill complex missions.

### Modular and Scalable Design

The codebase is designed modularly:

- Image DB: Uses a structured database implemented via SQLAlchemy and SQLite, enabling efficient data querying and future scalability.

- YOLO Detector: Employs the YOLOv8 model (Ultralytics), chosen specifically for its balance of high speed, accuracy, and lightweight design suitable for edge deployment.

- Robust Error Handling: Includes retry mechanisms and timeouts to gracefully handle transient service issues, demonstrating awareness of microservice resiliency.

## PyTorch and Model Optimization

YOLOv8, built on PyTorch, was chosen for its edge-optimized performance, essential for deployment in resource-constrained environments like NVIDIA Jetson devices. Familiarity with PyTorch was leveraged to efficiently integrate YOLOv8. Additionally, the solution acknowledges the potential for optimization using NVIDIA TensorRT, highlighting awareness of techniques for further inference acceleration on NVIDIA hardware.

## Docker and Deployment

Docker was employed to ensure portability and ease of deployment. A lean Docker image (python:3.10-slim) was crafted, meticulously tested to confirm compatibility and reliability. Though this solution currently utilizes CPU-based inference for simplicity, considerations for GPU acceleration, specifically on NVIDIA Jetson platforms, are included. The provided Dockerfile can easily be extended to use NVIDIA’s CUDA-enabled base images and runtime for GPU-enhanced inference.

## SQLAlchemy Integration

To enhance scalability and maintainability, the original image filtering logic was upgraded to use SQLAlchemy with SQLite:

Defines a robust database schema.

Enables efficient querying and filtering by timestamp.

## Usage

### Prerequisites

Docker (recommended) or Python 3.10+

OpenAI API key set as an environment variable (OPENAI_API_KEY)

### Setup and Run with Docker

docker build -t mcp-agent .
docker run --rm -e OPENAI_API_KEY="your_key_here" mcp-agent \
"detect all cars in images between 11:00 and 11:05"

### Setup and Run Locally

pip install -r requirements.txt
export OPENAI_API_KEY="your_key_here"
python main.py "detect all cars in images between 11:00 and 11:05"

## Project Structure

- services/image_db.py: Database management and timestamp filtering using SQLAlchemy.

- services/yolo_detector.py: YOLOv8-based object detection with resiliency enhancements.

- agent.py: LangChain agent setup and tool orchestration.

- main.py: CLI entry point for executing missions.

## Future Enhancements (If i had more time what would i do)

- Natural language parsing of timestamps.

- Transitioning simulated services to production databases and API endpoints.

- GPU acceleration with NVIDIA TensorRT.

- Real-time video analysis integration via GStreamer or NVIDIA DeepStream.


