" ATP project vim script: Fri Jun 27, 2014 at 02:01 PM +1200.

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
let b:atp_Viewer = 'okular'
let b:TreeOfFiles = {'content/appendices/microprocessorPowerMeasurements/appendix.tex': [{}, 90], 'content/acknowledgement.tex': [{}, 21], 'content/introduction/01-LiquidsAtScale/chapter.tex': [{}, 27], 'content/pt1/02-Microcontrollers/chapter.tex': [{}, 68], 'content/appendices/streamingCellMeasurements/appendix.tex': [{}, 92], 'content/pt1/02-WirelessWaterMeter/chapter.tex': [{}, 62], 'content/pt1/04-HarvesterDesign/chapter.tex': [{}, 75], 'content/pt2/01-ElectricalModelling/chapter.tex': [{}, 80], 'content/pt1/01-PowerHarvesting/chapter.tex': [{}, 54], 'content/abstract.tex': [{}, 17], 'content/appendices/chargedWaterDrops/appendix.tex': [{}, 88], 'content/introduction/02-TheDoubleLayer/chapter.tex': [{}, 29], 'frontmatter.tex': [{}, 7], 'content/pt2/02-InterfaceParameters/chapter.tex': [{}, 82], 'content/pt1/03-DataTransmission/chapter.tex': [{}, 71]}
let b:ListOfFiles = ['configuration.tex', 'frontmatter.tex', 'content/abstract.tex', 'content/acknowledgement.tex', 'content/introduction/01-LiquidsAtScale/chapter.tex', 'content/introduction/02-TheDoubleLayer/chapter.tex', 'content/pt1/01-PowerHarvesting/chapter.tex', 'content/pt1/02-WirelessWaterMeter/chapter.tex', 'content/pt1/02-Microcontrollers/chapter.tex', 'content/pt1/03-DataTransmission/chapter.tex', 'content/pt1/04-HarvesterDesign/chapter.tex', 'content/pt2/01-ElectricalModelling/chapter.tex', 'content/pt2/02-InterfaceParameters/chapter.tex', 'content/appendices/chargedWaterDrops/appendix.tex', 'content/appendices/microprocessorPowerMeasurements/appendix.tex', 'content/appendices/streamingCellMeasurements/appendix.tex', 'bibliography.bib']
let b:TypeDict = {'configuration.tex': 'preambule', 'content/appendices/microprocessorPowerMeasurements/appendix.tex': 'input', 'content/acknowledgement.tex': 'input', 'content/introduction/01-LiquidsAtScale/chapter.tex': 'input', 'bibliography.bib': 'bib', 'content/pt1/02-Microcontrollers/chapter.tex': 'input', 'content/appendices/streamingCellMeasurements/appendix.tex': 'input', 'content/pt1/02-WirelessWaterMeter/chapter.tex': 'input', 'content/pt1/04-HarvesterDesign/chapter.tex': 'input', 'content/pt2/01-ElectricalModelling/chapter.tex': 'input', 'content/pt1/01-PowerHarvesting/chapter.tex': 'input', 'content/abstract.tex': 'input', 'content/appendices/chargedWaterDrops/appendix.tex': 'input', 'content/introduction/02-TheDoubleLayer/chapter.tex': 'input', 'frontmatter.tex': 'input', 'content/pt2/02-InterfaceParameters/chapter.tex': 'input', 'content/pt1/03-DataTransmission/chapter.tex': 'input'}
let b:LevelDict = {'configuration.tex': 1, 'content/appendices/microprocessorPowerMeasurements/appendix.tex': 1, 'content/acknowledgement.tex': 1, 'content/introduction/01-LiquidsAtScale/chapter.tex': 1, 'bibliography.bib': 1, 'content/pt1/02-Microcontrollers/chapter.tex': 1, 'content/appendices/streamingCellMeasurements/appendix.tex': 1, 'content/pt1/02-WirelessWaterMeter/chapter.tex': 1, 'content/pt1/04-HarvesterDesign/chapter.tex': 1, 'content/pt2/01-ElectricalModelling/chapter.tex': 1, 'content/pt1/01-PowerHarvesting/chapter.tex': 1, 'content/abstract.tex': 1, 'content/appendices/chargedWaterDrops/appendix.tex': 1, 'content/introduction/02-TheDoubleLayer/chapter.tex': 1, 'frontmatter.tex': 1, 'content/pt2/02-InterfaceParameters/chapter.tex': 1, 'content/pt1/03-DataTransmission/chapter.tex': 1}
let b:atp_BibCompiler = 'bibtex'
let b:atp_StarEnvDefault = ''
let b:atp_StarMathEnvDefault = ''
let b:atp_updatetime_insert = 4000
let b:atp_updatetime_normal = 2000
let b:atp_LocalCommands = []
let b:atp_LocalEnvironments = []
let b:atp_LocalColors = ['chaptergrey', 'dark']
