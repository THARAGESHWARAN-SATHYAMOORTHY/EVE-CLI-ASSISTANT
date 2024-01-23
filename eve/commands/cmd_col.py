import click
import tkinter
from tkinter import colorchooser


@click.command()
@click.option("-cf", "--colorformat", default=None)
def cli(colorformat):
    '''- Pick a color in HEX or RGB format'''
    color_picked = colorchooser.askcolor()
    if colorformat == None:
        click.echo(f"You have selected:\n\tHEX COLOR CODE : {color_picked[1]}\n\tRGB COLOR CODE : {color_picked[0]}")
    elif colorformat == "hex":
        click.echo(f"\n\tHEX COLOR CODE : {color_picked[1]}\n\t")
    elif colorformat == "rgb":
        click.echo(f"\n\tRGB COLOR CODE : {color_picked[0]}\n\t")
