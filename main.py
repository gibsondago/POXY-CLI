"""
Proxy Manager CLI - Main Application

Author: Rezaul Karim
Email: work.rezaul@outlook.com
Powered By: REZ LAB

Main CLI application with rich formatting.
"""

import argparse
import sys
import subprocess
import platform
from config_manager import *
from proxy_server import *

# Import rich for better formatting and colors
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm

console = Console()

def show_help_information():
    """Display comprehensive help and usage information."""
    console.print(Panel(
        "[bold blue]🚀 Proxy Manager CLI - Help & Usage Guide[/bold blue]\n\n"
        "A powerful command-line tool for managing HTTP/SOCKS proxies across multiple platforms.\n\n"
        "[bold yellow]📖 What is Proxy Manager CLI?[/bold yellow]\n"
        "• Manage proxy server configurations easily\n"
        "• Support for HTTP, SOCKS4, and SOCKS5 proxies\n"
        "• Cross-platform compatibility (Windows, macOS, Linux)\n"
        "• Interactive menu system for ease of use\n"
        "• Both system-wide and local proxy modes\n\n"

        "[bold yellow]🔧 Supported Proxy Types:[/bold yellow]\n"
        "• [bold cyan]HTTP[/bold cyan]   - Standard HTTP proxy servers\n"
        "• [bold cyan]SOCKS4[/bold cyan] - SOCKS version 4 protocol\n"
        "• [bold cyan]SOCKS5[/bold cyan] - SOCKS version 5 protocol (recommended)\n\n"

        "[bold yellow]⚙️ Activation Modes:[/bold yellow]\n"
        "• [bold green]Local Mode[/bold green]  - Start a local proxy server on localhost:8080\n"
        "  💡 [italic]Recommended for most users[/italic]\n"
        "  💡 Configure applications to use localhost:8080\n"
        "  💡 No admin privileges required\n\n"

        "• [bold yellow]System Mode[/bold yellow] - Set system-wide proxy settings\n"
        "  ⚠️  [italic]Requires administrator/root privileges[/italic]\n"
        "  ⚠️  Affects all applications system-wide\n"
        "  ⚠️  May require restart of some applications\n\n"

        "[bold yellow]📋 Menu Options:[/bold yellow]\n"
        "• [bold cyan]1 - List Profiles[/bold cyan]  - View all saved proxy configurations\n"
        "• [bold cyan]2 - Add Profile[/bold cyan]   - Create a new proxy configuration\n"
        "• [bold cyan]3 - Delete Profile[/bold cyan]- Remove an existing proxy configuration\n"
        "• [bold cyan]4 - Use Profile[/bold cyan]   - Activate a proxy configuration\n"
        "• [bold cyan]5 - Help[/bold cyan]         - Show this help information\n"
        "• [bold cyan]0 - Exit[/bold cyan]         - Close the application\n\n"

        "[bold yellow]💡 Usage Tips:[/bold yellow]\n"
        "• Use descriptive names for your proxy profiles\n"
        "• SOCKS5 proxies offer the best compatibility\n"
        "• Local mode is generally safer and more flexible\n"
        "• Always test your proxy connection before using\n"
        "• Use authentication when available for security\n\n"

        "[bold yellow]🛠️ Command Line Usage:[/bold yellow]\n"
        "[italic]Basic Commands:[/italic]\n"
        "• python main.py add <name> --type http --host <host> --port <port>\n"
        "• python main.py list\n"
        "• python main.py delete <name>\n"
        "• python main.py use <name> --mode local\n\n"

        "[italic]Examples:[/italic]\n"
        "• python main.py add work-proxy --type socks5 --host proxy.company.com --port 1080 --username myuser --password mypass\n"
        "• python main.py use work-proxy --mode local\n"
        "• python main.py list\n"
        "• python main.py delete old-proxy\n\n"

        "[bold yellow]🔒 Security Notes:[/bold yellow]\n"
        "• Credentials are stored securely in configuration files\n"
        "• Use strong passwords for proxy authentication\n"
        "• Be cautious with system-wide proxy settings\n"
        "• Verify proxy server trustworthiness before use\n\n"

        "[bold yellow]🆘 Getting Help:[/bold yellow]\n"
        "• Use option [5] in the interactive menu for this help\n"
        "• Check the README.md file for detailed documentation\n"
        "• Visit the project repository for updates and issues\n\n"

        "[bold green]✨ Happy Proxy Management![/bold green]",
        title="❓ Help & Usage Information",
        border_style="blue"
    ))

