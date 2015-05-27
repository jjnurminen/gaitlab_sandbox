# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:37:51 2015

Plot PiG outputs (online) from Nexus.

@author: Jussi
"""


from nexus_plot import nexus_plotter

layout = [4,3]

plotvars = ['PelvisAnglesX',
           'PelvisAnglesY',
           'PelvisAnglesZ',
           'HipAnglesX',
           'HipAnglesY',
           'HipAnglesZ',
           'KneeAnglesX',
           'KneeAnglesY',
           'KneeAnglesZ',
           'AnkleAnglesX',
           'FootProgressAnglesZ',
           'AnkleAnglesZ']
maintitleprefix = 'Kinematics plot for '

nplotter = nexus_plotter(layout)
nplotter.open_trial(plotvars)
nplotter.plot_trial(maintitleprefix=maintitleprefix)

plotvars = ['HipMomentX',
            'HipMomentY',
             'HipMomentZ',
             'HipPowerZ',
             'KneeMomentX',
             'KneeMomentY',
             'KneeMomentZ',
             'KneePowerZ',
             'AnkleMomentX',None,None,
             'AnklePowerZ']                      
maintitleprefix = 'Kinetics plot for '

nplotter = nexus_plotter(layout)
nplotter.open_trial(plotvars)
nplotter.plot_trial(maintitleprefix=maintitleprefix)

nplotter.show()
    
   
