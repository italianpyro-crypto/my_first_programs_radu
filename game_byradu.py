while True:
    print("you and ur friend are in a dark room. You have a box of matches")
    scene = input("what do you do?>>")
    if scene == "light up a match":
        print("the room has been lightend, you see a hole")
        scene2 = input("what do you do?>>")
        if scene2 == "go through the hole":
                print("you go through the hole, but your friend cant. He gives you a piece of paper")
                scene3 = input("what do you do?>>")
                if scene3 == "ignore the paper and go through":
                    print("you go through, but u abandon ur friend. You go and discover a ship at the end of the tunel. Yay! you win")
                elif scene3 == "read the paper":
                    print("you read the paper: 'please dont leave me..'") 
                    scene4 = input("what do you do?>>")
                    if scene4 == "go through":
                        print("you go through, but u abandon ur friend. You go and discover a ship at the end of the tunel. Yay! you win")
                    elif scene4 == "stay with ur friend":
                        print("you stay with him, and you dont leave him. He says: 'thank you for staying with me..' you win!!")

                elif scene3 == "take your friend with you":
                    print("you take your friend with you, but he has his leg broken. you cant take him with you")
                    scene5 = input("what do you do?>>")
                    if scene5 == "leave him":
                        print("you leave him, and you go through the hole. You discover a ship at the end of the tunel. Yay! you win")
                    elif scene5 == "stay with him":
                        print("you stay with him, and you dont leave him. He says: 'thank you for staying with me..' you win!!")
        elif scene2 == "stay with your friend":
             print("you both lay down. he gives you a peace of paper.")
             scene6 = input("what do you do?>>")
             if scene6 == "read the paper":
                print("you read the paper: 'please dont leave me..'")
                scene7 = input("what do you do?>>")
                if scene7 == "go through":
                    print("you go through, but u abandon ur friend. You go and discover a ship at the end of the tunel. Yay! you win")
                elif scene7 == "stay with ur friend":
                    print("you stay with him, and you dont leave him. He says: 'thank you for staying with me..' you win!!")
            
    
        
