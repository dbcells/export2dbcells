# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sergio/.local/share/QGIS/QGIS3/profiles/default/python/plugins/export2dbcells/export_dbcells_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExportDBCellsDialogBase(object):
    def setupUi(self, ExportDBCellsDialogBase):
        ExportDBCellsDialogBase.setObjectName("ExportDBCellsDialogBase")
        ExportDBCellsDialogBase.resize(469, 324)
        self.gridLayout = QtWidgets.QGridLayout(ExportDBCellsDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QVBoxLayout()
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelRDF = QtWidgets.QLabel(ExportDBCellsDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRDF.sizePolicy().hasHeightForWidth())
        self.labelRDF.setSizePolicy(sizePolicy)
        self.labelRDF.setMinimumSize(QtCore.QSize(108, 0))
        self.labelRDF.setObjectName("labelRDF")
        self.horizontalLayout.addWidget(self.labelRDF)
        self.lineTTL = QtWidgets.QLineEdit(ExportDBCellsDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineTTL.sizePolicy().hasHeightForWidth())
        self.lineTTL.setSizePolicy(sizePolicy)
        self.lineTTL.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineTTL.setObjectName("lineTTL")
        self.horizontalLayout.addWidget(self.lineTTL)
        self.buttonTTL = QtWidgets.QToolButton(ExportDBCellsDialogBase)
        self.buttonTTL.setObjectName("buttonTTL")
        self.horizontalLayout.addWidget(self.buttonTTL)
        self.formLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelID = QtWidgets.QLabel(ExportDBCellsDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelID.sizePolicy().hasHeightForWidth())
        self.labelID.setSizePolicy(sizePolicy)
        self.labelID.setMinimumSize(QtCore.QSize(108, 0))
        self.labelID.setObjectName("labelID")
        self.horizontalLayout_2.addWidget(self.labelID)
        self.comboID = QtWidgets.QComboBox(ExportDBCellsDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboID.sizePolicy().hasHeightForWidth())
        self.comboID.setSizePolicy(sizePolicy)
        self.comboID.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboID.setObjectName("comboID")
        self.horizontalLayout_2.addWidget(self.comboID)
        spacerItem = QtWidgets.QSpacerItem(26, 26, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkSelected = QtWidgets.QCheckBox(ExportDBCellsDialogBase)
        self.checkSelected.setChecked(True)
        self.checkSelected.setObjectName("checkSelected")
        self.verticalLayout_2.addWidget(self.checkSelected)
        self.checkGeometries = QtWidgets.QCheckBox(ExportDBCellsDialogBase)
        self.checkGeometries.setObjectName("checkGeometries")
        self.verticalLayout_2.addWidget(self.checkGeometries)
        self.atributos = QtWidgets.QLabel(ExportDBCellsDialogBase)
        self.atributos.setObjectName("atributos")
        self.verticalLayout_2.addWidget(self.atributos)
        self.tableAttributes = QtWidgets.QTableWidget(ExportDBCellsDialogBase)
        self.tableAttributes.setObjectName("tableAttributes")
        self.tableAttributes.setColumnCount(0)
        self.tableAttributes.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableAttributes)
        self.formLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ExportDBCellsDialogBase)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.formLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(ExportDBCellsDialogBase)
        QtCore.QMetaObject.connectSlotsByName(ExportDBCellsDialogBase)

    def retranslateUi(self, ExportDBCellsDialogBase):
        _translate = QtCore.QCoreApplication.translate
        ExportDBCellsDialogBase.setWindowTitle(_translate("ExportDBCellsDialogBase", "ExportDBcells"))
        self.labelRDF.setText(_translate("ExportDBCellsDialogBase", "TTL (RDF)  File"))
        self.buttonTTL.setText(_translate("ExportDBCellsDialogBase", "..."))
        self.labelID.setText(_translate("ExportDBCellsDialogBase", "ID"))
        self.checkSelected.setText(_translate("ExportDBCellsDialogBase", "Selected"))
        self.checkGeometries.setText(_translate("ExportDBCellsDialogBase", "Export geometries"))
        self.atributos.setText(_translate("ExportDBCellsDialogBase", "atributos"))
