# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ExportDBCells
                                 A QGIS plugin
 exportar dados para o dbcells
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-11-19
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Sergio Costa
        email                : sergio.costa@ufma.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction,QFileDialog, QCheckBox, QComboBox

from qgis.core import (
  QgsGeometry,
  QgsGeometryCollection,
  QgsPoint,
  QgsPointXY,
  QgsWkbTypes,
  Qgis,
  QgsProject,
  QgsFeatureRequest,
  QgsVectorLayer,
  QgsDistanceArea,
  QgsUnitTypes,
  QgsCoordinateTransform,
  QgsMultiPolygon,
  QgsCoordinateReferenceSystem
)

from qgis.utils import iface

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .export_dbcells_dialog import ExportDBCellsDialog
import os.path


plugin_dir = os.path.dirname(__file__)

try:
    import pip
except:
    exec(open(os.path.join(plugin_dir, "get_pip.py")).read())
    import pip
    # just in case the included version is old
    pip.main(['install','--upgrade','pip'])

try:
    import simpot
except:
    pip.main(['install', 'simpot'])

try:
    import rdflib
except:
    pip.main(['install', 'rdflib'])


from simpot import serialize_to_rdf, serialize_to_rdf_file, RdfsClass, BNamespace, graph

from rdflib import Namespace, Literal, URIRef,RDF, Graph
from rdflib.namespace import DC, FOAF

namespaces = {
    'cell': (Namespace("http://purl.org/ontology/dbcells/cells#"), 'turtle'),
    'geo' : (Namespace ("http://www.opengis.net/ont/geosparql#"), 'xml'),
    'amz' : (Namespace ("http://purl.org/ontology/dbcells/amazon"), "ttl")
}

CELL = namespaces['cell'][0]
GEO = namespaces['geo'][0]

#https://stackoverflow.com/questions/2466191/set-attributes-from-dictionary-in-python
class Cell ():
    
    asWkt = GEO.asWKT
    
    @RdfsClass(CELL.Cell,"http://www.dbcells.org/epsg4326/")
    @BNamespace('geo', GEO)
    @BNamespace('cells', CELL)
    def __init__(self, dict):
        self.id = dict["id"]
        dict.pop("id")
        if ('asWkt' in dict):
            self.asWkt = Literal(dict["asWkt"])
            dict.pop('asWkt')

        for key in dict:
            setattr(self, key, Literal(dict[key]))

class ExportDBCells:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'ExportDBCells_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&DBCells')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        self.loadVocabularies() # se demorar muito, nao sei o que pode acontecer :(

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('ExportDBCells', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToVectorMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/export_dbcells/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Export Layer to DBCells'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginVectorMenu(
                self.tr(u'&DBCells'),
                action)
            self.iface.removeToolBarIcon(action)

    def vocabulariesCombo(self):
        comboBox = QComboBox()
        for attr in self.vocabularies:
            comboBox.addItem(attr)
        return comboBox

    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = ExportDBCellsDialog()

        layer = self.iface.activeLayer()
        fields = layer.fields()
        
        
        self.dlg.tableAttributes.setRowCount(len(fields))
        self.dlg.tableAttributes.setColumnCount(2)
        self.dlg.tableAttributes.setHorizontalHeaderLabels(["Name", "Vocabulary"])
        
        i = 0
        for field in fields:
            self.dlg.comboID.addItem(field.name())
            checkbox = QCheckBox(field.name())
            self.dlg.tableAttributes.setCellWidget(i, 0, checkbox)
            self.dlg.tableAttributes.setCellWidget(i, 1, self.vocabulariesCombo())
            i += 1

        self.dlg.buttonTTL.clicked.connect(self.outputFile)

        self.dlg.buttonBox.accepted.connect(self.saveFile)
        self.dlg.buttonBox.rejected.connect(self.close)

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            #self.dlg.labelID.setText("olA")
            pass



    def outputFile (self):
        self.file_name=str(QFileDialog.getSaveFileName(caption="Defining output file", filter="Terse RDF Triple Language(*.ttl)")[0])
        self.dlg.lineTTL.setText(self.file_name)

    def saveFile(self):

        saveAttrs = {}
        for row in range(self.dlg.tableAttributes.rowCount()): 
            check = self.dlg.tableAttributes.cellWidget(row, 0) 
            if check.isChecked():
                combo = self.dlg.tableAttributes.cellWidget(row, 1)
                class_attr = check.text()
                rdf = combo.currentText().split(":")
                namespace = namespaces[rdf[0]][0]
                rdf_attr = rdf[1]
                saveAttrs[class_attr] = rdf_attr
                setattr(Cell,class_attr, namespace[rdf_attr])
                #print(Cell,class_attr, rdf[0],  namespace, rdf_attr)
                

        layer = self.iface.activeLayer()

        if self.dlg.checkSelected.isChecked():
            features = layer.selectedFeatures() 
        else:
            features = layer.getFeatures()

        cells = []
        for feature in features:
            pol = QgsMultiPolygon()
            pol.fromWkt (feature.geometry().asWkt())
            cell = {
                "id": str(feature[self.dlg.comboID.currentText()])
            }
            if self.dlg.checkGeometries.isChecked():
                pol = QgsMultiPolygon()
                pol.fromWkt (feature.geometry().asWkt())
                cell['asWkt'] = pol.polygonN(0).asWkt()

            for key in saveAttrs:
                cell[key] = feature[key]

            cells.append (cell)
        fileName = self.dlg.lineTTL.text()
        self.iface.messageBar().pushMessage(
            "Success", "Output file written at " + fileName,
            level=Qgis.Success, duration=3
        )

        serialize_to_rdf_file(cells, Cell, fileName)
    
    def close(self):
        self.dlg.setVisible(False)

    def loadVocabulary(self, namespace, format, key):
        #namespace = "http://purl.org/ontology/dbcells/cells#"
        g = Graph()
        g.parse(str(namespace), format=format)
        q = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>

            SELECT ?p
            WHERE {
                ?p rdf:type owl:DatatypeProperty.
            }
        """

        # Apply the query to the graph and iterate through results
        for r in g.query(q):
            attr = r["p"].split("#") 
            name = key+":"+attr[1]
            self.vocabularies.append(name)
            #vs.append(key+":"+attr[1])
    

    def loadVocabularies(self):
        self.vocabularies = []
        for key, value in namespaces.items():
            self.loadVocabulary(value[0], value[1], key)
