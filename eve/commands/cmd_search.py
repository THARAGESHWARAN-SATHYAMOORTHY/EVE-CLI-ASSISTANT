import click
import webbrowser
from eve.config import google_url, wiki_url, youtube_url
import pyttsx3


def female_speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',200)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


class Context:
    def __init__(self, topic):
        self.topic = str(topic)

@click.group()
@click.option("-t", "--topic", type=str, help="Topic you want to search for", default=google_url)
@click.pass_context
def cli(ctx, topic):
    '''- Search For Something'''
    ctx.obj = Context(topic)


@cli.command()
@click.pass_context
def google(ctx):
    '''- Search in google'''
    topic_list = str(ctx.obj.topic).split()
    url = google_url
    for i in range(0, len(topic_list)):
        if i == len(topic_list) - 1:
            url += topic_list[i]
        else:
            url += topic_list[i] + "+"
    click.echo(f"Opening {str(ctx.obj.topic)} in google...")
    female_speak(f"Opening {str(ctx.obj.topic)} in google...")
    webbrowser.open(url)


@cli.command()
@click.pass_context
def wiki(ctx):
    '''- Search in wikipedia'''
    topic_list = str(ctx.obj.topic).split()
    url = wiki_url
    for i in range(0, len(topic_list)):
        if i == len(topic_list) - 1:
            url += topic_list[i]
        else:
            url += topic_list[i] + "_"
    click.echo(f"Opening {str(ctx.obj.topic)} in wikipedia...")
    female_speak(f"Opening {str(ctx.obj.topic)} in wikipedia...")
    webbrowser.open(url)


@cli.command()
@click.pass_context
def yt(ctx):
    '''- Search in youtube'''
    topic_list = str(ctx.obj.topic).split()
    url = youtube_url
    for i in range(0, len(topic_list)):
        if i == len(topic_list) - 1:
            url += topic_list[i]
        else:
            url += topic_list[i] + "+"
    click.echo(f"Opening {str(ctx.obj.topic)} in youtube...")
    female_speak(f"Opening {str(ctx.obj.topic)} in youtube...")
    webbrowser.open(url)