import nmap
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint

# Initialize Rich Console & Nmap Scanner
console = Console()
nm = nmap.PortScanner()

# 1. Banner Header
console.print(
    Panel.fit(
        "[bold cyan]🌐 RECONNAISSANCE PORT SCANNER[/bold cyan]\n"
        "[italic gray]Automated Network Discovery Tool | Python + Nmap[/italic gray]",
        border_style="bold blue",
    )
)

# 2. Dynamic Target Input
target = input("\n[?] Enter IP Address or Domain to scan: ").strip()

if not target:
    console.print("[bold red]❌ Error: No target provided. Exiting...[/bold red]")
else:
    options = "-sV -F -Pn"

    # 3. Loading Spinner during scan
    with console.status(
        f"[bold yellow]Scanning target {target}... Please wait...[/bold yellow]",
        spinner="dots",
    ):
        try:
            nm.scan(target, arguments=options)
        except Exception as e:
            console.print(f"[bold red]❌ Scan Failed:[/bold red] {e}")
            nm = None

    # 4. Display Results in a Rich Table
    if nm and nm.all_hosts():
        for host in nm.all_hosts():
            hostname = nm[host].hostname() or "Unknown Host"
            host_state = nm[host].state()

            # Host Overview Badge
            console.print(
                f"\n[bold green]✔ Target Up:[/bold green] [bold white]{host}[/bold white] ({hostname}) | State: [cyan]{host_state}[/cyan]"
            )

            for protocol in nm[host].all_protocols():
                # Create a formatted table
                table = Table(
                    title=f"Protocol: {protocol.upper()}",
                    header_style="bold magenta",
                )
                table.add_column("Port", style="cyan", justify="center")
                table.add_column("State", justify="center")
                table.add_column("Service", style="yellow")
                table.add_column("Version Details", style="white")

                port_info = nm[host][protocol]
                for port, data in sorted(port_info.items()):
                    state = data.get("state", "unknown")
                    service = data.get("name", "unknown")
                    product = data.get("product", "")
                    version = data.get("version", "")
                    
                    # Full version string
                    version_info = f"{product} {version}".strip() or "N/A"

                    # Colorize state based on result
                    if state == "open":
                        colored_state = "[bold green]OPEN[/bold green]"
                    elif state == "filtered":
                        colored_state = "[yellow]FILTERED[/yellow]"
                    else:
                        colored_state = "[red]CLOSED[/red]"

                    table.add_row(
                        str(port), colored_state, service, version_info
                    )

                console.print(table)
    else:
        console.print("[bold red]⚠️ No active hosts or results found.[/bold red]")