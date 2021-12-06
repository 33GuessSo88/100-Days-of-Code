print('''
        .-"""-.       ||::::::==========
       /=      \      ||::::::==========
      |- /~~~\  |     ||::::::==========
      |=( '.' ) |     ||================
      \__\_=_/__/     ||================
       {_______}      ||================
     /` *       `'--._||
    /= .     [] .     { >
   /  /|ooo     |`'--'||
  (   )\_______/      ||
   \``\/       \      ||
    `-| ==    \_|     ||
      /         |     ||
     |=   >\  __/     ||
     \   \ |- --|     ||
      \ __| \___/     ||
      _{__} _{__}     ||
     (    )(    )     ||
 ^^~  `"""  `"""  ~^^^~^^~~~^^^~^^^~^^^~^^~^
''')

print("Welcome to the Space Game, designed by BIG DIESEL")

first = input("You are on the moon, do you leave your habitat or wait for your partner? (leave or wait)").lower()
if first == "leave":
    print("You died")
else:
    print("your partner arrives, you are ready to go outside now")

    second = input("do you go left or right? " ).lower()

    if second == "right":
        print("you are dead")
    else:
        print("you are the best astronaught ever")

