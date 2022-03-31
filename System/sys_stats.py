import click
import psutil
import humanfriendly
@click.command()
@click.option('--task', default='all', help='all, cpu or ram')
def sys_stats(task):
  click.echo('getting stats %s' % task)
  if (task == 'cpu' or task == 'all'):
    cpu_stats = f'Count: {psutil.cpu_count()}\n Usage: {psutil.cpu_percent()}'
    click.echo(cpu_stats)
  if (task == 'ram' or task == 'all'):
    ram_stats = f'Total: {psutil.virtual_memory().total}\n Used: {psutil.virtual_memory().available}'
   
    click.echo(ram_stats)

if __name__ == '__main__':
  sys_stats()