def show_interactive_menu():
    """Display an interactive menu for easy proxy management."""
    while True:
        console.clear()
        console.print(Panel(
            "[bold blue]Proxy Manager CLI[/bold blue]\n\n"
            "Manage HTTP/SOCKS proxies across Windows, macOS, and Linux\n\n"
            "[bold yellow]Select an option:[/bold yellow]",
            title="🚀 Welcome to Proxy Manager CLI",
            border_style="green"
        ))

        console.print("\n[bold cyan]Available Options:[/bold cyan]")
        console.print("[1] 📋 List all proxy profiles")
        console.print("[2] ➕ Add a new proxy profile")
        console.print("[3] 🗑️  Delete a proxy profile")
        console.print("[4] ▶️  Use/Activate a proxy profile")
        console.print("[5] ❓ Show help and usage information")
        console.print("[0] ❌ Exit")
        console.print()

        try:
            choice = console.input("[bold yellow]Enter your choice (0-5): [/bold yellow]").strip()

            if choice == "1":
                list_proxy_profiles()
            elif choice == "2":
                add_proxy_profile_interactive()
            elif choice == "3":
                delete_proxy_profile_interactive()
            elif choice == "4":
                use_proxy_profile_interactive()
            elif choice == "5":
                show_help_information()
            elif choice == "0":
                console.print(Panel(
                    "Thank you for using Proxy Manager CLI!\n\n"
                    "👋 Goodbye!",
                    title="Goodbye",
                    border_style="blue"
                ))
                break
            else:
                console.print(Panel(
                    f"❌ Invalid choice: '{choice}'\n\n"
                    "Please select a number between 0-5.",
                    title="Error",
                    border_style="red"
                ))

            if choice != "0":
                console.print("\n[bold cyan]Press Enter to continue...[/bold cyan]")
                console.input()

        except KeyboardInterrupt:
            console.print("\n\n[bold yellow]👋 Goodbye![/bold yellow]")
            break
        except EOFError:
            console.print("\n\n[bold yellow]👋 Goodbye![/bold yellow]")
            break

def list_proxy_profiles():
    """List all proxy profiles in a formatted table."""
    profiles = list_profiles()
    if profiles:
        console.print(Panel(
            f"📋 Proxy Profiles ({len(profiles)} total)",
            border_style="blue"
        ))

        table = Table(
            title=" ",
            show_header=True,
            header_style="bold yellow",
            row_styles=["none", "dim"]
        )
        table.add_column("Name", style="bold green", no_wrap=True)
        table.add_column("Type", style="cyan", no_wrap=True)
        table.add_column("Host", style="magenta")
        table.add_column("Port", style="blue", justify="center")
        table.add_column("Auth", style="red", justify="center")

        for p in profiles:
            profile_data = get_profile(p)
            has_auth = "✅ Yes" if profile_data.get('username') else "❌ No"
            profile_type = profile_data.get('type', 'N/A').upper()

            table.add_row(
                f"🔹 {p}",
                profile_type,
                profile_data.get('host', 'N/A'),
                str(profile_data.get('port', 'N/A')),
                has_auth
            )

        console.print(table)
    else:
        console.print(Panel(
            "📭 No proxy profiles found.\n\n"
            "💡 Tip: Use option [2] to create your first proxy profile",
            title="Empty",
            border_style="yellow"
        ))

