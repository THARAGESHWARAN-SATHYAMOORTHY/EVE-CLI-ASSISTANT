import click
from eve.service import svc_weather
import time
import pyttsx3


def female_speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',200)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def convert_epoch_to(epoch, fmt):
    return time.strftime(fmt, time.localtime(epoch))

def is_around_midday(epoch):
    return 11 <= int(convert_epoch_to(epoch, '%H')) <= 13


class Context:
    def __init__(self, location):
        self.location = location
        self.weather = svc_weather.Weather()


@click.group()
@click.option("-l", "--location", type=str, help="Weather at this location")
@click.pass_context
def cli(ctx, location):
    '''- Weather info'''
    ctx.obj = Context(location)

@cli.command()
@click.pass_context
def current(ctx):
    """Current weather info"""
    result = ctx.obj.weather.current(location=ctx.obj.location)
    click.echo(f" {result['location']} - {result['status'].upper()} ".center(45, "="))
    female_speak(f" Bringning to you the current weather in {result['location']}...")
    female_speak(f"The weather is {result['status'].upper()} ")
    click.echo(f"\U0001F525 Temp: {result['temp']} - {result['min']}/{result['max']} (min/max) ")
    female_speak(f" The temperature is {int(result['temp'])} degrees celsius")
    female_speak(f"The minimum temperature is {int(result['min'])} degrees celsius and the maximum temperature is {int(result['max'])} degrees celsius")
    click.echo(f"\U0001F32A Wind: {round(result['wind'], 1)}")
    female_speak(f" Wind speeds are at {round(result['wind'], 1)} miles per hour")
    click.echo(f"\U0001F4A7 Rain: {result['rain']}")
    if result['rain'] == {}:
        pass
    else:
        female_speak(f" Rainfall status is {result['rain']}")
    click.echo(
        f"\U0001F315 Sunrise: {time.strftime('%H:%m %p', time.localtime(result['sun_rise']))} \n"
        f"\U0001F311 Sun set: {time.strftime('%H:%m %p', time.localtime(result['sun_set']))} "
    )


@cli.command()
@click.pass_context
def forecast(ctx):
    """Weather forecast for the week"""

    def formatter(data):
        if isinstance(data, float):
            data = round(data, 2)
        return str(data).center(14)

    to_display = [wx for wx in ctx.obj.weather.forecast(location=ctx.obj.location) if is_around_midday(wx['time'])]
    click.echo(f" {to_display[0]['location']} ".center(int(14*5.5), "="))
    female_speak(f" Bringin weather forecast in {to_display[0]['location']} ")
    click.echo("\U0001F4C5 Date:" + "".join([formatter(convert_epoch_to(wx['time'], "%a %d %b")) for wx in to_display]))
    click.echo("\U0001F525 Temp:" + "".join([formatter(wx['temp']) for wx in to_display]))
    click.echo("\U0001F32A Rain:" + "".join([formatter(wx['wind']) for wx in to_display]))
    click.echo("\U0001F4A7 Wind:" + "".join([formatter(wx['rain']) for wx in to_display]))
    
    # female_speak("Date:" + "".join([formatter(convert_epoch_to(wx['time'], "%a %d %b")) for wx in to_display]))
    # female_speak("Temp:" + "".join([formatter(wx['temp']) for wx in to_display]))
    # female_speak("Rain:" + "".join([formatter(wx['wind']) for wx in to_display]))
    # female_speak("Wind:" + "".join([formatter(wx['rain']) for wx in to_display]))
