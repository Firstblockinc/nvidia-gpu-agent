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

            # Convert VRAM values to MB
            vram_used_mb = memory_info.used / (1024 ** 2)  
            vram_free_mb = memory_info.free / (1024 ** 2) 
            vram_total_mb = memory_info.total / (1024 ** 2) 

            info = {
                'id': i,
                'model': pynvml.nvmlDeviceGetName(handle),
                'temperature': pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU),
                'utilization': pynvml.nvmlDeviceGetUtilizationRates(handle).gpu,
                'vram_used': vram_used_mb,
                'vram_free': vram_free_mb,
                'vram_total': vram_total_mb,
                'power_consumption': pynvml.nvmlDeviceGetPowerUsage(handle)
            }
            gpu_data.append(info)


        return gpu_data
    except Exception as e:
        logging.error(f"An error occurred while getting GPU info: {e}")
    finally:
        pynvml.nvmlShutdown()
