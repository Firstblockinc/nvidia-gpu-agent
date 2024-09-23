import pynvml
import logging

logging.basicConfig(level=logging.INFO)

def get_gpu_info():
    pynvml.nvmlInit()
    try:
        device_count = pynvml.nvmlDeviceGetCount()
        gpu_data = []
    
        logging.info(f"Detected {device_count} GPU(s).")

        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)

            info = {
                'id': i,
                'model': pynvml.nvmlDeviceGetName(handle).decode('utf-8'),
                'temperature': pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU),
                'utilization': pynvml.nvmlDeviceGetUtilizationRates(handle).gpu,
                'vram_used': pynvml.nvmlDeviceGetMemoryInfo(handle).used,
                'vram_free': pynvml.nvmlDeviceGetMemoryInfo(handle).free,
                'vram_total': pynvml.nvmlDeviceGetMemoryInfo(handle).total,
                'power_consumption': pynvml.nvmlDeviceGetPowerUsage(handle)
            }
            gpu_data.append(info)


        return gpu_data
    except Exception as e:
        logging.error(f"An error occurred while getting GPU info: {e}")
    finally:
        pynvml.nvmlShutdown()
