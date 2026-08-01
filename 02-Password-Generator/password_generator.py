import random
import string
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


def generate_password(length: int = 15) -> str:
    """Generates a random password of given length."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(alphabet) for _ in range(length))


def main():
    # 1. Header Banner
    console.print(
        Panel.fit(
            "[bold cyan]🔑 SECURE PASSWORD GENERATOR[/bold cyan]\n"
            "[italic gray]CLI Utility | Python + Rich[/italic gray]",
            border_style="bold blue",
        )
    )

    # 2. Dynamic Length Input
    user_input = Prompt.ask(
        "\n[?] Enter password length (4-15)",
        default="15",
    )

    # 3. Validation Logic (Min 4, Max 15)
    try:
        length = int(user_input)
        if length < 4:
            console.print(
                "[bold yellow]⚠️ Warning: Password length too short. Setting to minimum (4).[/bold yellow]"
            )
            length = 4
        elif length > 15:
            console.print(
                "[bold yellow]⚠️ Warning: Maximum length is 15. Setting to 15.[/bold yellow]"
            )
            length = 15
    except ValueError:
        console.print(
            "[bold red]❌ Invalid input! Please enter numbers only. Defaulting to 15.[/bold red]"
        )
        length = 15

    # 4. Generate & Display
    password = generate_password(length)

    console.print(
        Panel(
            f"[bold green]{password}[/bold green]",
            title="[bold white]Generated Password[/bold white]",
            border_style="green",
            expand=False,
        )
    )


if __name__ == "__main__":
    main()