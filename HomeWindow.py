from PyQt5.QtWidgets import QWidget,QMainWindow,QPushButton,QLineEdit,QLabel,QVBoxLayout,QHBoxLayout,QFrame,QGridLayout,QComboBox,QTableWidget,QTableWidgetItem
from DataBaseOperation import DBOperation
from PyQt5.QtWidgets import QHeaderView,qApp
import PyQt5.QtGui

class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        self.dbOperation=DBOperation()
        widget=QWidget()
        widget.setStyleSheet("background:#000")
        layout_horizontal=QHBoxLayout()
        menu_vertical_layout=QVBoxLayout()

        self.btn_home=QPushButton("Home")
        self.btn_add = QPushButton("Add Vehicle")
        self.btn_manage = QPushButton("Manage Vehicle")
        self.btn_history = QPushButton("History")

        menu_vertical_layout.setContentsMargins(0,0,0,0)
        menu_vertical_layout.setSpacing(0)
        self.btn_home.setStyleSheet("width:200px;height:160px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")


        self.btn_home.clicked.connect(self.showHome)
        self.btn_add.clicked.connect(self.showAdd)
        self.btn_manage.clicked.connect(self.showManage)
        self.btn_history.clicked.connect(self.showHistory)

        menu_frame=QFrame()
        menu_vertical_layout.addWidget(self.btn_home)
        menu_vertical_layout.addWidget(self.btn_add)
        menu_vertical_layout.addWidget(self.btn_manage)
        menu_vertical_layout.addWidget(self.btn_history)
        menu_vertical_layout.addStretch()
        menu_frame.setLayout(menu_vertical_layout)
        #menu_frame.setMinimumWidth(200)
        #menu_frame.setMaximumHeight(200)




        parent_vertical=QVBoxLayout()
        parent_vertical.setContentsMargins(0,0,0,0)
        self.vertical_1=QVBoxLayout()
        self.addHomePageData()


        self.vertical_2=QVBoxLayout()
        self.vertical_2.setContentsMargins(0,0,0,0)
        self.addAddStudentPage()

        self.vertical_3=QVBoxLayout()
        self.vertical_3.setContentsMargins(0,0,0,0)
        self.addManagePage()

        self.vertical_4=QVBoxLayout()
        self.addHistoryPage()


        self.frame_1=QFrame()
        self.frame_1.setMinimumWidth(self.width())
        self.frame_1.setMaximumWidth(self.width())
        self.frame_1.setMaximumHeight(self.width())
        self.frame_1.setMaximumHeight(self.width())

        self.frame_1.setLayout(self.vertical_1)
        self.frame_2=QFrame()
        self.frame_2.setLayout(self.vertical_2)
        self.frame_3=QFrame()
        self.frame_3.setLayout(self.vertical_3)
        self.frame_4=QFrame()
        self.frame_4.setLayout(self.vertical_4)

        parent_vertical.addWidget(self.frame_1)
        parent_vertical.addWidget(self.frame_2)
        parent_vertical.addWidget(self.frame_3)
        parent_vertical.addWidget(self.frame_4)



        layout_horizontal.addWidget(menu_frame)
        layout_horizontal.addLayout(parent_vertical)
        layout_horizontal.setContentsMargins(0,0,0,0)
        parent_vertical.setContentsMargins(0,0,0,0)
        parent_vertical.addStretch()
        #menu_vertical_layout.addStretch()
        layout_horizontal.addStretch()
        widget.setLayout(layout_horizontal)

        self.frame_1.show()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()

        self.setCentralWidget(widget)

    def showHistory(self):
        self.btn_home.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:160px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")


        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.show()

    def showManage(self):
        self.btn_home.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:160px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")


        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_4.hide()
        self.frame_3.show()

    def showAdd(self):
        self.btn_home.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:160px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")

        self.frame_1.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_2.show()

    def showHome(self):
        self.btn_home.setStyleSheet("width:200px;height:160px;font-size:20px;background:blue;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_add.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_manage.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")
        self.btn_history.setStyleSheet("width:200px;height:160px;font-size:20px;background:orange;color:#fff;font-weight:bold;border:1px solid white")

        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_1.show()

    def refreshHome(self):
        while self.gridLayout.count():
            child=self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        row=0
        i=0
        alldata=self.dbOperation.getSlotSpace()
        for data in alldata:
            label=QPushButton("Slot "+str(data[0])+" \n "+str(data[1]))

            if data[3]==1:
                label.setStyleSheet("background-color:green;color:white;padding:5px;width:100px;height:100px;border:1px solid white;text-align:center;font-weight:bold")
            else:
                label.setStyleSheet("background-color:red;color:white;padding:5px;width:100px;height:100px;border:1px solid white;text-align:center;font-weight:bold")

            if i%5==0:
                i=0
                row=row+1

            self.gridLayout.addWidget(label,row,i)
            i=i+1


    def addHomePageData(self):
        self.vertical_1.setContentsMargins(0,0,0,0)
        button=QPushButton("Refresh")

        button.clicked.connect(self.refreshHome)
        vertical_layout=QVBoxLayout()
        vertical_layout.setContentsMargins(0,0,0,0)
        frame=QFrame()

        horizontal=QHBoxLayout()
        horizontal.setContentsMargins(0,0,0,0)
        vertical_layout.addLayout(horizontal)

        alldata=self.dbOperation.getSlotSpace()
        self.gridLayout=QGridLayout()
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(0)
        vertical_layout.addWidget(button)
        vertical_layout.addLayout(self.gridLayout)

        row=0
        i=0
        for data in alldata:
            label=QPushButton("Slot "+str(data[0])+" \n "+str(data[1]))

            if data[3]==1:
                label.setStyleSheet("background-color:green;color:white;padding:5px;width:100px;height:100px;border:1px solid white;text-align:center;font-weight:bold")
            else:
                label.setStyleSheet("background-color:red;color:white;padding:5px;width:100px;height:100px;border:1px solid white;text-align:center;font-weight:bold")

            if i%5==0:
                i=0
                row=row+1

            self.gridLayout.addWidget(label,row,i)
            i=i+1

        frame.setLayout(vertical_layout)
        self.vertical_1.addWidget(frame)
        self.vertical_1.addStretch()

    def addAddStudentPage(self):
        layout=QVBoxLayout()
        frame=QFrame()


        name_label=QLabel("Name : ")
        name_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        mobile_label=QLabel("Mobile : ")
        mobile_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        vechicle_label=QLabel("Vehicle No : ")
        vechicle_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        vechicle_type=QLabel("Vehicle Type : ")
        vechicle_type.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        error_label=QLabel("")
        error_label.setStyleSheet("color:red;padding:8px 0px;font-size:20px")

        name_input=QLineEdit()
        name_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        mobile_input=QLineEdit()
        mobile_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        vehicle_input=QLineEdit()
        vehicle_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
        vtype=QComboBox()
        vtype.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;border:1px solid white")
        vtype.addItem("2 Wheeler")
        vtype.addItem("4 Wheeler")

        button=QPushButton("Add Vehicle")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")

        layout.addWidget(name_label)
        layout.addWidget(name_input)
        layout.addWidget(mobile_label)
        layout.addWidget(mobile_input)
        layout.addWidget(vechicle_label)
        layout.addWidget(vehicle_input)
        layout.addWidget(vechicle_type)
        layout.addWidget(vtype)
        layout.addWidget(button)
        layout.addWidget(error_label)

        layout.setContentsMargins(0,0,0,0)
        frame.setMinimumHeight(self.height())
        frame.setMinimumWidth(self.width())
        frame.setMaximumHeight(self.width())
        frame.setMaximumWidth(self.width())

        layout.addStretch()
        frame.setLayout(layout)
        button.clicked.connect(lambda:self.addVehicles(name_input.text(),vehicle_input.text(),mobile_input.text(),vtype.currentIndex(),error_label))
        self.vertical_2.addWidget(frame)

    def addVehicles(self,name,vehicleno,mobile,index,error_label):
        vtp=2
        if index==0:
            vtp=2
        else:
            vtp=4


        data=self.dbOperation.AddVehicles(name,vehicleno,mobile,str(vtp))
        if data==True:
            error_label.setText("Added Successfully")
        elif data==False:
            error_label.setText("Failed to Add Vehicle")
        else:
            error_label.setText(str(data))



    def addManagePage(self):
        data=self.dbOperation.getCurrentVehicle()
        self.table=QTableWidget()
        self.table.setStyleSheet("background:#fff")
        self.table.resize(self.width(),self.height())
        self.table.setRowCount(len(data))
        self.table.setColumnCount(7)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("ID"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem("VEHICLE No"))
        self.table.setHorizontalHeaderItem(3,QTableWidgetItem("MOBILE"))
        self.table.setHorizontalHeaderItem(4,QTableWidgetItem("VEHICLE TYPE"))
        self.table.setHorizontalHeaderItem(5,QTableWidgetItem("ENTRY TIME"))
        self.table.setHorizontalHeaderItem(6,QTableWidgetItem("ACTION"))

        loop=0
        for smalldata in data:
            self.table.setItem(loop,0,QTableWidgetItem(str(smalldata[0])))
            self.table.setItem(loop,1,QTableWidgetItem(str(smalldata[1])))
            self.table.setItem(loop,2,QTableWidgetItem(str(smalldata[6])))
            self.table.setItem(loop,3,QTableWidgetItem(str(smalldata[2])))
            self.table.setItem(loop,4,QTableWidgetItem(str(smalldata[7])))
            self.table.setItem(loop,5,QTableWidgetItem(str(smalldata[3])))
            self.button_exit=QPushButton("Exit")
            self.button_exit.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
            self.table.setCellWidget(loop,6,self.button_exit)
            self.button_exit.clicked.connect(self.exitCall)
            loop=loop+1

        frame=QFrame()
        layout=QVBoxLayout()
        button=QPushButton("Refresh")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refreshManage)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(button)
        layout.addWidget(self.table)
        frame.setLayout(layout)
        frame.setContentsMargins(0,0,0,0)
        frame.setMaximumWidth(self.width())
        frame.setMinimumWidth(self.width())
        frame.setMaximumHeight(self.height())
        frame.setMinimumHeight(self.height())
        self.vertical_3.addWidget(frame)
        self.vertical_3.addStretch()

    def refreshManage(self):
        data=self.dbOperation.getCurrentVehicle()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(7)
        loop=0
        for smalldata in data:
            self.table.setItem(loop,0,QTableWidgetItem(str(smalldata[0])))
            self.table.setItem(loop,1,QTableWidgetItem(str(smalldata[1])))
            self.table.setItem(loop,2,QTableWidgetItem(str(smalldata[6])))
            self.table.setItem(loop,3,QTableWidgetItem(str(smalldata[2])))
            self.table.setItem(loop,4,QTableWidgetItem(str(smalldata[7])))
            self.table.setItem(loop,5,QTableWidgetItem(str(smalldata[3])))
            self.button_exit=QPushButton("Exit")
            self.table.setCellWidget(loop,6,self.button_exit)
            self.button_exit.clicked.connect(self.exitCall)
            loop=loop+1


    def refreshHistory(self):
        self.table1.clearContents()
        data=self.dbOperation.getAllVehicle()
        loop=0
        self.table1.setRowCount(len(data))
        self.table1.setColumnCount(7)
        for smalldata in data:
            self.table1.setItem(loop,0,QTableWidgetItem(str(smalldata[0])))
            self.table1.setItem(loop,1,QTableWidgetItem(str(smalldata[1])))
            self.table1.setItem(loop,2,QTableWidgetItem(str(smalldata[6])))
            self.table1.setItem(loop,3,QTableWidgetItem(str(smalldata[2])))
            self.table1.setItem(loop,4,QTableWidgetItem(str(smalldata[7])))
            self.table1.setItem(loop,5,QTableWidgetItem(str(smalldata[3])))
            self.table1.setItem(loop,6,QTableWidgetItem(str(smalldata[4])))
            loop=loop+1

    def addHistoryPage(self):
        data=self.dbOperation.getAllVehicle()
        self.table1=QTableWidget()
        self.table1.resize(self.width(),self.height())
        self.table1.setRowCount(len(data))
        self.table1.setStyleSheet("background:#fff")
        self.table1.setColumnCount(7)

        button=QPushButton("Refresh")
        button.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;background:green;border:1px solid white")
        button.clicked.connect(self.refreshHistory)


        self.table1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table1.setHorizontalHeaderItem(0,QTableWidgetItem("ID"))
        self.table1.setHorizontalHeaderItem(1,QTableWidgetItem("Name"))
        self.table1.setHorizontalHeaderItem(2,QTableWidgetItem("VEHICLE No"))
        self.table1.setHorizontalHeaderItem(3,QTableWidgetItem("MOBILE"))
        self.table1.setHorizontalHeaderItem(4,QTableWidgetItem("VEHICLE TYPE"))
        self.table1.setHorizontalHeaderItem(5,QTableWidgetItem("ENTRY TIME"))
        self.table1.setHorizontalHeaderItem(6,QTableWidgetItem("EXIT TIME"))

        loop=0
        for smalldata in data:
            self.table1.setItem(loop,0,QTableWidgetItem(str(smalldata[0])))
            self.table1.setItem(loop,1,QTableWidgetItem(str(smalldata[1])))
            self.table1.setItem(loop,2,QTableWidgetItem(str(smalldata[6])))
            self.table1.setItem(loop,3,QTableWidgetItem(str(smalldata[2])))
            self.table1.setItem(loop,4,QTableWidgetItem(str(smalldata[7])))
            self.table1.setItem(loop,5,QTableWidgetItem(str(smalldata[3])))
            self.table1.setItem(loop,6,QTableWidgetItem(str(smalldata[4])))
            loop=loop+1

        self.frame5=QFrame()
        self.layout1=QVBoxLayout()
        self.layout1.setContentsMargins(0,0,0,0)
        self.layout1.setSpacing(0)
        self.layout1.addWidget(button)
        self.layout1.addWidget(self.table1)
        self.frame5.setLayout(self.layout1)
        self.frame5.setContentsMargins(0,0,0,0)
        self.frame5.setMaximumWidth(self.width())
        self.frame5.setMinimumWidth(self.width())
        self.frame5.setMaximumHeight(self.height())
        self.frame5.setMinimumHeight(self.height())
        self.vertical_4.addWidget(self.frame5)
        self.vertical_4.addStretch()


    def exitCall(self):
        btton=self.sender()
        if btton:
            row=self.table.indexAt(btton.pos()).row()
            id =str(self.table.item(row,0).text())
            self.dbOperation.exitVehicle(id)
            self.table.removeRow(row)