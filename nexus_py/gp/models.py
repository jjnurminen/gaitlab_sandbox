# -*- coding: utf-8 -*-
"""

models.py - definitions for various models (PiG, muscle length, etc.)
Defines variable names, descriptions, etc.
For a new model, create a model() instance, fill in the data and append to
models_all.

@author: Jussi
"""

import config
import getpass

# needed to get normal data dirs from config
# TODO: hardcoded dirs, also in plot.py
pathprefix = 'c:/users/' + getpass.getuser()
desktop = pathprefix + '/Desktop'
appdir = desktop + '/GaitPlotter'
cfg = config.Config(appdir)
cfg.read()

models_all = []


class model:
    """ A class for storing model variable data, e.g. Plug-in Gait. """    

    def __init__(self):
        self.read_vars = list()  # vars to be read from data
        # How to read multidimensional variables: 'split_xyz' splits each 
        # variable into x,y,z components; or give a number to read the 
        # corresponding dimension only (e.g. 0=first dim)
        self.read_strategy = False
        self.desc = ''  # description of model
        self.varnames = list()   # resulting variable names
        self.varlabels = dict()  # descriptive label for each variable
        self.normaldata_map = dict()  # mapping from variable names to .gcd normaldata variables (optional)
        self.normaldata_path = None  # where to find normal data
        self.ylabels = dict()  # y axis labels for plotting the variables (optional)
        self.type = ''  # variable type, e.g. 'PiG'
        self.was_read = False  # whether physical model data was read for this instance

    # convenience methods for model creation

    def list_with_side(self, vars):
        """ Prepend variables in vars with 'L' and 'R', creating a new list of
        variables. Many model variables share the same name, except for leading
        'L' or 'R' that indicates side. """
        return ['L'+var for var in vars]+['R'+var for var in vars]

    def dict_with_side(self, dict, append_side=False):
        """ Prepend dict keys with 'R' or 'L'. If append_side,
        also append corresponding ' (R)' or ' (L)' to every dict value. """
        di = {}
        if append_side:
            Rstr, Lstr = (' (R)',' (L)')
        else:
            Rstr, Lstr = ('', '')
        for key in dict:
            di['R'+key] = dict[key]+Rstr
            di['L'+key] = dict[key]+Lstr
        return di
   
#
# Plug-in Gait lowerbody
#
pig_lowerbody = model()

pig_lowerbody.desc = 'Plug-in Gait lower body'

pig_lowerbody.type = 'PiG'

pig_lowerbody.read_strategy = 'split_xyz'

pig_lowerbody.read_vars = pig_lowerbody.list_with_side(['HipMoment',
      'KneeMoment',
      'AnkleMoment',
      'HipPower',
      'KneePower',
      'AnklePower',
      'HipAngles',
      'KneeAngles',
      'AbsAnkleAngle',
      'AnkleAngles',
      'PelvisAngles',
      'FootProgressAngles'])
      
pig_lowerbody.varlabels = pig_lowerbody.dict_with_side({'AnkleAnglesX': 'Ankle dorsi/plant',
                         'AnkleAnglesZ': 'Ankle rotation',
                         'AnkleMomentX': 'Ankle dors/plan moment',
                         'AnklePowerZ': 'Ankle power',
                         'FootProgressAnglesZ': 'Foot progress angles',
                         'HipAnglesX': 'Hip flexion',
                         'HipAnglesY': 'Hip adduction',
                         'HipAnglesZ': 'Hip rotation',
                         'HipMomentX': 'Hip flex/ext moment',
                         'HipMomentY': 'Hip ab/add moment',
                         'HipMomentZ': 'Hip rotation moment',
                         'HipPowerZ': 'Hip power',
                         'KneeAnglesX': 'Knee flexion',
                         'KneeAnglesY': 'Knee adduction',
                         'KneeAnglesZ': 'Knee rotation',
                         'KneeMomentX': 'Knee flex/ext moment',
                         'KneeMomentY': 'Knee ab/add moment',
                         'KneeMomentZ': 'Knee rotation moment',
                         'KneePowerZ': 'Knee power',
                         'PelvisAnglesX': 'Pelvic tilt',
                         'PelvisAnglesY': 'Pelvic obliquity',
                         'PelvisAnglesZ': 'Pelvic rotation'}, append_side=False)

pig_lowerbody.varnames = pig_lowerbody.varlabels.keys()
      
pig_lowerbody.normaldata_map = pig_lowerbody.dict_with_side({'AnkleAnglesX': 'DorsiPlanFlex',
             'AnkleAnglesZ': 'FootRotation',
             'AnkleMomentX': 'DorsiPlanFlexMoment',
             'AnklePowerZ': 'AnklePower',
             'FootProgressAnglesZ': 'FootProgression',
             'HipAnglesX': 'HipFlexExt',
             'HipAnglesY': 'HipAbAdduct',
             'HipAnglesZ': 'HipRotation',
             'HipMomentX': 'HipFlexExtMoment',
             'HipMomentY': 'HipAbAdductMoment',
             'HipMomentZ': 'HipRotationMoment',
             'HipPowerZ': 'HipPower',
             'KneeAnglesX': 'KneeFlexExt',
             'KneeAnglesY': 'KneeValgVar',
             'KneeAnglesZ': 'KneeRotation',
             'KneeMomentX': 'KneeFlexExtMoment',
             'KneeMomentY': 'KneeValgVarMoment',
             'KneeMomentZ': 'KneeRotationMoment',
             'KneePowerZ': 'KneePower',
             'PelvisAnglesX': 'PelvicTilt',
             'PelvisAnglesY': 'PelvicObliquity',
             'PelvisAnglesZ': 'PelvicRotation'})