def add_proxy_profile_interactive():
    """Interactively add a new proxy profile."""
    console.print(Panel(
        "➕ Add New Proxy Profile\n\n"
        "Please provide the following information:",
        title="Add Proxy Profile",
        border_style="green"
    ))

    name = console.input("\n[bold yellow]Profile Name: [/bold yellow]").strip()
    if not name:
        console.print(Panel("❌ Profile name cannot be empty!", title="Error", border_style="red"))
        return

    console.print("\n[bold cyan]Proxy Types:[/bold cyan]")
    console.print("• http   - HTTP Proxy")
    console.print("• socks4 - SOCKS4 Proxy")
    console.print("• socks5 - SOCKS5 Proxy")

    proxy_type = console.input("\n[bold yellow]Proxy Type (http/socks4/socks5): [/bold yellow]").strip().lower()
    if proxy_type not in ['http', 'socks4', 'socks5']:
        console.print(Panel("❌ Invalid proxy type! Please choose: http, socks4, or socks5", title="Error", border_style="red"))
        return

    host = console.input("[bold yellow]Proxy Host/IP: [/bold yellow]").strip()
    if not host:
        console.print(Panel("❌ Host cannot be empty!", title="Error", border_style="red"))
        return

    try:
        port = int(console.input("[bold yellow]Proxy Port: [/bold yellow]").strip())
        if port <= 0 or port > 65535:
            console.print(Panel("❌ Invalid port number! Must be between 1-65535", title="Error", border_style="red"))
            return
    except ValueError:
        console.print(Panel("❌ Port must be a number!", title="Error", border_style="red"))
        return

    username = console.input("[bold yellow]Username (optional): [/bold yellow]").strip()
    password = ""
    if username:
        password = console.input("[bold yellow]Password: [/bold yellow]").strip()

    try:
        add_profile(name, proxy_type, host, port, username if username else None, password if password else None)

        auth_status = "✅ With Authentication" if username else "❌ No Authentication"

        console.print(Panel(
            "🎉 Profile added successfully!\n\n"
            f"📝 Name: {name}\n"
            f"🔧 Type: {proxy_type.upper()}\n"
            f"🌐 Host: {host}\n"
            f"🔌 Port: {port}\n"
            f"🔐 Auth: {auth_status}",
            title="✅ Success",
            border_style="green"
        ))
    except Exception as e:
        console.print(Panel(
            f"❌ Failed to add profile: {str(e)}",
            title="Error",
            border_style="red"
        ))

def delete_proxy_profile_interactive():
    """Interactively delete a proxy profile."""
    profiles = list_profiles()
    if not profiles:
        console.print(Panel(
            "📭 No proxy profiles available to delete.\n\n"
            "💡 Use option [2] to add a proxy profile first.",
            title="No Profiles",
            border_style="yellow"
        ))
        return

    console.print(Panel("🗑️  Delete Proxy Profile", title="Delete Profile", border_style="red"))

    # Show available profiles
    console.print("\n[bold cyan]Available Profiles:[/bold cyan]")
    for i, profile in enumerate(profiles, 1):
        console.print(f"{i}. 🔹 {profile}")

    try:
        choice = console.input(f"\n[bold yellow]Enter profile name to delete: [/bold yellow]").strip()

        if not choice:
            console.print(Panel("❌ Profile name cannot be empty!", title="Error", border_style="red"))
            return

        profile = get_profile(choice)
        if not profile:
            console.print(Panel(f"❌ Profile '{choice}' not found!", title="Error", border_style="red"))
            return

        # Confirmation
        confirm = console.input(f"[bold red]Are you sure you want to delete '{choice}'? (yes/no): [/bold red]").strip().lower()
        if confirm in ['yes', 'y']:
            delete_profile(choice)
            console.print(Panel(
                f"🗑️  Profile '{choice}' deleted successfully!",
                title="✅ Deleted",
                border_style="green"
            ))
        else:
            console.print(Panel(
                "❌ Deletion cancelled.",
                title="Cancelled",
                border_style="yellow"
            ))
    except Exception as e:
        console.print(Panel(
            f"❌ Error deleting profile: {str(e)}",
            title="Error",
            border_style="red"
        ))

