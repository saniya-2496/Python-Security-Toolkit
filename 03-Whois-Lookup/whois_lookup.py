from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import whois

console = Console()


def get_whois_info(domain: str):
    """Fetches detailed WHOIS information using the python-whois library."""
    try:
        data = whois.whois(domain)
        return data
    except Exception as e:
        return None


def format_field(value):
    """Helper function to format lists or missing values cleanly."""
    if not value:
        return "N/A / Redacted for Privacy"
    if isinstance(value, list):
        # Filter out duplicates while preserving order
        unique_vals = list(dict.fromkeys([str(v) for v in value]))
        return "\n".join(unique_vals)
    return str(value)


def main():
    # Header Banner
    console.print(
        Panel.fit(
            "[bold cyan]WHOIS DOMAIN RECONNAISSANCE[/bold cyan]\n"
            "[italic gray]Detailed Domain & Ownership Lookup | Python + Rich[/italic gray]",
            border_style="bold blue",
        )
    )

    # Input Prompt
    target = Prompt.ask("\n[?] Enter Domain Name (e.g., facebook.com)").strip()

    if not target:
        console.print("[bold red]Error: No domain provided. Exiting...[/bold red]")
        return

    # Query Execution
    with console.status(
        f"[bold yellow]Querying registrar database for {target}...[/bold yellow]",
        spinner="dots",
    ):
        domain_info = get_whois_info(target)

    if not domain_info or not domain_info.domain_name:
        console.print(
            f"[bold red]Error: Could not retrieve WHOIS record for '{target}'.[/bold red]"
        )
        return

    # Create Summary Table
    table = Table(
        title=f"WHOIS Record: {target}",
        show_header=True,
        header_style="bold magenta",
        border_style="cyan",
    )
    table.add_column("Attribute", style="bold white", width=20)
    table.add_column("Details", style="green")

    # Add Extracted Fields
    table.add_row("Domain Name", format_field(domain_info.domain_name))
    table.add_row("Registrar", format_field(domain_info.registrar))
    table.add_row("Organization / Owner", format_field(domain_info.org))
    table.add_row("Registrant Name", format_field(domain_info.name))
    table.add_row("Registrant Country", format_field(domain_info.country))
    table.add_row("Creation Date", format_field(domain_info.creation_date))
    table.add_row("Expiration Date", format_field(domain_info.expiration_date))
    table.add_row("Name Servers", format_field(domain_info.name_servers))

    # Display Table Output
    console.print(table)

    # Privacy Note
    console.print(
        "\n[italic gray]Note: Many major domains redact personal owner names and emails under GDPR/Privacy regulations. "
        "In such cases, the 'Organization' or 'Registrant' field will display privacy proxy details.[/italic gray]"
    )


if __name__ == "__main__":
    main()