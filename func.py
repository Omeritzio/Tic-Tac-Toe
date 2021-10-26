green = "\033[0;32m"
red = "\033[0;31m"
white = "\033[0;37m"
yellow = "\033[0;93m"
blue = "\033[1;34m"

#פונקצית משתמש ראשון
def player1():
  try: 
    with open ("champions.txt", "r") as f:
      file = f.read()
      print ("List Players:\n")
      for i in file:
        print(i, end = "")
      file = file.replace("\n" ," ")
      file_list = file.split(" ")
      print("\n")
      player_name1 = input("Choose one name from above: \n").capitalize()
      while player_name1 not in file_list:
        print ("We dont know this name, lets start again.\n")
        player_name1 = input("Choose one of our name from above: \n").capitalize()
      else:
        return player_name1
  except FileNotFoundError:
    print ("There is no file\n")
  except Exception as e:
    print (f"There is an error {e}\n")

#פונקצית משתמש שני
def player2():
  try: 
    with open ("champions.txt", "r") as f:
      file = f.read()
      print ("List Players:\n")
      for i in file:
        print(i, end = "")
      file = file.replace("\n" ," ")
      file_list = file.split(" ")
      print("\n")

      player_name2 = input("Choose one name from above: \n").capitalize()

      while player_name2 not in file_list:
        print ("We dont know this name, lets start again. \n")
        player_name2 = input("Choose one of our name from above: \n").capitalize()
      else:
        return player_name2
  except FileNotFoundError:
    print ("There is no file\n")
  except Exception as e:
    print (f"There is an error {e}\n")


#פונקצית להראות את לוח המשחק
def display_board(board):
  print(white + '   |   |')
  print(blue + ' ' + board[1] + white + ' | ' + blue + board[2] + white + ' | ' + blue + board[3])
  print(white + '   |   |')
  print(white + '-----------')
  print(white + '   |   |')
  print(blue + ' ' + board[4] + white + ' | ' + blue + board[5] + white + ' | ' + blue + board[6])
  print(white + '   |   |')
  print(white + '-----------')
  print(white + '   |   |')
  print(blue + ' ' + board[7] + white + ' | ' + blue + board[8] + white + ' | ' + blue + board[9])
  print(white + '   |   |' + white)


#בדיקת המספר בלוח במידה והמספר לא מופיע בלוח יש שגיאה 
def players_turn (player:str,symbol:str,board:list):
  number_selection = input(f"{player} which number on our board you wanna place your {symbol} ? \n")
  while number_selection not in board or number_selection == "0":
      print ("This number not in our board try another number \n")
      number_selection = input(f"{player} which number on our board you wanna place your {symbol}? \n")
  else:
        board[int(number_selection)] = symbol
  return board



#הפונקציה שואלת אם ברצונו של כל אחד מהמשתימשים לשחק רק במידה ושניהם מסכים המשחק מתחיל
def again (player1,player2,playerscore1,playerscore2):
    playagain = input(f"{player1} to play again click 'y' for ending click 'n': \n")

    while playagain != "y" and playagain != "n":
        print ("I believe you miss-click your answer, lets try again! :) \n")
        playagain = input("To play again click 'y' for ending click 'n': \n")
  
    if playagain == "y":
      playagain = input(f"{player2} to play again click 'y' for ending click 'n': \n")

      while playagain != "y" and playagain != "n":
        print("I believe you miss - Click your answer, lets try again! :) \n")
        playagain = input("To play again click 'y' for ending click 'n': \n")

      if playagain == "y":
        games(player1,player2)

      elif playagain == "n":
        scoreprinting1 = playerscore1.count(1)
        scoreprinting2 = playerscore2.count(1)
        print ("\n")
        print (yellow + "*** Total Score ***")
        print (white + f"|{player1} : {scoreprinting1}| VS |{player2} : {scoreprinting2}|")
      

    elif playagain == "n":
        scoreprinting1 = playerscore1.count(1)
        scoreprinting2 = playerscore2.count(1)
        print ("\n")
        print (yellow + "*** Total Score ***")
        print (white + f"|{player1} : {scoreprinting1}| VS |{player2} : {scoreprinting2}|")

#ניצחונות של משתמש אחד ומשתמש שני בתוך שני רשימות
player1score=[]
player2score=[] 