def use_proxy_profile_interactive():
    """Interactively use/activate a proxy profile."""
    profiles = list_profiles()
    if not profiles:
        console.print(Panel(
            "📭 No proxy profiles available to use.\n\n"
            "💡 Use option [2] to add a proxy profile first.",
            title="No Profiles",
            border_style="yellow"
        ))
        return

    console.print(Panel("▶️  Use/Activate Proxy Profile", title="Use Profile", border_style="blue"))

    # Show available profiles
    console.print("\n[bold cyan]Available Profiles:[/bold cyan]")
    for i, profile in enumerate(profiles, 1):
        profile_data = get_profile(profile)
        if profile_data:
            console.print(f"{i}. 🔹 {profile} ({profile_data.get('type', 'N/A').upper()}) - {profile_data.get('host', 'N/A')}:{profile_data.get('port', 'N/A')}")

    try:
        profile_name = console.input(f"\n[bold yellow]Enter profile name to use: [/bold yellow]").strip()

        if not profile_name:
            console.print(Panel("❌ Profile name cannot be empty!", title="Error", border_style="red"))
            return

        profile = get_profile(profile_name)
        if not profile:
            console.print(Panel(f"❌ Profile '{profile_name}' not found!", title="Error", border_style="red"))
            return

        console.print("\n[bold cyan]Activation Modes:[/bold cyan]")
        console.print("• local  - Start local proxy server (recommended)")
        console.print("• system - Set system-wide proxy (requires admin)")

        mode = console.input("[bold yellow]Activation mode (local/system) [default: local]: [/bold yellow]").strip().lower()
        if mode not in ['local', 'system']:
            mode = 'local'

        # Use the profile directly instead of restarting main
        if mode == 'system':
            try:
                set_system_proxy(profile['host'], profile['port'], profile.get('username'), profile.get('password'))
                console.print(Panel(
                    f"✅ System proxy set to {profile['host']}:{profile['port']}\n\n"
                    f"🌐 Protocol: {profile['type'].upper()}\n"
                    f"🔐 Authentication: {'✅ Yes' if profile.get('username') else '❌ No'}\n\n"
                    f"⚙️  Changes are now active on your system.",
                    title="✅ System Proxy Activated",
                    border_style="green"
                ))
            except Exception as e:
                console.print(Panel(
                    f"❌ Failed to set system proxy: {str(e)}\n\n"
                    f"💡 You may need administrator privileges to set system proxy.\n"
                    f"💡 Try running as administrator or use local mode instead.",
                    title="❌ Error",
                    border_style="red"
                ))
        else:
            console.print(Panel(
                f"🚀 Starting local proxy server...\n\n"
                f"📡 Upstream Proxy: {profile['host']}:{profile['port']} ({profile['type'].upper()})\n"
                f"🔌 Local Endpoint: localhost:8080\n"
                f"🔐 Auth Configured: {'✅ Yes' if profile.get('username') else '❌ No'}\n\n"
                f"💡 Press Ctrl+C to stop the proxy server",
                title="🔄 Local Proxy Server",
                border_style="blue"
            ))

            try:
                if profile['type'].startswith('socks'):
                    server = start_socks_proxy(8080, profile['host'], int(profile['port']), profile.get('username'), profile.get('password'))
                else:
                    server = start_http_proxy(8080, profile['host'], int(profile['port']))

                console.print(Panel(
                    f"✅ Local proxy is now running on localhost:8080\n\n"
                    f"🌍 Applications can now use this proxy to route traffic through {profile['host']}:{profile['port']}\n\n"
                    f"⚙️  Configure your applications to use HTTP proxy at localhost:8080",
                    title="✅ Active",
                    border_style="green"
                ))

                # Keep the proxy running until Ctrl+C
                import time
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                console.print(Panel(
                    "🛑 Shutting down proxy server...\n\n"
                    f"🧹 Cleaning up resources...\n"
                    f"🔌 Proxy server for '{profile_name}' has been stopped.",
                    title="🔌 Disconnected",
                    border_style="yellow"
                ))
                from proxy_server import stop_all_servers
                stop_all_servers()
                console.print("✅ Proxy servers stopped successfully.")
            except Exception as e:
                console.print(Panel(
                    f"❌ Failed to start local proxy: {str(e)}",
                    title="❌ Error",
                    border_style="red"
                ))

    except Exception as e:
        console.print(Panel(
            f"❌ Error using profile: {str(e)}",
            title="❌ Error",
            border_style="red"
        ))

