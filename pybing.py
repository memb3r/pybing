import g4f
import time
from g4f.Provider import Bing
from rich.console import Console

console = Console()

console.print('''[bold blue]
 ____        ____  _             
|  _ \ _   _| __ )(_)_ __   __ _ 
| |_) | | | |  _ \| | '_ \ / _` |
|  __/| |_| | |_) | | | | | (_| |
|_|    \__, |____/|_|_| |_|\__, |[/][white] 1.0
       [blue]|___/               |___/[/] 
''')

console.print('[bold white on blue]Author:[/] memb3r')
console.print('[bold white on yellow]System Message:[/] Basically, the response is generated from 4 to 25 seconds, it all depends on its size.')
console.print('[bold white on red]Warning:[/] This program is made with [bold]g4f[/] library and this program is in no way associated with OpenAI or Microsoft.\n')

while True:
    promt = console.input('[bold white on blue]User:[/] ')
    console.print(f'[bold white on yellow]System Message:[/] [italic white]Loading response...[/]')
    start_time = time.time()
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        provider=g4f.Provider.Bing,
        messages=[{"role": "user", "content": promt}],
        stream=False
    )
    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    seconds, milliseconds = divmod(seconds, 1)
    milliseconds = int(milliseconds * 1000)
    formatted_time = f'{int(minutes)}m{int(seconds)}s{milliseconds}ms'
    console.print(f'[bold white on blue]Bing ({formatted_time}):[/] {response}')