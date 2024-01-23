import click


@click.command()
@click.argument("expression", type=str)
def cli(expression):
    '''- Evaluate an expression'''
    exp = True
    for i in expression:
        if i.isalpha():
            exp = False
            click.echo(f"Error : Cannot calculate this expression.\nEnter valid data type")
            break
        
    if exp:
        expression.replace("x", "*")
        expression.replace("^", "**")
        click.echo(f" {expression} = {eval(expression)} ")