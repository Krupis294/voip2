import click
import sys
from asterisk.ami import AMIClient, SimpleAction

ASTERISK_IP = "localhost"
ASTERISK_PORT = 5038
AMI_USERNAME = "amiuser"
AMI_PASSWORD = "amipass"


@click.command()
@click.option(
    "-f",
    "--from_ext",
    default="10",
    show_default=True,
    help="Extension that originates a call",
)
@click.option(
    "-t",
    "--to_ext",
    default="11",
    show_default=True,
    help="Extension that receives the call",
)
@click.option(
    "--host",
    default=ASTERISK_IP,
    show_default=True,
    help="Asterisk AMI host",
)
@click.option(
    "--port",
    default=ASTERISK_PORT,
    show_default=True,
    help="Asterisk AMI port",
)
@click.option(
    "--timeout",
    default=30,
    show_default=True,
    help="Call timeout in seconds",
)
def make_call(from_ext, to_ext, host, port, timeout):
    """Originate a call between two extensions via Asterisk AMI."""

    click.echo(f"Connecting to AMI at {host}:{port}...")

    try:
        client = AMIClient(address=host, port=port)

        # LOGIN
        future = client.login(username=AMI_USERNAME, secret=AMI_PASSWORD)
        response = future.response

        if not response or response.status == "Error":
            click.echo(f"[ERROR] Login failed: {getattr(response, 'keys', {})}", err=True)
            sys.exit(1)

        click.echo("[OK] Connected to AMI")

        # ORIGINATE
        click.echo(f"Originating call: {from_ext} -> {to_ext}")
        action = SimpleAction(
            "Originate",
            Channel=f"Local/{to_ext}@from-ami",
            Context="from-ami",
            Exten=str(to_ext),
            Priority=1,
            CallerID=str(from_ext),
            Timeout=timeout * 1000,
            Async="true",
    	)
        future = client.send_action(action)
        response = future.response

        if not response or response.status == "Error":
            click.echo(f"[ERROR] Originate failed: {getattr(response, 'keys', {})}", err=True)
            client.logoff()
            sys.exit(1)

        click.echo("[OK] Call initiated successfully")

        client.logoff()

    except ConnectionRefusedError:
        click.echo(f"[ERROR] Cannot connect to AMI at {host}:{port}. Is Asterisk running?", err=True)
        sys.exit(1)

    except Exception as e:
        click.echo(f"[ERROR] Unexpected error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    make_call()