def games(player1,player2):
  try:
    board = []
    player2Symbol = ""
    turn = 1

    for i in range(0,10):
      board.append(str(i))
    Ending = ""
    print ("")
    print (yellow + "Let's start the game:  \n" + white)
    print (f"*** {player1} VS {player2} ***\n")
    print (f"{player1} let's choose which symbol you prefer: \n")
      #משתמש בוחר האם ברצונו להשתמש באיקס או עיגול
    player1Symbol = input("Choose " + red + "X" + white + " or " + green + "O" + white + " : \n").upper()
      #במידה ובחר סימן אשר לא מוכר למערכת המערכת תשלח שגיאה ותבקשב לבחור שוב
    while player1Symbol != "X" and player1Symbol != "O":
      print ("We dont know this symbol let's try again \n")
      player1Symbol = input("Choose " + red + "X" + white + " or " + green + "O" + white + " : \n").upper()
    else:  
      if player1Symbol == "X":
          player2Symbol = green + "O" + white
          player1Symbol = red + "X" + white
      elif player1Symbol == "O":
        player2Symbol = red + "X" + white
        player1Symbol = green + "O" + white
      print ("__________________________\n")
      display_board(board)
      print ("__________________________\n")

      #הפונקציה בודקת האם הסתיים המשחק במידה ולא ממשיכה עד תור 9
    while Ending != "finish" :
     
      #המשתמש הראשון מכניס את בחירתו
      while turn % 2 == 1:
         board = players_turn (player1,player1Symbol,board)
         print ("__________________________\n")
         display_board(board)
         print ("__________________________\n")
         turn += 1
         

      # כל אפשרויות הניצחון עבור המשתמש הראשון
      first_row = board[1:4].count(player1Symbol) 
      third_row = (board[7],board[8],board[9]).count(player1Symbol)
      sec_row = (board[4],board[5],board[6]).count(player1Symbol)
      first_colmun = (board[1],board[4],board[7]).count(player1Symbol)
      second_colmun = (board[2],board[5],board[8]).count(player1Symbol)
      third_colmun = (board[3],board[6],board[9]).count(player1Symbol)
      slash = (board[1],board[5],board[9]).count(player1Symbol)
      back_slash = (board[3],board[5],board[7]).count(player1Symbol)
   
      if first_row == 3 or sec_row == 3 or third_row == 3 or first_colmun == 3  or second_colmun == 3 or third_colmun == 3 or slash==3 or back_slash==3:
        Ending = "finish"
        player1score.append(1)
        player1score.append(1)
        player1score.append(1)

          
        print(f"{player1} you are the winner !!!\n")
      else:
        while turn % 2 == 0:
            board = players_turn(player2,player2Symbol,board)
            print ("__________________________\n")
            display_board(board)
            print ("__________________________\n")
            turn += 1
            
            #אפשרויות  ניצחון עבור המשתמש השני
            first_row2 = board[1:4].count(player2Symbol) 
            third_row2 = (board[7],board[8],board[9]).count(player2Symbol)
            sec_row2 = (board[4],board[5],board[6]).count(player2Symbol)
            first_colmun2 = (board[1],board[4],board[7]).count(player2Symbol)
            second_colmun2 = (board[2],board[5],board[8]).count(player2Symbol)
            third_colmun2 = (board[3],board[6],board[9]).count(player2Symbol)
            slash2 = (board[1],board[5],board[9]).count(player2Symbol)
            back_slash2 = (board[3],board[5],board[7]).count(player2Symbol)

            #במידה והמשתמש השני ניצח
            if first_row2 == 3 or sec_row2 == 3 or third_row2 == 3 or first_colmun2 == 3  or second_colmun2 == 3 or third_colmun2 == 3 or slash2 == 3 or back_slash2 == 3:
              print(f"{player2} you are the winner !!!\n")
              Ending = "finish"
              player2score.append(1)
              player2score.append(1)
              player2score.append(1)

      #בדיקה לגבי התור ה9 
      if turn == 9 :
         board = players_turn(player1,player1Symbol,board)
         print ("__________________________\n")
         display_board(board)
         print ("__________________________\n")
         first_row = board[1:4].count(player1Symbol) 
         third_row = (board[7],board[8],board[9]).count(player1Symbol)
         sec_row = (board[4],board[5],board[6]).count(player1Symbol)
         first_colmun = (board[1],board[4],board[7]).count(player1Symbol)
         second_colmun = (board[2],board[5],board[8]).count(player1Symbol)
         third_colmun = (board[3],board[6],board[9]).count(player1Symbol)
         slash = (board[1],board[5],board[9]).count(player1Symbol)
         back_slash = (board[3],board[5],board[7]).count(player1Symbol)
    
         if first_row == 3 or sec_row == 3 or third_row == 3 or first_colmun == 3  or second_colmun == 3 or third_colmun == 3 or slash == 3 or back_slash == 3:
          Ending = "finish"
          print(f"{player1} you are the winner !!!\n")
          player1score.append(1)
          player1score.append(1)
          player1score.append(1)

         else:
          print("It's a draw \n")
          player2score.append(1)
          player1score.append(1) 
          Ending = "finish" 
        
    else:
      print("The game is over \n")
      print("Would you like to play again? \n")
      again(player1,player2,player1score,player2score)
  except Exception as e:
    print(f"There is an Error {e}  \n")