from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'electron_cutID_benchmark_TT_90X'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runElectrons_VID_CutBased_Summer16_80X_benchmark.py'

config.section_("Data")
config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/PhaseISpring17MiniAOD-FlatPU28to62_902_90X_upgrade2017_realistic_v20_ext1-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.publication = False
config.Data.ignoreLocality = False

config.section_("Site")
# Limit to US Tier2 sites. It appears to give more reliable performance.
#config.Site.whitelist = ['T2_US_MIT','T2_US_UCSD','T2_US_Florida','T2_US_Wisconsin','T2_US_Caltech','T2_US_Purdue']
config.Site.storageSite = 'T2_US_Nebraska'
