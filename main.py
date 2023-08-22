import multiprocessing
from shurasbot import ShurasBot

def process_function():
    bot = ShurasBot()
    bot.run_bot()

def main():
    num_processes = int(input("Введите количество процессов: "))
    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(target=process_function)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()

