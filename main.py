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
                console.print("\n" + Panel(
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
    
    # If no command was provided, show help
    elif not args.command:
        console.print(Panel(
            f"Proxy Manager CLI\n\n"
            f"Manage HTTP/SOCKS proxies across Windows, macOS, and Linux\n\n"
            f"Commands:\n"
            f"  add    : Add a new proxy profile\n"
            f"  list   : List all proxy profiles\n"
            f"  delete : Delete a proxy profile\n"
            f"  use    : Activate a proxy profile\n\n"
            f"Usage: python main.py [command] [options]",
            title="Welcome to Proxy Manager CLI", 
            border_style="green"
        ))
        parser.print_help()

if __name__ == '__main__':
    main()