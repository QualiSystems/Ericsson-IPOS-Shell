#
# PySNMP MIB module ERICSSON-ROUTER-SMI (http://pysnmp.sf.net)
# ASN.1 source file://\usr\share\snmp\ERICSSON-ROUTER-SMI.my
# Produced by pysmi-0.0.6 at Tue Aug 02 15:20:36 2016
# On host ? platform ? version ? by user ?
# Using Python version 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)]
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ericsson, ) = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericsson")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eriRouterSMI = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 218)).setRevisions(("2015-01-14 18:00", "2011-01-19 18:00", "2002-06-06 00:00", "2001-06-27 00:00", "1998-04-18 23:00",))
eriRouterProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1))
eriRouterMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 2))
eriRouterExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 3))
eriRouterCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 4))
eriRouterModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 5))
eriRouterEntities = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6))
eriRouterInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 7))
mibBuilder.exportSymbols("ERICSSON-ROUTER-SMI", eriRouterMgmt=eriRouterMgmt, eriRouterSMI=eriRouterSMI, eriRouterEntities=eriRouterEntities, eriRouterExperiment=eriRouterExperiment, eriRouterProducts=eriRouterProducts, eriRouterCapabilities=eriRouterCapabilities, PYSNMP_MODULE_ID=eriRouterSMI, eriRouterModules=eriRouterModules, eriRouterInternal=eriRouterInternal)
