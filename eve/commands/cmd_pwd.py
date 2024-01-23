import click
import os
import json
from pprint import pprint


@click.group()
def cli():
    """- Password Manager"""

@cli.command()
@click.argument("masterpassword", type=str, required=True)
def show(masterpassword):
    '''- Show Passwords'''
    if masterpassword == os.environ.get('MASTER PASSWORD'):
        with open('D:/Varun/PROGRAMMING/Eve-CLI-Tool/eve/passwords.json', 'r') as passwds:
            raw_data = passwds.read()

        data = json.loads(raw_data)
        click.echo(f"These are your passwords...\n")
        for username in data.keys():
            click.echo(f"\t {username} : {data[username]} ")


@cli.command()
@click.argument("username", type=str, required=True)
@click.argument("password", type=str, required=True)
def add(username, password):
    '''- Add Password'''
    with open('D:/Varun/PROGRAMMING/Eve-CLI-Tool/eve/passwords.json', 'r') as passwds:
        raw_data = passwds.read()

    data = json.loads(raw_data)
    if username in data.keys():
        click.echo(f"key '{username}' already exists.")

    else:
        data[username] = password
        with open('D:/Varun/PROGRAMMING/Eve-CLI-Tool/eve/passwords.json', 'w') as passwds:
            json.dump(data, passwds, indent=4)


@cli.command()
@click.argument("username", type=str, required=True)
def remove(username):
    '''- Delete Password'''
    with open('D:/Varun/PROGRAMMING/Eve-CLI-Tool/eve/passwords.json', 'r') as passwds:
        raw_data = passwds.read()

    data = json.loads(raw_data)
    if username in data.keys():
        click.echo(f"'{username} : {data.pop(username)}' has been deleted.")
        with open('D:/Varun/PROGRAMMING/Eve-CLI-Tool/eve/passwords.json', 'w') as passwds:
            json.dump(data, passwds, indent=4)
    else:
        click.echo(f"key '{username}' does not exist.")
