"""
  Vous etes contre un bot, vous avez chacun 50PV au depart, vous attackez tour par tour

  L'attack du bot fait entre 5 et 20 dégats

  Votre attack fait entre 5 et 10 dégats

  Vous avez un avantage que le bot n'a pas ; vous pouvez boire des potions

    Vous avez 3 Potions,
    Chaque potion vous rajoute entre 15 et 50PV
 
 
  PS: quand vous utiliser une potion, vous sautez votre prochain tour,
  autremment dit :
      vous buvez une potion --- le bot vous attack
      vous sauter votre tour --- le bot vous attack

"""


from random import randint

player_pv = 50
bot_pv = 50

#le choix du joueur
attack_popo = ["1", "2"]

#le nombre de potion dispo
player_popo = 3


while player_pv != 0 or bot_pv != 0 :
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    #check si le choix est valide
    if choix in attack_popo:
        choix = int(choix)
    else:
        continue


    if choix == 1:
        #le joueur attack
        player_dommages = randint(5, 10)
        #le bot perd des PV
        bot_pv -= player_dommages
        print(f"⚔ Vous avez infligé {player_dommages} points de dégats à l'ennemi 🪓")
        if bot_pv <= 0:
            print("Vous avez gagné, GG !")
            break

        #le bot attck
        bot_dommages = randint(5, 20)
        #le joueur perd des pv
        player_pv -= bot_dommages
        print(f"⚔ L'ennemie vous a infligé {bot_dommages} points de dégats 🪓")

        #check les pv du joueur
        if player_pv <= 0:
            print("Dommage, vous avez perdu ")
            break

        #resultat
        print(f"Il vous reste {player_pv} pv.")
        print(f"Il reste {bot_pv} pv à l'ennemi.")


    elif choix == 2 :
        #popo
        if player_popo > 0:
            #le joueur utilise une potion
            player_popo -= 1
            player_rec = randint(15, 40)
            #le joueur recupere des PV
            player_pv += player_rec
            print(f"🍙 Vous avez récupérez {player_rec} pv ❤  ({player_popo} 🍡  restantes)")

            #le bot attack
            bot_dommages = randint(5, 20)
            player_pv -= bot_dommages
            print(f"⚔ L'ennemie vous a infligé {bot_dommages} points de dégats 🪓")

            #check les PV du joueur
            if player_pv <= 0:
                print("Dommage, vous avez perdu ")
                break

            #resultat
            print(f"Il vous reste {player_pv} pv.")
            print(f"Il reste {bot_pv} pv à l'ennemi.")

        #le joueur n'a plus de potion, il ne peut donc pas recup
        else:
            print("vous n'avez plus de potion")
            print("-"*50)
            continue
    print("-"*50)


    #le deuxiéme tour
    if choix == 1:
        continue

    elif choix == 2:
        #le joueur pass son tour
        print("Vous passez votre tour ...")

        #le bot attack
        bot_dommages = randint(5, 20)
        player_pv -= bot_dommages
        print(f"⚔ L'ennemie vous a infligé {bot_dommages} points de dégats 🪓")
        if player_pv <= 0:
            print("Dommage, vous avez perdu ")
            break

        #resultat
        print(f"Il vous reste {player_pv} pv.")
        print(f"Il reste {bot_pv} pv à l'ennemi.")
    print("-"*50)

print("Fin du jeu, à bientôt !")
