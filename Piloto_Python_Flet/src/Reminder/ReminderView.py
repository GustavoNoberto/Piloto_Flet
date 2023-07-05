from flet import *
import flet as ft
from database import DatabaseConnection
from datatable import *

db = DatabaseConnection()  # Cria uma instância da classe DatabaseConnection
db.connect()  #Abre conexao com a base de dados ORACLE

def main(page: Page):
    page.scroll="auto"
    page.bgcolor="#fdfdfd"
    page.padding=10
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }
    page.theme = Theme(font_family="Kanit")

    img = Image(
        #src = r"teste.jpg",
        src_base64="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",
        width=60,
        height=60,
        #offset=transform.Offset(0, -0.1),
        animate_offset=animation.Animation(),
    )

    def header():
        return Container(
            expand="auto",
            height=60,
            bgcolor="#9932CC",
            border_radius=border_radius.only(top_left=15, top_right=15),
            padding=padding.only(left=15,right=15),
            content=Row(
                expand=True, 
                alignment=MainAxisAlignment.CENTER, 
                controls=[
                    Container(content=Text("Reminder Manager",size=25, color="WHITE",font_family="Kanit")),
                    img,
                ],
            ),
        )

    def close_window_button():
        return Container(
                alignment=alignment.top_right,
                content=ElevatedButton(
                    on_click=hideRegister,
                    bgcolor="#9932CC",
                    color="white",
                    content=Row(
                    controls=[
                        Icon(name=icons.CLOSE,size=12,),
                        Text(
                            "Close",
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

    def format_insert_button():
        return Container(
            alignment=alignment.center,
            content=ElevatedButton(
                on_click=savedata,
                bgcolor="#9932CC",
                color="white",
                content=Row(
                    controls=[
                        #Icon(name=icons.ADD_ROUNDED,size=12,),
                        Text(
                            "Register",
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

    def savedata(e):
        try:
            # INPUT TO DATABASE
            cursor = db.conn.cursor()
            if checkQuickRegistration.value == True:
                listDayReg = [15,45,60]
                for day in listDayReg:
                    cursor.execute("INSERT INTO RPA.RPA_GERENCIADOR_REMINDERS \
                        (ID_BOT, DATE_REGISTER, DAYS_TO_REMINDER, APPROVED, REGISTER_OWNER, SEND_TO_ORIGINAL_CHANNEL, CHANNEL_ID, TS_SLACK) \
                        VALUES('"+str(idBot.value)+"', "+str(dataReg)+", '"+str(day)+"', '"+str(approved)+"', 'QuickRegistration', '"+str(sendOrigChannel)+"', '123456789', '"+str(tsSlack)+"')")
                    db.commit()
            else:
                cursor.execute("INSERT INTO RPA.RPA_GERENCIADOR_REMINDERS \
                    (ID_BOT, DATE_REGISTER, DAYS_TO_REMINDER, APPROVED, REGISTER_OWNER, SEND_TO_ORIGINAL_CHANNEL, CHANNEL_ID, TS_SLACK) \
                    VALUES('"+str(idBot.value)+"', "+str(dataReg)+", '"+str(daysToReminder.value)+"', '"+str(approved)+"', '"+str(owner.value)+"', '"+str(sendOrigChannel)+"', '"+str(slackChannel.value)+"', '"+str(tsSlack)+"')")
                db.commit()
            print("success")

            # ADD SNACKBAR IF SUCCESS INPUT TO DATABASE

            page.snack_bar = SnackBar(
                Text("Reminder successfully added!"),
                bgcolor="green"
                )

            page.snack_bar.open = True
            
            # REFRESH TABLE
            tb.rows.clear()
            calldb()
            tb.update()
            page.update()
            inputNewData.visible = False
            inputNewData.update()


        except Exception as e:
            print(e)

    def showRegister(e):
        inputNewData.visible = True
        inputNewData.update()

    def hideRegister(e):
        inputNewData.visible = False
        inputNewData.update()
             
    def changeQuickFields(e):
        if checkQuickRegistration.value == True:
            daysToReminder.disabled = True
            owner.disabled = True
            slackChannel.disabled = True
        else:
            daysToReminder.disabled = False
            owner.disabled = False
            slackChannel.disabled = False
        inputNewData.update()

    
    searchIdBot = TextField(label="IdBot",height=42,width=220,border_radius=15)
    idBot = TextField(label="IdBot",expand=1,border_radius=15) 
    daysToReminder = TextField(label="Days To Reminder",expand=1,border_radius=15)
    owner = TextField(label="Owner", suffix_text="@nubank.com.br",expand=3,border_radius=15)
    approved = "0"
    sendOrigChannel = "0"
    dataReg = "sysdate"
    slackChannel = TextField(label="Slack Channel",expand=1,border_radius=15)
    tsSlack = "NULL"
    checkQuickRegistration = ft.Checkbox(label="Quick Registration? 3 records will be registered 15, 45 and 60 days for reminder*", value=False, on_change=changeQuickFields)

    #Container de cadastro novo reminder
    inputNewData = Container(
                bgcolor="white10",
                border=border.all(1, "#ebebeb"),
                border_radius=10,
                padding=15,
                height="auto",
                content=Column(
                    expand=True,
                    controls=[
                        Row(alignment=MainAxisAlignment.SPACE_BETWEEN, controls=[checkQuickRegistration, close_window_button()]),
                        #Row([ft.Text("3 records will be registered 15, 45 and 60 days for reminder*",size=15,italic=True)]),
                        Row([
                        idBot, 
                        daysToReminder,
                        slackChannel,
                        owner,
                        ]),
                        Row(alignment=MainAxisAlignment.CENTER, controls=[format_insert_button(),]),
                    ]
                )                        
            )

    inputNewData.visible = False

    textRegisterButton = Text(
                "New Reminder",
                size=14,
                color="white",
                weight="w700",
                offset= transform.Offset(0,0),
                animate_offset=animation.Animation(duration=900, curve='decelerate'),
                animate_opacity=200,
                )

    buttonRegistrationReminder = IconButton(
                icon=icons.ADD,
                icon_color="white",
                icon_size=15,
                offset= transform.Offset(0,0),
                animate_offset=animation.Animation(duration=900, curve="decelerate"),
                rotate= transform.Rotate(11,alignment=alignment.center),
                animate_rotation= animation.Animation(duration=600, curve="decelerate"),
                scale=Scale(scale=1),
                animate_scale= animation.Animation(duration=600, curve="bounceOut")
                )

    newReminderButton = Container(
                height=42,
                width=220,
                bgcolor="#9932CC",
                border_radius=10,
                on_hover=lambda e: NewButton(e),
                on_click=showRegister,
                content=Row(
                        controls=[
                            buttonRegistrationReminder,
                            textRegisterButton,
                        ]
                )
            )

    def NewButton(e):
        if e.data == "true":
            buttonRegistrationReminder.rotate.angle += 1.5
            buttonRegistrationReminder.offset = transform.Offset(0.5, 0)
            buttonRegistrationReminder.scale = transform.Scale(1.25)
            buttonRegistrationReminder.update()
        else:
            buttonRegistrationReminder.rotate.angle -= 1.5
            buttonRegistrationReminder.offset = transform.Offset(00, 0)
            buttonRegistrationReminder.scale = transform.Scale(1)
            buttonRegistrationReminder.update()

    textSearchButton = Text(
                "Search Reminder",
                size=14,
                color="white",
                weight="w700",
                offset= transform.Offset(0,0),
                animate_offset=animation.Animation(duration=900, curve='decelerate'),
                animate_opacity=200,
                )

    buttonSearchReminder = IconButton(
                #icon=icons.APP_REGISTRATION,
                icon=icons.SEARCH,
                icon_color="white",
                icon_size=15,
                offset= transform.Offset(0,0),
                animate_offset=animation.Animation(duration=900, curve="decelerate"),
                rotate= transform.Rotate(11,alignment=alignment.center),
                animate_rotation= animation.Animation(duration=600, curve="decelerate"),
                scale=Scale(scale=1),
                animate_scale= animation.Animation(duration=600, curve="bounceOut")
                )

    newSearchButton = Container(
                height=42,
                width=220,
                bgcolor="#9932CC",
                border_radius=10,
                on_click=lambda e: searchReminder(e),
                on_hover=lambda e: animationSearchButton(e),
                content=Row(
                        controls=[
                            buttonSearchReminder,
                            textSearchButton,
                            
                        ]
                )
            )
    
    def searchReminder(e):
        cursor = db.conn.cursor()
        print("SELECT * FROM RPA_GERENCIADOR_REMINDERS where ID_BOT = '"+str(searchIdBot.value)+"' ORDER BY DATE_REGISTER DESC")
        cursor.execute("SELECT * FROM RPA_GERENCIADOR_REMINDERS where ID_BOT = '"+str(searchIdBot.value)+"' ORDER BY DATE_REGISTER DESC")
        reminders = cursor.fetchall()
        print(reminders)
        if len(reminders) != 0:
            
            tb.rows.clear()
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
            tb.update()
            page.update()
        else:
            open_dlg(e)
            calldb()
            tb.update()
            page.update()
            inputNewData.visible = False
            inputNewData.update()
      
    dialog = ft.AlertDialog(
        title=ft.Text("ID not found!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        page.dialog = dialog
        dialog.open = True
        page.update()

    def animationSearchButton(e):
        if e.data == "true":
            buttonSearchReminder.rotate.angle += 1.5
            buttonSearchReminder.offset = transform.Offset(0.5, 0)
            buttonSearchReminder.scale = transform.Scale(1.25)
            buttonSearchReminder.update()
        else:
            buttonSearchReminder.rotate.angle -= 1.5
            buttonSearchReminder.offset = transform.Offset(00, 0)
            buttonSearchReminder.scale = transform.Scale(1)
            buttonSearchReminder.update()

    rowSearch = Row([
        searchIdBot, newSearchButton
    ])
    

    page.add(
        Column( 
            controls=[
            header(),
            Divider(height=2, color="transparent"),
            Column(
                    scroll='always',
                    expand="auto",
                    controls=[
                        Row(alignment=MainAxisAlignment.SPACE_BETWEEN, controls=[newReminderButton, rowSearch]),
                        inputNewData,
                        mytable
                    ]
                )     
            ])    
        )
    



if __name__ == "__main__":
    flet.app(target=main, view=flet.WEB_BROWSER)