import argparse
import sys
import pynvml

class GPUManager:
    def __init__(self):
        # Initialize NVML library
        pynvml.nvmlInit()

    def __del__(self):
        # Clean up NVML resources
        pynvml.nvmlShutdown()

    def get_temperature(self, gpu_id):
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_id)
        return pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

    def get_power(self, gpu_id):
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_id)
        return pynvml.nvmlDeviceGetPowerUsage(handle) / 1000  

    def get_memory(self, gpu_id):
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_id)
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        return mem_info.used / (1024 * 1024)  

