import os
import collections
import click
from eve.config import TIDY_ROOT
import pyttsx3


def female_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    engine.setProperty("volume", 1)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()


@click.command()
@click.option("-v", "--verbose", type=bool, help="Vebose Logging", default=False)
@click.option("-p", "--path", type=str, help="Directory to tidy", default=TIDY_ROOT)
def cli(verbose, path):
    """- Organizes your Downloads Folder"""
    root_dir = path or os.path.join(os.path.expanduser("~"), "Downloads")

    file_mappings = collections.defaultdict()

    for filename in os.listdir(root_dir):
        file_type = filename.split(".")[-1]
        file_mappings.setdefault(file_type, []).append(filename)

    click.echo("File Mappings created...")
    female_speak("File Mappings created...")

    for folder_name, folder_items in file_mappings.items():
        folder_path = os.path.join(root_dir, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        if verbose:
            click.echo(
                f"Tidying {len(folder_items)} files in: {root_dir} ".center(100, "=")
            )
        for folder_item in folder_items:
            source = os.path.join(root_dir, folder_item)
            destination = os.path.join(folder_path, folder_item)
            try:
                click.echo(f"Moving {source} to {destination}... ")
                os.rename(source, destination)
            except PermissionError:
                pass
    click.echo("Tidying Downloads...")
    female_speak("Tidying Downloads...")
    click.echo("~~~~~~~~~~~~~~~~~~~~~~~~")
    click.echo("Downloads Tidied.")
    female_speak("Downloads Tidied.")
