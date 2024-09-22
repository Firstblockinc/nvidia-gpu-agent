# NVIDIA GPU HTTP Agent

A lightweight HTTP agent built with Flask for collecting and serving NVIDIA GPU metrics. This agent utilizes the NVIDIA Management Library (NVML) to monitor various GPU parameters, providing a simple interface for polling GPU data.

## Features

- Collects key GPU metrics including:
  - GPU Utilization
  - VRAM Usage (Total, Used, Free)
  - Temperature
  - Power Consumption
  - Fan Speed
  - Clock Speeds (Graphics and Memory)
  - Compute Mode
  - Active Processes
- Exposes a simple HTTP endpoint for retrieving GPU data.

## Requirements

- Python 3.x
- Flask
- NVIDIA NVML (included with NVIDIA drivers)
- `pynvml` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/nvidia-gpu-http-agent.git
   cd nvidia-gpu-http-agent
