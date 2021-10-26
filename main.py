import func as f


#המשתמש מכניס את שמו
#המשתמש השני מכניס את שמו
#לאחר הפונקציה פונה אל המשתמש בשמו מתחיל המשחק 
#משתמש בוחר האם ברצונו להשתמש באיקס או עיגול
#משתמש בוחר מספר בלוח ובו מכניס את הבחירה שלו
#לאחר מכן המשתמש השני בוחר מספר בלוח ובחור באיקס או עיגול בהינתן במה שהמשתמש הראשון בחר 
#לאחר מכן הפונקציה בודקת האם המשתמש סיים את התוכנית 
#לאחר מכן הפונקציה בודקת אם יש 3 סימונים דומים באלחסון או ישר 
#במידה ויש הפונקציה מעלה נקודה למנצח ורושמת את הניקוד 

white = "\033[0;37m"
blue = "\033[1;34m"
orange = "\033[1;33m"

print (blue + "The names of the developers - 'Omer Shlomo' and 'Alon Shaul'\n" + white)

print (orange + "Welcome to the game 'Tic - Tac - Toe':\n" + white)

playername1=f.player1()
print("")
playername2=f.player2()

f.games(playername1,playername2)