" ATP project vim script: Tue Feb 17, 2015 at 04:05 PM +1300.

let b:atp_MainFile = 'thesis.tex'
let g:atp_mapNn = 0
let b:atp_autex = 1
let b:atp_TexCompiler = 'pdflatex'
let b:atp_TexOptions = '-synctex=1'
let b:atp_TexFlavor = 'tex'
let b:atp_auruns = '1'
let b:atp_ReloadOnError = '1'
let b:atp_OutDir = '/home/mark/repos/thesis'
let b:atp_OpenViewer = '1'
let b:atp_XpdfServer = 'thesis'
let b:atp_Viewer = 'evince'
let b:TreeOfFiles = {'content/appendices/chargedWaterDrops/appendix.tex': [{}, 163], 'content/pt2/interfaceParameters.tex': [{}, 152], 'content/pt1/03-DataTransmission/chapter-DataTransmission.tex': [{}, 132], 'content/pt2/recipes.tex': [{}, 156], 'content/pt1/02-WirelessWaterMeter/chapter-WirelessWaterMeter.tex': [{}, 123], 'content/pt2/modelling.tex': [{}, 149], 'content/introduction/introduction.tex': [{}, 80], 'content/appendices/microprocessorPowerMeasurements/appendix.tex': [{}, 165], 'content/pt1/introduction.tex': [{}, 104], 'frontmatter.tex': [{}, 8], 'content/pt1/01-PowerHarvesting/chapter-PowerHarvesting.tex': [{}, 113], 'content/appendices/Solution-Impedance-Measurements/appendix_mimicry.tex': [{}, 167]}
let b:ListOfFiles = ['configuration.tex', 'frontmatter.tex', 'content/introduction/introduction.tex', 'content/pt1/introduction.tex', 'content/pt1/01-PowerHarvesting/chapter-PowerHarvesting.tex', 'content/pt1/02-WirelessWaterMeter/chapter-WirelessWaterMeter.tex', 'content/pt1/03-DataTransmission/chapter-DataTransmission.tex', 'content/pt2/modelling.tex', 'content/pt2/interfaceParameters.tex', 'content/pt2/recipes.tex', 'content/appendices/chargedWaterDrops/appendix.tex', 'content/appendices/microprocessorPowerMeasurements/appendix.tex', 'content/appendices/Solution-Impedance-Measurements/appendix_mimicry.tex', 'library.bib']
let b:TypeDict = {'library.bib': 'bib', 'content/appendices/chargedWaterDrops/appendix.tex': 'input', 'content/pt2/interfaceParameters.tex': 'input', 'content/pt2/modelling.tex': 'input', 'content/pt1/03-DataTransmission/chapter-DataTransmission.tex': 'input', 'content/pt2/recipes.tex': 'input', 'content/pt1/introduction.tex': 'input', 'content/introduction/introduction.tex': 'input', 'content/appendices/microprocessorPowerMeasurements/appendix.tex': 'input', 'configuration.tex': 'preambule', 'frontmatter.tex': 'input', 'content/pt1/02-WirelessWaterMeter/chapter-WirelessWaterMeter.tex': 'input', 'content/pt1/01-PowerHarvesting/chapter-PowerHarvesting.tex': 'input', 'content/appendices/Solution-Impedance-Measurements/appendix_mimicry.tex': 'input'}
let b:LevelDict = {'library.bib': 1, 'content/appendices/chargedWaterDrops/appendix.tex': 1, 'content/pt2/interfaceParameters.tex': 1, 'content/pt2/modelling.tex': 1, 'content/pt1/03-DataTransmission/chapter-DataTransmission.tex': 1, 'content/pt2/recipes.tex': 1, 'content/pt1/introduction.tex': 1, 'content/introduction/introduction.tex': 1, 'content/appendices/microprocessorPowerMeasurements/appendix.tex': 1, 'configuration.tex': 1, 'frontmatter.tex': 1, 'content/pt1/02-WirelessWaterMeter/chapter-WirelessWaterMeter.tex': 1, 'content/pt1/01-PowerHarvesting/chapter-PowerHarvesting.tex': 1, 'content/appendices/Solution-Impedance-Measurements/appendix_mimicry.tex': 1}
let b:atp_BibCompiler = 'bibtex'
let b:atp_StarEnvDefault = ''
let b:atp_StarMathEnvDefault = ''
let b:atp_updatetime_insert = 4000
let b:atp_updatetime_normal = 2000
let b:atp_LocalCommands = []
let b:atp_LocalEnvironments = []
let b:atp_LocalColors = ['chaptergrey', 'dark']
