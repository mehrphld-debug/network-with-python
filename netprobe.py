#!/usr/bin/env python3

import platform
import socket
from datetime import datetime

import speedtest
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()


def bits_to_mbps(bits_per_second):
    return bits_per_second / 1_000_000


def run_speed_test():
    console.print("\n[bold cyan]Finding best server...[/bold cyan]\n")

    st = speedtest.Speedtest()

    st.get_best_server()

    console.print("[yellow]Testing download...[/yellow]")
    download = st.download()

    console.print("[yellow]Testing upload...[/yellow]")
    upload = st.upload()

    return st, download, upload


def display_results(st, download, upload):

    server = st.results.server
    client = st.results.client

    table = Table(title="Internet Benchmark")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(
        "Download",
        f"{bits_to_mbps(download):.2f} Mbps"
    )

    table.add_row(
        "Upload",
        f"{bits_to_mbps(upload):.2f} Mbps"
    )

    table.add_row(
        "Ping",
        f"{st.results.ping:.1f} ms"
    )

    table.add_row(
        "Server",
        server["name"]
    )

    table.add_row(
        "ISP",
        server["sponsor"]
    )

    table.add_row(
        "Country",
        server["country"]
    )

    table.add_row(
        "Public IP",
        client["ip"]
    )

    table.add_row(
        "OS",
        platform.system()
    )

    table.add_row(
        "Hostname",
        socket.gethostname()
    )

    table.add_row(
        "Time",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    console.print(table)


def main():

    console.print(
        Panel.fit(
            "[bold cyan]NETPROBE[/bold cyan]\n"
            "Network Diagnostic Laboratory"
        )
    )

    st, download, upload = run_speed_test()

    display_results(
        st,
        download,
        upload
    )

    console.print(
        "\n[bold green]✓ Test complete[/bold green]\n"
    )


if __name__ == "__main__":
    main()