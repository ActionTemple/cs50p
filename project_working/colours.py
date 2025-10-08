from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text

console = Console()
layout = Layout()

layout.split(
    Layout(name="header", size=3),
    Layout(name="main", ratio=1),
    Layout(name="footer", size=3)
)

layout["header"].update(Panel("The Big House", style="bold white on blue"))
layout["footer"].update(Panel("Inventory: torch", style="white on black"))

# This will hold all the "in-game" output
#main_text = Text("Welcome!\n", style="white on black")
main_text = Text()

while True:
    console.clear()
    layout["main"].update(Panel(main_text, style="white on black"))
    console.print(layout)

    user_input = input("What's next? ")

    # Append input and placeholder response to main text
    main_text.append(f"> {user_input}\n", style="bold green")
    main_text.append("You typed something...\n", style="white")
