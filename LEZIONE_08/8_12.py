

def panino(*args):
    print(f"Il tuo panino è formato da: {', '.join(args)}") 
    print()

panino('Insalata', 'Hamburger', 'Pomodoro', 'Bacon')
panino('Insalata', 'Hamburger')
panino('Hamburger', 'Pomodoro', 'Bacon')