pig_lowerbody.ylabels = pig_lowerbody.dict_with_side({'AnkleAnglesX': 'Pla     ($^\\circ$)      Dor',
                         'AnkleAnglesZ': 'Ext     ($^\\circ$)      Int',
                         'AnkleMomentX': 'Int dors    Nm/kg    Int plan',
                         'AnklePowerZ': 'Abs    W/kg    Gen',
                         'FootProgressAnglesZ': 'Ext     ($^\\circ$)      Int',
                         'HipAnglesX': 'Ext     ($^\\circ$)      Flex',
                         'HipAnglesY': 'Abd     ($^\\circ$)      Add',
                         'HipAnglesZ': 'Ext     ($^\\circ$)      Int',
                         'HipMomentX': 'Int flex    Nm/kg    Int ext',
                         'HipMomentY': 'Int add    Nm/kg    Int abd',
                         'HipMomentZ': 'Int flex    Nm/kg    Int ext',
                         'HipPowerZ': 'Abs    W/kg    Gen',
                         'KneeAnglesX': 'Ext     ($^\\circ$)      Flex',
                         'KneeAnglesY': 'Val     ($^\\circ$)      Var',
                         'KneeAnglesZ': 'Ext     ($^\\circ$)      Int',
                         'KneeMomentX': 'Int flex    Nm/kg    Int ext',
                         'KneeMomentY': 'Int var    Nm/kg    Int valg',
                         'KneeMomentZ': 'Int flex    Nm/kg    Int ext',
                         'KneePowerZ': 'Abs    W/kg    Gen',
                         'PelvisAnglesX': 'Pst     ($^\\circ$)      Ant',
                         'PelvisAnglesY': 'Dwn     ($^\\circ$)      Up',
                         'PelvisAnglesZ': 'Bak     ($^\\circ$)      For'})


pig_lowerbody.normaldata_path = cfg.getval('pig_normaldata_path')

models_all.append(pig_lowerbody)

#
# Muscle length (MuscleLength.mod)
#

musclelen = model()

musclelen.desc = 'Muscle length (MuscleLength.mod)'

musclelen.type = 'musclelen'

musclelen.read_strategy = 0

musclelen.varlabels = musclelen.dict_with_side({'AdBrLength': 'AdBrLength',
                       'AdLoLength': 'AdLoLength',
                        'AdMaInfLength': 'AdMaInfLength',
                        'AdMaMidLength': 'AdMaMidLength',
                        'AdMaSupLength': 'AdMaSupLength',
                        'BiFLLength': 'Biceps femoris length',
                        'BiFSLength': 'BiFSLength',
                        'ExDLLength': 'ExDLLength',
                        'ExHLLength': 'ExHLLength',
                        'FlDLLength': 'FlDLLength',
                        'FlHLLength': 'FlHLLength',
                        'GMedAntLength': 'GMedAntLength',
                        'GMedMidLength': 'GMedMidLength',
                        'GMedPosLength': 'GMedPosLength',
                        'GMinAntLength': 'GMinAntLength',
                        'GMinMidLength': 'GMinMidLength',
                        'GMinPosLength': 'GMinPosLength',
                        'GemeLength': 'GemeLength',
                        'GlMaInfLength': 'GlMaInfLength',
                        'GlMaMidLength': 'GlMaMidLength',
                        'GlMaSupLength': 'GlMaSupLength',
                        'GracLength': 'Gracilis length',
                        'IliaLength': 'IliaLength',
                        'LaGaLength': 'Lateral gastrocnemius length',
                        'MeGaLength': 'Medial gastrocnemius length',
                        'PELOLength': 'PELOLength',
                        'PeBrLength': 'PeBrLength',
                        'PeTeLength': 'PeTeLength',
                        'PectLength': 'PectLength',
                        'PeriLength': 'PeriLength',
                        'PsoaLength': 'Psoas length',
                        'QuFeLength': 'QuFeLength',
                        'ReFeLength': 'Rectus femoris length',
                        'SartLength': 'SartLength',
                        'SeMeLength': 'Semimembranosus length',
                        'SeTeLength': 'Semitendinosus length',
                        'SoleLength': 'Soleus length',
                        'TiAnLength': 'Tibialis anterior length',
                        'TiPoLength': 'TiPoLength',
                        'VaInLength': 'VaInLength',
                        'VaLaLength': 'VaLaLength',
                        'VaMeLength': 'VaMeLength'}, append_side=False)

musclelen.read_vars = musclelen.varlabels.keys()

musclelen.varnames = musclelen.read_vars

musclelen.ylabels = {}
for var in musclelen.varnames:
    musclelen.ylabels[var] = 'Length (mm)'

models_all.append(musclelen)
                        

