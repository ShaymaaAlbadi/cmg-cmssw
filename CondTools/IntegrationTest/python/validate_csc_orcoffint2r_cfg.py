# The following comments couldn't be translated into the new config version:

# Configuration file for EventSetupTest_t

import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.PoolDBESSource = cms.ESSource("PoolDBESSource",
    loadAll = cms.bool(True),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('CSCPedestalsRcd'),
        tag = cms.string('CSCPedestals_from_online')
    ), 
        cms.PSet(
            record = cms.string('CSCGainsRcd'),
            tag = cms.string('CSCGains_from_online')
        ), 
        cms.PSet(
            record = cms.string('CSCNoiseMatrixRcd'),
            tag = cms.string('CSCNoiseMatrix_from_online')
        ), 
        cms.PSet(
            record = cms.string('CSCcrosstalkRcd'),
            tag = cms.string('CSCcrosstalk_from_online')
        )),
    messagelevel = cms.untracked.uint32(2),
    catalog = cms.untracked.string('relationalcatalog_oracle://cms_orcoff_int2r/CMS_COND_GENERAL'), ##cms_orcoff_int2r/CMS_COND_GENERAL"

    timetype = cms.string('runnumber'),
    connect = cms.string('oracle://cms_orcoff_int2r/CMS_COND_CSC'), ##cms_orcoff_int2r/CMS_COND_CSC"

    authenticationMethod = cms.untracked.uint32(1)
)

process.source = cms.Source("EmptySource",
    maxEvents = cms.untracked.int32(5),
    numberEventsInRun = cms.untracked.uint32(1),
    firstRun = cms.untracked.uint32(1)
)

process.get = cms.EDFilter("EventSetupRecordDataGetter",
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('CSCPedestalsRcd'),
        data = cms.vstring('CSCPedestals')
    ), 
        cms.PSet(
            record = cms.string('CSCGainsRcd'),
            data = cms.vstring('CSCGains')
        ), 
        cms.PSet(
            record = cms.string('CSCNoiseMatrixRcd'),
            data = cms.vstring('CSCNoiseMatrix')
        ), 
        cms.PSet(
            record = cms.string('CSCcrosstalkRcd'),
            data = cms.vstring('CSCcrosstalk')
        )),
    verbose = cms.untracked.bool(True)
)

process.print = cms.OutputModule("AsciiOutputModule")

process.p = cms.Path(process.get)
process.ep = cms.EndPath(process.print)

