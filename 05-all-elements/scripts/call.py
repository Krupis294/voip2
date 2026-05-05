import click
import requests

NGINX_IP = "u54.srv.liptel"
NGINX_PORT = 443

@click.command()
@click.option(
    "-f",
    "--from_ext",
    default="10",
    help="Extension that originates a call (can only be internal)",
)
@click.option(
    "-t",
    "--to_ext",
    default="11",
    help="Extension that receives the call (can be internal or external)",
)
def make_call(from_ext, to_ext):
    response = requests.post(
        f"https://{NGINX_IP}:{NGINX_PORT}/api/v1/call",
        headers={"Content-Type": "application/json"},
        json={
            "from_ext": from_ext,
            "to_ext": to_ext,
        },
        verify=False
    )
    print(response.text)


def main():
    make_call()


if __name__ == "__main__":
    main()