def set_system_proxy(host, port, username=None, password=None):
    os_name = platform.system().lower()
    
    if os_name == 'windows':
        subprocess.run([
            'reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings',
            '/v', 'ProxyServer', '/t', 'REG_SZ', '/d', f'{host}:{port}', '/f'
        ], check=True)
        
    elif os_name == 'darwin':  # macOS
        cmd = ['networksetup', '-setwebproxy', 'Wi-Fi', host, str(port)]
        if username:
            cmd.extend(['-setwebproxyauthentication', 'Wi-Fi', username, password])
        subprocess.run(cmd, check=True)
        
    elif os_name == 'linux':
        subprocess.run(['gsettings', 'set', 'org.gnome.system.proxy.http', 'host', host], check=True)
        subprocess.run(['gsettings', 'set', 'org.gnome.system.proxy.http', 'port', str(port)], check=True)

def main():
    parser = argparse.ArgumentParser(description='Proxy Manager CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new proxy profile')
    add_parser.add_argument('name', type=str, help='Name for the proxy profile')
    add_parser.add_argument('--type', choices=['http', 'socks4', 'socks5'], required=True, help='Proxy type')
    add_parser.add_argument('--host', type=str, required=True, help='Proxy server host')
    add_parser.add_argument('--port', type=int, required=True, help='Proxy server port')
    add_parser.add_argument('--username', type=str, default=None, help='Authentication username (optional)')
    add_parser.add_argument('--password', type=str, default=None, help='Authentication password (optional)')

    subparsers.add_parser('list', help='List all proxy profiles')

    del_parser = subparsers.add_parser('delete', help='Delete a proxy profile')
    del_parser.add_argument('name', type=str, help='Name of the proxy profile to delete')

    use_parser = subparsers.add_parser('use', help='Activate a proxy profile')
    use_parser.add_argument('name', type=str, help='Name of the proxy profile to use')
    use_parser.add_argument('--mode', choices=['system', 'local'], default='local', help='Activation mode')

    args = parser.parse_args()
    init_config()

    if args.command == 'add':
        add_profile(args.name, args.type, args.host, args.port, args.username, args.password)
        
        auth_status = "With Auth" if args.username else "No Auth"
        
        console.print(Panel(
            f"Profile '{args.name}' added successfully!\n\n"
            f"Type: {args.type.upper()}\n"
            f"Host: {args.host}\n"
            f"Port: {args.port}\n"
            f"Auth: {auth_status}",
            title="New Proxy Profile",
            border_style="green"
        ))

    elif args.command == 'list':
        profiles = list_profiles()
        if profiles:
            console.print(Panel(
                f"Proxy Profiles ({len(profiles)} total)",
                border_style="blue"
            ))
            
            table = Table(
                title=" ",
                show_header=True, 
                header_style="bold yellow",
                row_styles=["none", "dim"]  # Alternate row styling
            )
            table.add_column("Name", style="bold green", no_wrap=True)
            table.add_column("Type", style="cyan", no_wrap=True)
            table.add_column("Host", style="magenta")
            table.add_column("Port", style="blue", justify="center")
            table.add_column("Auth", style="red", justify="center")
            
            for p in profiles:
                profile_data = get_profile(p)
                has_auth = "Yes" if profile_data.get('username') else "No"
                profile_type = profile_data.get('type', 'N/A').upper()
                
                table.add_row(
                    f"{p}",
                    profile_type,
                    profile_data.get('host', 'N/A'),
                    str(profile_data.get('port', 'N/A')),
                    has_auth
                )
            
            console.print(table)
        else:
            console.print(Panel(
                "No proxy profiles found.\n\n"
                "Tip: Use 'add' command to create your first proxy profile",
                title="Empty",
                border_style="yellow"
            ))

    elif args.command == 'delete':
        profile = get_profile(args.name)
        if profile:
            # For Windows batch files and non-interactive environments, delete without confirmation
            # For direct command line use, show confirmation if running interactively
            import sys, os
            try:
                # Check if we're in an interactive terminal
                is_interactive = os.isatty(0) and os.isatty(1)  # stdin and stdout are TTYs
                if is_interactive:
                    confirmation = Confirm.ask(f"Are you sure you want to delete the profile '{args.name}'?")
                    if confirmation:
                        delete_profile(args.name)
                        console.print(Panel(
                            f"Profile '{args.name}' deleted successfully!\n\n"
                            f"The proxy profile has been permanently removed.",
                            title="Profile Deleted",
                            border_style="green"
                        ))
                    else:
                        console.print(Panel(
                            f"Deletion cancelled.\n\n"
                            f"Your proxy profile remains intact.",
                            title="Cancelled",
                            border_style="yellow"
                        ))
                else:
                    # Non-interactive mode - delete without confirmation
                    delete_profile(args.name)
                    console.print(Panel(
                        f"Profile '{args.name}' deleted successfully!",
                        title="Profile Deleted",
                        border_style="green"
                    ))
            except:
                # If there are any issues with detection, just delete without confirmation
                delete_profile(args.name)
                console.print(Panel(
                    f"Profile '{args.name}' deleted successfully!",
                    title="Profile Deleted",
                    border_style="green"
                ))
        else:
            console.print(Panel(
                f"Profile '{args.name}' not found!\n\n"
                f"Please check the profile name and try again.",
                title="Error",
                border_style="red"
            ))
            sys.exit(1)

    elif args.command == 'use':
        profile = get_profile(args.name)
        if not profile:
            console.print(Panel(
                f"Profile '{args.name}' not found!\n\n"
                f"Please check the profile name and try again.",
                title="Error",
                border_style="red"
            ))
            sys.exit(1)

        if args.mode == 'system':
            try:
                set_system_proxy(profile['host'], profile['port'], profile.get('username'), profile.get('password'))
                console.print(Panel(
                    f"System proxy set to {profile['host']}:{profile['port']}\n\n"
                    f"Protocol: {profile['type'].upper()}\n"
                    f"Authentication: {'Yes' if profile.get('username') else 'No'}\n\n"
                    f"Changes are now active on your system.",
                    title="System Proxy Activated",
                    border_style="green"
                ))
            except Exception as e:
                console.print(Panel(
                    f"Failed to set system proxy: {str(e)}\n\n"
                    f"You may need administrator privileges to set system proxy.\n"
                    f"Try running as administrator or use local mode instead.",
                    title="Error",
                    border_style="red"
                ))
        else:
            console.print(Panel(
                f"Starting local proxy server...\n\n"
                f"Upstream Proxy: {profile['host']}:{profile['port']} ({profile['type'].upper()})\n"
                f"Local Endpoint: localhost:8080\n"
                f"Auth Configured: {'Yes' if profile.get('username') else 'No'}\n\n"
                f"Press Ctrl+C to stop the proxy server",
                title="Local Proxy Server",
                border_style="blue"
            ))
            
            try:
                if profile['type'].startswith('socks'):
                    server = start_socks_proxy(8080, profile['host'], int(profile['port']), profile.get('username'), profile.get('password'))
                else:
                    server = start_http_proxy(8080, profile['host'], int(profile['port']))
                
                console.print(Panel(
                    f"Local proxy is now running on localhost:8080\n\n"
                    f"Applications can now use this proxy to route traffic through {profile['host']}:{profile['port']}\n\n"
                    f"Configure your applications to use HTTP proxy at localhost:8080",
                    title="Active",
                    border_style="green"
                ))
                
                # Keep the main thread alive to keep the proxy running
                import time
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                console.print(Panel(
                    "Shutting down proxy server...\n\n"
                    f"Cleaning up resources...\n"
                    f"Proxy server for '{args.name}' has been stopped.",
                    title="Disconnected",
                    border_style="yellow"
                ))
                from proxy_server import stop_all_servers
                stop_all_servers()
                console.print("Proxy servers stopped successfully.")
                sys.exit(0)
    
    # If no command was provided, show interactive menu
    elif not args.command:
        show_interactive_menu()

if __name__ == '__main__':
    main()
