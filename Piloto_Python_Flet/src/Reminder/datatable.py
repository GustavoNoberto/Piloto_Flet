from flet import *
import flet as ft
from database import DatabaseConnection
from ReminderView import Page

page = Page


db = DatabaseConnection()  # Cria uma instância da classe DatabaseConnection
db.connect()  # 

#Colunas da tabela reminder
tb = DataTable(
            expand=True,
            border_radius=8,
            border=border.all(2, "#ebebeb"),
            horizontal_lines=border.BorderSide(1, "#ebebeb"),
            columns=[
                DataColumn(
                    Text("ID Bot", size=12, color="black", 
                            weight="bold")
                ),
                DataColumn(
                    Text("Date Register", size=12, color="black", 
                            weight="bold")
                ),
                DataColumn(
                    Text("Days To Reminder", size=12, color="black", 
                            weight="bold")
                ),
                DataColumn(
                    Text("Approved", size=12, color="black", 
                            weight="bold")
                ),
                DataColumn(
                    Text("Register Owner", size=12, color="black", 
                            weight="bold")
                ),
                DataColumn(
                    Text("Send To Original Channel", size=12, color="black", 
                            weight="bold")
                ),
                DataColumn(
                    Text("Channel ID", size=12, color="black", 
                            weight="bold")
                ),
                DataColumn(
                    Text("TS Slack", size=12, color="black", 
                            weight="bold")
                ),
                DataColumn(
                    Text("ACTIONS", size=12, color="black", 
                            weight="bold")
                ),
                
            ],

            rows=[],
        )


#funcao que deleta o reminder do banco de dados
def showdelete(e):
        


        try:
            infos = str(e.control.data).split("|")
            idbot = infos[0]
            daysReminder = infos[1]
            cursor = db.conn.cursor()
            #print(("DELETE FROM RPA_GERENCIADOR_REMINDERS WHERE ID_BOT='"+str(idbot)+"' and DAYS_TO_REMINDER='"+str(daysReminder)+"'"))
            cursor.execute("DELETE FROM RPA_GERENCIADOR_REMINDERS WHERE ID_BOT='"+str(idbot)+"' and DAYS_TO_REMINDER='"+str(daysReminder)+"'")
            db.commit()
            #close_dlg
            print("success delete")
            tb.rows.clear()	
            calldb()
            tb.update()

        except Exception as e:
            print(e)
'''
def close_dlg(e):
        dlg_modal.open = False
        Page.update()

dlg_modal = ft.AlertDialog(
    modal=True,
    title=ft.Text("Confirm Delete"),
    content=ft.Text("Do you really want to delete?"),
    actions=[
        ft.TextButton("Yes", on_click=showdelete),
        ft.TextButton("No", on_click=close_dlg),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
    on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )


def open_dlg(e):
    page.dialog = dlg_modal
    dlg_modal.open = True
    page.update()
'''
idbot_edit = TextField(label="idBot",expand=1,border_radius=15, disabled=True) 
daysReminder_edit = TextField(label="Days To Reminder",expand=1,border_radius=15)
owner_edit = TextField(label="Owner",expand=3,border_radius=15, disabled=True)
slackChannel_edit = TextField(label="Slack Channel",expand=1,border_radius=15)
oldDaysReminder_edit = TextField(label="Old Days",expand=1,border_radius=15)


def hidedlg(e):
        dlg.visible = False
        dlg.update()


#funcao que armazena os valores na tela de edicao do reminder
def showedit(e):
        data_edit = e.control.data
        idbot_edit.value = data_edit['ID_BOT']  
        daysReminder_edit.value = data_edit['DAYS_TO_REMINDER']
        oldDaysReminder_edit.value = data_edit['DAYS_TO_REMINDER']
        owner_edit.value = data_edit['REGISTER_OWNER']
        slackChannel_edit.value = data_edit['CHANNEL_ID']
        dlg.visible = True
        dlg.update()

#Funcao que atualiza o reminder no banco ORACLE


