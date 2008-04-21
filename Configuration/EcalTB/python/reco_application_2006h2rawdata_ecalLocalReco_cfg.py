import FWCore.ParameterSet.Config as cms

process = cms.Process("RECO")
process.load("RecoTBCalo.EcalTBTDCReconstructor.ecal2006TBH2TDCReconstructor_cfi")

process.load("Configuration.EcalTB.readConfigurationH2_2006_v0_cff")

process.load("RecoTBCalo.EcalTBRecProducers.ecal2006TBH2WeightUncalibRecHit_cfi")

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO'),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(10000)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(20)
        ),
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10)
        ),
        DDLParser = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    ),
    categories = cms.untracked.vstring('DDLParser', 
        'FwkJob', 
        'FwkReport'),
    destinations = cms.untracked.vstring('cout')
)

process.source = cms.Source("PoolSource",
    maxEvents = cms.untracked.int32(1000),
    fileNames = cms.untracked.vstring('file:/u1/meridian/data/h2/2006/h2.00028833.combined.OutServ_0.0.root')
)

process.tbunpacker = cms.EDFilter("HcalTBObjectUnpacker",
    IncludeUnmatchedHits = cms.untracked.bool(False),
    HcalTDCFED = cms.untracked.int32(8),
    HcalSourcePosFED = cms.untracked.int32(-1),
    HcalTriggerFED = cms.untracked.int32(1),
    HcalQADCFED = cms.untracked.int32(8),
    HcalSlowDataFED = cms.untracked.int32(-1),
    ConfigurationFile = cms.untracked.string('configQADCTDC.txt')
)

process.ecalTBunpack = cms.EDFilter("EcalRawToDigi",
    FEDs = cms.untracked.vint32(9),
    DCCMapFile = cms.untracked.string('EventFilter/EcalRawToDigi/data/DCCMap_h2.txt'),
    EcalFirstFED = cms.untracked.int32(8)
)

process.reco-pool-out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *', 
        'drop FEDRawDataCollection_*_*_*'),
    fileName = cms.untracked.string('h2.ecalReco.root')
)

process.p = cms.Path(process.getCond*process.tbunpacker*process.ecalTBunpack*process.ecal2006TBH2TDCReconstructor*process.ecal2006TBH2WeightUncalibRecHit)
process.ep = cms.EndPath(process.reco-pool-out)

