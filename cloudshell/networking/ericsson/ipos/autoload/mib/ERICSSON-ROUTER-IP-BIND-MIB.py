#
# PySNMP MIB module ERICSSON-ROUTER-IP-BIND-MIB (http://pysnmp.sf.net)
# ASN.1 source file://\usr\share\snmp\ERICSSON-ROUTER-IP-BIND-MIB.my
# Produced by pysmi-0.0.6 at Wed Aug 03 17:53:30 2016
# On host ? platform ? version ? by user ?
# Using Python version 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)]
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( eriRouterMgmt, ) = mibBuilder.importSymbols("ERICSSON-ROUTER-SMI", "eriRouterMgmt")
( EriRouterCircuitHandle, ) = mibBuilder.importSymbols("ERICSSON-ROUTER-TC", "EriRouterCircuitHandle")
( ifIndex, InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eriRouterIpBindMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 218, 2, 26)).setRevisions(("2015-01-14 18:00", "2011-01-19 18:00", "2002-08-20 12:00",))
eriRouterIpBindMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 0))
eriRouterIpBindMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 1))
eriRouterIpBindMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 2))
eriRouterIpBindTable = MibTable((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 1, 1), )
eriRouterIpBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ERICSSON-ROUTER-IP-BIND-MIB", "eriRouterIpBindCircuitHandle"))
eriRouterIpBindCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 1, 1, 1, 1), EriRouterCircuitHandle())
eriRouterIpBindIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
eriRouterIpBindHierarchicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 1, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
eriRouterIpBindCircuitDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,192))).setMaxAccess("readonly")
eriRouterIpBindContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,63))).setMaxAccess("readonly")
eriRouterIpBindCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 2, 1))
eriRouterIpBindGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 2, 2))
eriRouterIpBindCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 2, 1, 1)).setObjects(*(("ERICSSON-ROUTER-IP-BIND-MIB", "eriRouterIpBindDisplayGroup"),))
eriRouterIpBindDisplayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 218, 2, 26, 2, 2, 1)).setObjects(*(("ERICSSON-ROUTER-IP-BIND-MIB", "eriRouterIpBindIfIndex"), ("ERICSSON-ROUTER-IP-BIND-MIB", "eriRouterIpBindHierarchicalIfIndex"), ("ERICSSON-ROUTER-IP-BIND-MIB", "eriRouterIpBindCircuitDescr"), ("ERICSSON-ROUTER-IP-BIND-MIB", "eriRouterIpBindContextName"),))
mibBuilder.exportSymbols("ERICSSON-ROUTER-IP-BIND-MIB", eriRouterIpBindMibConformance=eriRouterIpBindMibConformance, eriRouterIpBindDisplayGroup=eriRouterIpBindDisplayGroup, eriRouterIpBindTable=eriRouterIpBindTable, eriRouterIpBindGroups=eriRouterIpBindGroups, PYSNMP_MODULE_ID=eriRouterIpBindMib, eriRouterIpBindMibNotifications=eriRouterIpBindMibNotifications, eriRouterIpBindIfIndex=eriRouterIpBindIfIndex, eriRouterIpBindMibObjects=eriRouterIpBindMibObjects, eriRouterIpBindContextName=eriRouterIpBindContextName, eriRouterIpBindMib=eriRouterIpBindMib, eriRouterIpBindCircuitDescr=eriRouterIpBindCircuitDescr, eriRouterIpBindCompliances=eriRouterIpBindCompliances, eriRouterIpBindEntry=eriRouterIpBindEntry, eriRouterIpBindCircuitHandle=eriRouterIpBindCircuitHandle, eriRouterIpBindCompliance=eriRouterIpBindCompliance, eriRouterIpBindHierarchicalIfIndex=eriRouterIpBindHierarchicalIfIndex)
