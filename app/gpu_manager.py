import pynvml

def get_gpu_info():
    pynvml.nvmlInit()
    try:
        device_count = pynvml.nvmlDeviceGetCount()
        gpu_data = []

        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            info = {
                'id': i,
                'model': pynvml.nvmlDeviceGetName(handle).decode('utf-8'),
                'temperature': pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU),
                'utilization': pynvml.nvmlDeviceGetUtilizationRates(handle).gpu,
                'vram_used': pynvml.nvmlDeviceGetMemoryInfo(handle),
                'power_consumption': pynvml.nvmlDeviceGetPowerUsage(handle)
            }
            gpu_data.append(info)

        return gpu_data
    finally:
        pynvml.nvmlShutdown()
