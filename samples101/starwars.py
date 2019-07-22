from pyfiglet import Figlet

def starwars(text):
    custom_fig = Figlet(font='starwars')
    return(custom_fig.renderText(text))
