import googlesearch as gs
import sqlite3
conn = sqlite3.connect('chatbot.db')
c = conn.cursor()

def getresponse(query):
    getdata="""SELECT * FROM chatdata"""
    c.execute(getdata)
    data=c.fetchall()
    for i in data:
        if query in (i[0].lower()):
            print("joker> "+str(i[1]))
            return False
    return True

def saveresponse(query):
    print("joker> Please give your custom response")
    response=input("user> ")
    add_query=f"""INSERT INTO chatdata values ("{query}","{response}");"""
    c.execute(add_query)
    conn.commit()
    print("joker> Saved your custom response")

    
def search(query):
    link=gs.lucky(query)
    print("Here's the result from google search: "+ link)


def main():
    create_query="""CREATE TABLE IF NOT EXISTS chatdata
                    (query TEXT,
                    response TEXT)"""
    c.execute(create_query)
    print("\t\t Joker chatbot")
    while True:
        query=input("user> ")
        if getresponse(query.lower()):
            while True:
                print("joker> Sorry i cannot understand you yet \n Press 1 to save your custom response to this query \n Press 2 to search google for this query \n Press 3 to neglect the query")     
                choice=input("user> ")
                if choice.isnumeric():
                    if int(choice)==1:
                        saveresponse(query)
                        break
                    elif int(choice)==2:
                        search(query)
                        break
                    elif int(choice)==3:
                        break
                    else:
                        print("Sorry couldnt get you!")
                else:
                    print("Sorry couldnt get you!")

if __name__=="__main__":
    main()
