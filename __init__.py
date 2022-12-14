# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ExportDBCells
                                 A QGIS plugin
 exportar dados para o dbcells
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-11-19
        copyright            : (C) 2022 by Sergio Costa
        email                : sergio.costa@ufma.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ExportDBCells class from file ExportDBCells.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .export_dbcells import ExportDBCells
    return ExportDBCells(iface)
