'''
/***************************************************************************
                                PYyQt Utilities
        
                             -------------------
    begin                : 2013-11-17
    copyright            : (C) 2013 by Walter Tsui
    email                : waltertech426@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import math


class QWidgetGrid(QWidget):
    def __init__(self, WidgetType, WidgetTypeName, WidgetArguSet, GridDirection = 0, MaxRowCnt = 0, MaxColCnt = 0):
        QWidget.__init__(self)
        
        if GridDirection > 1:
            return
        
        if MaxRowCnt == 0 and MaxColCnt == 0:
            return
            
        TblCnt = len(WidgetArguSet)
        
        if TblCnt <= 0:
            return
        
        
        if MaxRowCnt > 0 and MaxColCnt == 0:
            MaxColCnt = int(math.ceil(float(TblCnt)/float(MaxRowCnt)))
            
        elif MaxColCnt > 0 and MaxRowCnt == 0:
            MaxRowCnt = int(math.ceil(float(TblCnt)/float(MaxColCnt)))
                
        self.QGL = QGridLayout()
        

        tbl_idx = 0
        
        #From Top to Bottom, than Left to Right
        if GridDirection == 0:
            ColCnt = int(math.ceil(float(TblCnt)/float(MaxRowCnt)))
            
            for col_idx in range(0, ColCnt):
                RowCnt = MaxRowCnt

                if col_idx >= ColCnt - 1 and (TblCnt % MaxRowCnt) > 0:
                    RowCnt = TblCnt % MaxRowCnt
                
                for row_idx in range(0, RowCnt):
                    str_Widget_curr =  'self.' + WidgetTypeName + '_' + str(tbl_idx)
                    str_CreateWidget = str_Widget_curr + ' = ' + WidgetType + '('
                    
                    for k in range(0, len(WidgetArguSet[tbl_idx])):
                        str_CreateWidget += WidgetArguSet[tbl_idx][k] + ', '
                    
                    
                    str_CreateWidget = str_CreateWidget.rstrip(',') + ')'
                    exec(str_CreateWidget)     
                    exec('self.QGL.addWidget(' + str_Widget_curr + ', ' + str(row_idx) + ', ' + str(col_idx) + ')')
                    
                    tbl_idx += 1
        
        
        #From Left to Right, Top to Bottom
        elif GridDirection == 1:
            RowCnt = int(math.ceil(float(TblCnt)/float(MaxColCnt)))
            
            for row_idx in range(0, RowCnt):
                ColCnt = MaxColCnt

                if row_idx >= RowCnt - 1 and (TblCnt % MaxColCnt) > 0:
                    ColCnt = TblCnt % MaxColCnt
                
                for col_idx in range(0, ColCnt):
                    str_Widget_curr =  'self.' + WidgetTypeName + '_' + str(tbl_idx)
                    str_CreateWidget = str_Widget_curr + ' = ' + WidgetType + '('
                    
                    for k in range(0, len(WidgetArguSet[tbl_idx])):
                        str_CreateWidget += WidgetArguSet[tbl_idx][k] + ', '
                        
                        
                    str_CreateWidget = str_CreateWidget.rstrip(',') + ')'
                    exec(str_Widget_curr + ' = ' + WidgetType +'(' + str_CreateWidget + ')')     
                    exec('self.QGL.addWidget(' + str_Widget_curr + ', ' + str(row_idx) + ', ' + str(col_idx) + ')')
                    
                    tbl_idx += 1
        
        
        self.setLayout(self.QGL)
    
    def __del__(self):
        return