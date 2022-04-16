import psutil 
import humanfriendly 
import sys
import arrow
import os



system = f'{sys.platform.upper()}'
start = f'{arrow.get(psutil.boot_time()).humanize()}'
cpu_clock = psutil.cpu_freq()
cpu_clock = round(cpu_clock.current, 2) if cpu_clock else '???'
cpu_count = f'{psutil.cpu_count()} ({psutil.cpu_count(logical=False)})'
cpu_usage = f'{psutil.cpu_percent()}%'
cpu_clock = f'{cpu_clock} MHz'
avail_mem = psutil.virtual_memory().available
total_mem = psutil.virtual_memory().total
used_mem = humanfriendly.format_size(total_mem - avail_mem, binary=True)
total_mem = humanfriendly.format_size(total_mem, binary=True)





print('CPU Information')
print('===============================')
print(f'CPU Cores: {cpu_count}' )
print(f'CPU Usage: {cpu_usage}')
print(f'CPU Clock: {cpu_clock}')
print('===============================')
print('RAM Information')
print('===============================')
print(f'Used: {used_mem}')
print(f'Total: {total_mem}')
print('===============================')
print('System Information')
print('===============================')
print(f'Platform: {system}') 
print(f'Started: {start}')
print('===============================')



