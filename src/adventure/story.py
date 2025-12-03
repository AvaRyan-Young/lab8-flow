from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.theme import Theme
from rich.style import Style
from rich import print
from rich.prompt import Prompt

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[red]You stand still, unsure what to do. The forest swallows you.[/red]"

def left_path(event):
    return "[cyan]You chose left. [/cyan]" + event

def right_path(event):
    return "[magenta]You walk right. [/magenta]" + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[i]You wake up in a dark forest.[/i] You can go [cyan]left[/cyan] or [magenta]right.[/magenta]")
    while True:
        choice = Prompt.ask("[b]Which direction do you choose?[/b] ([cyan]left[/cyan]/[magenta]right[/magenta]/[red]exit[/red])", case_sensitive=False)
        choice = choice.strip()
        if choice == 'exit':
            break
        
        print(step(choice, events))