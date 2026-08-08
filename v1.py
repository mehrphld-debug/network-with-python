#!/usr/bin/env python3

import platform
import socket
from datetime import datetime

import speedtest
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def mbps(bits):
    return bits / 1_000_000


console.print()

console.rule("[bold cyan]Neural Network Speed Test[/bold cyan]")

console.print("Finding best server...\n")

st = speedtest.Speedtest()

st.get_best_server()

download = st.download()

upload = st.upload()

ping = st.results.ping

server = st.results.server

table = Table(title="Internet Benchmark")

table.add_column("Metric", style="cyan")
table.add_column("Value", style="green")

table.add_row("Download", f"{mbps(download):.2f} Mbps")

table.add_row("Upload", f"{mbps(upload):.2f} Mbps")

table.add_row("Ping", f"{ping:.1f} ms")

table.add_row("ISP", server["sponsor"])

table.add_row("Server", server["name"])

table.add_row("Country", server["country"])

table.add_row("Public IP", st.results.client["ip"])

table.add_row("OS", platform.platform())

table.add_row("Hostname", socket.gethostname())

table.add_row(
    "Time",
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

console.print(table)

console.print()

console.print(
    Panel.fit(
        "[bold green]Test Complete ✓[/bold green]"
    )
)