__author__ = 'geoffroy'

from pymatgen.core.structure import Structure
from pymatgen.core.periodic_table import Element
from pycdcd.core.defectsmaker import ChargedDefectsStructures
from pycdcd.utils.vasp import make_vasp_defect_files
import json


def example_maker():
        struct=Structure.from_dict(json.loads(open("PbTiO3.json",'r').read()))
        print struct.formula
        print dir(struct.composition)
        #print struct
        make_vasp_defect_files(ChargedDefectsStructures(struct,
            max_min_oxi={'Pb':(0,2),'Ti':(0,4),'O':(-2,0),'Al':(3,4),'V':(3,4),
                "Cr":(3,4),'Ga':(3,4),'Fe':(3,4),'Co':(3,4),'Ni':(3,4),
                'K':(1,2),'Na':(1,2),"N":(-3,-2)},
            substitutions={'Pb':['Na','K'],
                'Ti':['Al','V','Cr','Ga','Fe','Co','Ni'],'O':['N']}, 
            oxi_states={'Pb':2,'Ti':4,'O':-2}).defects, 
            struct.composition.reduced_formula)

if __name__ == '__main__':
    example_maker()