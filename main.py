from services.gpu_manager import GPUManager
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='GPU Information Fetcher')
    parser.add_argument('--gpu', type=int, help='Get information for specific GPU (e.g., --gpu 0)', required=True)
    parser.add_argument('--temp', action='store_true', help='Get GPU temperature')
    parser.add_argument('--power', action='store_true', help='Get GPU power consumption')
    parser.add_argument('--memory', action='store_true', help='Get GPU memory usage')
    parser.add_argument('--raw', action='store_true', help='Get only the raw value')
    return parser.parse_args()

def main():
    args = parse_arguments()
    gpu_manager = GPUManager()
    
    gpu_id = args.gpu

    if args.temp:
        temp = gpu_manager.get_temperature(gpu_id)
        if args.raw:
            print(temp)
        else:
            print(f"GPU {gpu_id} Temp: {temp}°C")
        return

    if args.power:
        power = gpu_manager.get_power(gpu_id)
        if args.raw:
            print(power)
        else:
            print(f"GPU {gpu_id} Power: {power} Watts")
        return

    if args.memory:
        memory = gpu_manager.get_memory(gpu_id)
        if args.raw:
            print(memory)
        else:
            print(f"GPU {gpu_id} Memory: {memory} MiB")
        return
    
    if not args.raw:
        print(f"GPU {gpu_id} Info:")
        print(f" - Temperature: {gpu_manager.get_temperature(gpu_id)}°C")
        print(f" - Power Usage: {gpu_manager.get_power(gpu_id)} Watts")
        print(f" - Memory Usage: {gpu_manager.get_memory(gpu_id)} MiB")
    else:
        print(gpu_manager.get_temperature(gpu_id))
        print(gpu_manager.get_power(gpu_id))
        print(gpu_manager.get_memory(gpu_id))

if __name__ == "__main__":
    main()