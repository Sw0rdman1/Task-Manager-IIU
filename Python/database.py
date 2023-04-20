import mysql.connector

# DATABASE
mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    passwd='admin',
    database='tasks'
)


def initalConnectToDB():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")

    flag = False

    for tb in mycursor:
        if tb.__contains__('tasks'):
            flag = True;

    if flag:
        print('Table Tasks already exists!')
    else:
        mycursor.execute(
            "CREATE TABLE tasks ( id INTEGER(10) PRIMARY KEY NOT NULL AUTO_INCREMENT ,title VARCHAR(255), content VARCHAR(255), done BOOLEAN default FALSE)")
        putGeneratedTasksInDB(mydb)
        print("Table Tasks created!")


def putGeneratedTasksInDB(mydb):
    mycursor = mydb.cursor()
    sqlFormula = 'INSERT INTO tasks (id,  title, content, done) VALUES (%s,%s,%s,%s)'
    task1 = (1, "Task 1", "Buy milk in shop", 0)
    task2 = (2, "Task 2", "Write email", 0)
    task3 = (3, "Task 3", "Code a chat application", 1)
    tasks = [task1, task2, task3]

    mycursor.executemany(sqlFormula, tasks)
    print("Dummy tasks created!")
    mydb.commit()


def getAllTasksFromDB():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tasks")
    myresult = mycursor.fetchall()

    print("All tasks from database!")

    tasks = []

    for oneRow in myresult:
        tasks.append({"id": oneRow[0], "title": oneRow[1], "content": oneRow[2], "done": oneRow[3]})
    return tasks


def updateTaskInDB(task):
    mycursor = mydb.cursor()
    sqlFormula = "UPDATE tasks SET done = %s WHERE id = %s"
    parameters = (task["done"], task["id"])
    mycursor.execute(sqlFormula, parameters)
    print("Task [id = {}] updated".format(task["id"]))
    mydb.commit()

def addTaskToDB(task):
    mycursor = mydb.cursor()
    sqlFormula = 'INSERT INTO tasks (title, content, done ) VALUES (  %s, %s, %s)'
    parameters = (task["title"],task["content"],task["done"])
    mycursor.execute(sqlFormula, parameters)
    mydb.commit()

def findNextID():
    mycursor = mydb.cursor()
    query = "SELECT MAX(id) FROM tasks"
    mycursor.execute(query)

    # Fetch the result and return the biggest ID as an integer
    result = mycursor.fetchone()
    biggest_id = result[0]
    return biggest_id + 1

def deleteTaskFromDB(request_data):
    mycursor = mydb.cursor()
    sqlFormula = 'DELETE FROM tasks WHERE id = %s'
    parameters = (request_data["id"],)
    mycursor.execute(sqlFormula, parameters)
    print("Task [id = {}] deleted from database".format(request_data["id"]))
    mydb.commit()
