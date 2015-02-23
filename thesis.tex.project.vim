" ATP project vim script: Fri Feb 20, 2015 at 04:40 PM +1300.

let b:atp_MainFile = 'thesis.tex'
let g:atp_mapNn = 0
let b:atp_autex = 0
let b:atp_TexCompiler = 'pdflatex'
let b:atp_TexOptions = '-synctex=1'
let b:atp_TexFlavor = 'tex'
let b:atp_auruns = '1'
let b:atp_ReloadOnError = '1'
let b:atp_OutDir = '/home/mark/repos/thesis'
let b:atp_OpenViewer = '1'
let b:atp_XpdfServer = 'thesis'
let b:atp_Viewer = 'okular'
let b:TreeOfFiles = {'content/appendices/chargedWaterDrops/appendix.tex': [{}, 155], 'content/pt1/03-EnergyRequirements/chapter-EnergyRequirements.tex': [{}, 118], 'content/pt2/interfaceParameters.tex': [{}, 144], 'content/pt2/recipes.tex': [{}, 148], 'content/pt2/modelling.tex': [{}, 141], 'content/introduction/introduction.tex': [{}, 83], 'content/appendices/microprocessorPowerMeasurements/appendix.tex': [{}, 157], 'content/pt1/introduction.tex': [{}, 106], 'content/pt1/01-PowerHarvesting/chapter-PowerHarvesting.tex': [{}, 110], 'frontmatter.tex': [{}, 8], 'content/appendices/Solution-Impedance-Measurements/appendix_mimicry.tex': [{}, 159], 'content/pt1/02-WirelessWaterMeter/chapter-WirelessWaterMeter.tex': [{}, 114]}
let b:ListOfFiles = ['configuration.tex', 'frontmatter.tex', 'content/introduction/introduction.tex', 'content/pt1/introduction.tex', 'content/pt1/01-PowerHarvesting/chapter-PowerHarvesting.tex', 'content/pt1/02-WirelessWaterMeter/chapter-WirelessWaterMeter.tex', 'content/pt1/03-EnergyRequirements/chapter-EnergyRequirements.tex', 'content/pt2/modelling.tex', 'content/pt2/interfaceParameters.tex', 'content/pt2/recipes.tex', 'content/appendices/chargedWaterDrops/appendix.tex', 'content/appendices/microprocessorPowerMeasurements/appendix.tex', 'content/appendices/Solution-Impedance-Measurements/appendix_mimicry.tex', 'library.bib']
let b:TypeDict = {'library.bib': 'bib', 'content/pt2/modelling.tex': 'input', 'content/pt2/interfaceParameters.tex': 'input', 'content/appendices/chargedWaterDrops/appendix.tex': 'input', 'content/pt2/recipes.tex': 'input', 'configuration.tex': 'preambule', 'content/pt1/03-EnergyRequirements/chapter-EnergyRequirements.tex': 'input', 'content/appendices/microprocessorPowerMeasurements/appendix.tex': 'input', 'content/appendices/Solution-Impedance-Measurements/appendix_mimicry.tex': 'input', 'content/pt1/introduction.tex': 'input', 'frontmatter.tex': 'input', 'content/introduction/introduction.tex': 'input', 'content/pt1/01-PowerHarvesting/chapter-PowerHarvesting.tex': 'input', 'content/pt1/02-WirelessWaterMeter/chapter-WirelessWaterMeter.tex': 'input'}
let b:LevelDict = {'library.bib': 1, 'content/pt2/modelling.tex': 1, 'content/pt2/interfaceParameters.tex': 1, 'content/appendices/chargedWaterDrops/appendix.tex': 1, 'content/pt2/recipes.tex': 1, 'configuration.tex': 1, 'content/pt1/03-EnergyRequirements/chapter-EnergyRequirements.tex': 1, 'content/appendices/microprocessorPowerMeasurements/appendix.tex': 1, 'content/appendices/Solution-Impedance-Measurements/appendix_mimicry.tex': 1, 'content/pt1/introduction.tex': 1, 'frontmatter.tex': 1, 'content/introduction/introduction.tex': 1, 'content/pt1/01-PowerHarvesting/chapter-PowerHarvesting.tex': 1, 'content/pt1/02-WirelessWaterMeter/chapter-WirelessWaterMeter.tex': 1}
let b:atp_BibCompiler = 'bibtex'
let b:atp_StarEnvDefault = ''
let b:atp_StarMathEnvDefault = ''
let b:atp_updatetime_insert = 4000
let b:atp_updatetime_normal = 2000
let b:atp_LocalCommands = []
let b:atp_LocalEnvironments = []
let b:atp_LocalColors = ['chaptergrey', 'dark']
