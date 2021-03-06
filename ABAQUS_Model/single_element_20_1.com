from driverConstants import *
from driverExplicit import ExplicitAnalysis
import driverUtils, sys
options = {
    'ams':OFF,
    'analysisType':EXPLICIT,
    'applicationName':'analysis',
    'aqua':OFF,
    'ask_delete':OFF,
    'beamSectGen':OFF,
    'biorid':OFF,
    'cavityTypes':[],
    'cavparallel':OFF,
    'complexFrequency':OFF,
    'contact':OFF,
    'cosimulation':OFF,
    'coupledProcedure':OFF,
    'cpus':1,
    'cse':OFF,
    'cyclicSymmetryModel':OFF,
    'directCyclic':OFF,
    'domains':1,
    'dsa':OFF,
    'dynamic':OFF,
    'enrichment':OFF,
    'filPrt':[],
    'fils':[],
    'finitesliding':OFF,
    'foundation':OFF,
    'geostatic':OFF,
    'heatTransfer':OFF,
    'importer':OFF,
    'importerParts':OFF,
    'includes':[],
    'initialConditionsFile':OFF,
    'input':'single_element_20_1',
    'inputFormat':INP,
    'interactive':None,
    'job':'single_element_20_1',
    'keyword_licenses':[],
    'lanczos':OFF,
    'libs':[],
    'magnetostatic':OFF,
    'massDiffusion':OFF,
    'memory':'90%',
    'modifiedTet':OFF,
    'moldflowFiles':[],
    'moldflowMaterial':OFF,
    'mp_mode':THREADS,
    'multiphysics':OFF,
    'noDmpDirect':[],
    'noGUI':None,
    'noMultiHost':[],
    'noMultiHostElemLoop':[],
    'noStdParallel':[],
    'no_domain_check':1,
    'outputKeywords':ON,
    'parallel':DOMAIN,
    'parallel_odb':SINGLE,
    'parameterized':ON,
    'partsAndAssemblies':ON,
    'parval':OFF,
    'postOutput':OFF,
    'preDecomposition':OFF,
    'restart':OFF,
    'restartEndStep':OFF,
    'restartIncrement':0,
    'restartStep':0,
    'restartWrite':ON,
    'rezone':OFF,
    'runCalculator':OFF,
    'soils':OFF,
    'soliter':OFF,
    'solverTypes':['DIRECT'],
    'staticNonlinear':OFF,
    'steadyStateTransport':OFF,
    'step':ON,
    'subGen':OFF,
    'subGenLibs':[],
    'subGenTypes':[],
    'submodel':OFF,
    'substrLibDefs':OFF,
    'substructure':OFF,
    'symmetricModelGeneration':OFF,
    'thermal':OFF,
    'tmpdir':'C:\\Users\\gkim68\\AppData\\Local\\Temp',
    'tracer':OFF,
    'usub_lib_dir':'C:\\Users\\gkim68\\PycharmProjects\\PythonScripts\\SummerInternship2018\\ABAQUS_Model\\newlib',
    'visco':OFF,
}
analysis = ExplicitAnalysis(options)
status = analysis.run()
sys.exit(status)