def updateandsave(e):
        try:            
            cursor = db.conn.cursor()
            print("UPDATE RPA_GERENCIADOR_REMINDERS \
                           SET DAYS_TO_REMINDER='"+str(daysReminder_edit.value)+"', \
                            CHANNEL_ID='"+str(slackChannel_edit.value)+"' \
                                WHERE ID_BOT='"+str(idbot_edit.value)+"' \
                                    and DAYS_TO_REMINDER='"+str(oldDaysReminder_edit.value)+"'")
            cursor.execute("UPDATE RPA_GERENCIADOR_REMINDERS \
                           SET DAYS_TO_REMINDER='"+str(daysReminder_edit.value)+"', \
                            CHANNEL_ID='"+str(slackChannel_edit.value)+"' \
                                WHERE ID_BOT='"+str(idbot_edit.value)+"' \
                                    and DAYS_TO_REMINDER='"+str(oldDaysReminder_edit.value)+"'")
            db.commit()
            print("success Edit")
            tb.rows.clear()	
            calldb()
            dlg.visible = False
            dlg.update()
            tb.update()
        except Exception as e:
            print(e)

#funcao que realizar a busca dos dados no ORACLE
def calldb():
        cursor = db.conn.cursor()
        cursor.execute("SELECT * FROM RPA_GERENCIADOR_REMINDERS ORDER BY DATE_REGISTER DESC")
        reminders = cursor.fetchall()
        #print(reminders)
        if not reminders == "":
            keys = ['ID_BOT', 'DATE_REGISTER', 'DAYS_TO_REMINDER', 'APPROVED', 'REGISTER_OWNER', 'SEND_TO_ORIGINAL_CHANNEL', 'CHANNEL_ID', 'TS_SLACK']
            result = [dict(zip(keys, values)) for values in reminders]
            for x in result:
                tb.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(x['ID_BOT'])),
                            DataCell(Text(x['DATE_REGISTER'])),
                            DataCell(Text(x['DAYS_TO_REMINDER'])),
                            DataCell(Text(x['APPROVED'])),
                            DataCell(Text(x['REGISTER_OWNER'])),
                            DataCell(Text(x['SEND_TO_ORIGINAL_CHANNEL'])),
                            DataCell(Text(x['CHANNEL_ID'])),
                            DataCell(Text(x['TS_SLACK'])),
                            DataCell(Row([
                                IconButton(icon=icons.CREATE_OUTLINED,data=x,on_click=showedit),
                                IconButton(icon=icons.DELETE_OUTLINE,data=(str(x['ID_BOT'])+'|'+str(x['DAYS_TO_REMINDER'])),on_click=showdelete),
                                ])),
                        ],
                    ),

            )

#chamada do select no banco de dados
calldb()



def close_window_button():
        return Container(
                alignment=alignment.top_right,
                content=ElevatedButton(
                    on_click=hidedlg,
                    bgcolor="#9932CC",
                    color="white",
                    content=Row(
                    controls=[
                        Icon(name=icons.CLOSE,size=12,),
                        Text(
                            "Fechar",
                            size=11,
                            weight="bold",
                        ),
                    ],
                ),
                    style=ButtonStyle(
                        shape={
                            "": RoundedRectangleBorder(radius=50),
                        },
                        color={
                            "": "white",
                        },
                    ),
                    height=40,
                    width="auto"
                )
            )

def format_update_button():
        return Container(
            alignment=alignment.center,
            content=ElevatedButton(
                on_click=updateandsave,
                bgcolor="#9932CC",
                color="white",
                content=Row(
                    controls=[
                        #Icon(name=icons.ADD_ROUNDED,size=12,),
                        Text(
                            "Atualizar",
                            size=11,
                            weight="bold",
                        ),
                    ],
                ),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=50),
                    },
                    color={
                        "": "white",
                    },
                ),
                height=42,
                width="auto"
            )
        )

def editTitle():
    return Container(content=Text("Editar Reminder",size=25, color="#9932CC", italic=True))

#Container de edit reminder
dlg = Container(
	bgcolor="white10",
    border=border.all(1, "#ebebeb"),
    border_radius=10,
    padding=15,
    height="auto",
			content=Column([
                Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    editTitle(),
                    close_window_button()]),
                Row([
                idbot_edit,
				daysReminder_edit,
				owner_edit,
				slackChannel_edit,
                #dateRegister_edit,
                    ]),        
				Row(alignment=MainAxisAlignment.CENTER, controls=[format_update_button(),]),
				])
)             
    

dlg.visible = False

mytable = Column([
	dlg,
    Row(
              
        controls=[tb]
    )
	
	])
