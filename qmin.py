import pandas as pd
from pandas import groupby
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import opti
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
from bokeh.palettes import Inferno5
from bokeh.palettes import RdGy5

from bokeh.io import output_notebook
output_notebook()


  
res = pd.read_csv('Bookot.csv')
      

cluster = res.groupby('farmid')['Fendt','Kubota','Massey','Case','Deutz','JCB','Ford','Zetor','Corn_com_tractors_availability','Caterpillar_Kubota','Case_Kubota','Case_JCB','Massey_Fendt','JCB_Caterpillar','Fendt_Kubota','Massey_Deutz','Deutz_Kubota'].sum()	  

source = ColumnDataSource(cluster)
comm = source.data['farmid'].tolist()


TOOLS="hover,crosshair,pan,wheel_zoom,box_zoom,reset,tap,save,box_select,poly_select,lasso_select"

p = figure(x_range=comm, width=600, height=600, tools=TOOLS)

p.circle(x='farmid', y='Corn_com_tractors_availability',
         source=source,
         size=10, color='green')
		 
p.title.text = 'Optimization Solution'
p.xaxis.axis_label = 'Community Farms'
p.yaxis.axis_label = 'Int output'

hover = HoverTool()

hover.tooltips=[
             ('MachF', '@Fendt'), 
             ('MachK', '@Kubota'), 
             ('MachM', '@Massey'),  
             ('MachC', '@Case'),  
             ('MachD', '@Deutz'),  
             ('MachJ', '@JCB'), 
             ('MachO', '@Ford'), 
             ('MachZ', '@Zetor'), 
             ('exTractors', '@Corn_com_tractors_availability'), 
             ('Sch1', '@Caterpillar_Kubota'), 
             ('Sch2', '@Case_Kubota'), 
             ('Sch3', '@Case_JCB'),
             ('Sch4', '@Massey_Fendt'), 
             ('Sch5', '@JCB_Caterpillar'), 
             ('Sch6', '@Fendt_Kubota'), 
             ('Sch7', '@Massey_Deutz')
]


p.add_tools(hover)

show(p)