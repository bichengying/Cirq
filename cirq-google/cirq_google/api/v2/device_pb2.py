# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cirq_google/api/v2/device.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63irq_google/api/v2/device.proto\x12\x12\x63irq.google.api.v2\"\xfa\x01\n\x13\x44\x65viceSpecification\x12\x38\n\x0fvalid_gate_sets\x18\x01 \x03(\x0b\x32\x1b.cirq.google.api.v2.GateSetB\x02\x18\x01\x12:\n\x0bvalid_gates\x18\x05 \x03(\x0b\x32%.cirq.google.api.v2.GateSpecification\x12\x14\n\x0cvalid_qubits\x18\x02 \x03(\t\x12\x34\n\rvalid_targets\x18\x03 \x03(\x0b\x32\x1d.cirq.google.api.v2.TargetSet\x12!\n\x19\x64\x65veloper_recommendations\x18\x04 \x01(\t\"\xc2\x07\n\x11GateSpecification\x12\x1b\n\x13gate_duration_picos\x18\x01 \x01(\x03\x12=\n\x03syc\x18\x02 \x01(\x0b\x32..cirq.google.api.v2.GateSpecification.SycamoreH\x00\x12\x45\n\nsqrt_iswap\x18\x03 \x01(\x0b\x32/.cirq.google.api.v2.GateSpecification.SqrtISwapH\x00\x12L\n\x0esqrt_iswap_inv\x18\x04 \x01(\x0b\x32\x32.cirq.google.api.v2.GateSpecification.SqrtISwapInvH\x00\x12\x36\n\x02\x63z\x18\x05 \x01(\x0b\x32(.cirq.google.api.v2.GateSpecification.CZH\x00\x12\x43\n\tphased_xz\x18\x06 \x01(\x0b\x32..cirq.google.api.v2.GateSpecification.PhasedXZH\x00\x12I\n\x0cvirtual_zpow\x18\x07 \x01(\x0b\x32\x31.cirq.google.api.v2.GateSpecification.VirtualZPowH\x00\x12K\n\rphysical_zpow\x18\x08 \x01(\x0b\x32\x32.cirq.google.api.v2.GateSpecification.PhysicalZPowH\x00\x12K\n\rcoupler_pulse\x18\t \x01(\x0b\x32\x32.cirq.google.api.v2.GateSpecification.CouplerPulseH\x00\x12\x41\n\x04meas\x18\n \x01(\x0b\x32\x31.cirq.google.api.v2.GateSpecification.MeasurementH\x00\x12:\n\x04wait\x18\x0b \x01(\x0b\x32*.cirq.google.api.v2.GateSpecification.WaitH\x00\x12\x42\n\x04\x66sim\x18\x0c \x01(\x0b\x32\x32.cirq.google.api.v2.GateSpecification.FSimViaModelH\x00\x1a\n\n\x08Sycamore\x1a\x0b\n\tSqrtISwap\x1a\x0e\n\x0cSqrtISwapInv\x1a\x04\n\x02\x43Z\x1a\n\n\x08PhasedXZ\x1a\r\n\x0bVirtualZPow\x1a\x0e\n\x0cPhysicalZPow\x1a\x0e\n\x0c\x43ouplerPulse\x1a\r\n\x0bMeasurement\x1a\x06\n\x04Wait\x1a\x0e\n\x0c\x46SimViaModelB\x06\n\x04gate\"P\n\x07GateSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\x0bvalid_gates\x18\x02 \x03(\x0b\x32\".cirq.google.api.v2.GateDefinition\"\xa1\x01\n\x0eGateDefinition\x12\n\n\x02id\x18\x01 \x01(\t\x12\x18\n\x10number_of_qubits\x18\x02 \x01(\x05\x12\x35\n\nvalid_args\x18\x03 \x03(\x0b\x32!.cirq.google.api.v2.ArgDefinition\x12\x1b\n\x13gate_duration_picos\x18\x04 \x01(\x03\x12\x15\n\rvalid_targets\x18\x05 \x03(\t\"\xda\x01\n\rArgDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\x04type\x18\x02 \x01(\x0e\x32).cirq.google.api.v2.ArgDefinition.ArgType\x12\x39\n\x0e\x61llowed_ranges\x18\x03 \x03(\x0b\x32!.cirq.google.api.v2.ArgumentRange\"G\n\x07\x41rgType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05\x46LOAT\x10\x01\x12\x14\n\x10REPEATED_BOOLEAN\x10\x02\x12\n\n\x06STRING\x10\x03\"=\n\rArgumentRange\x12\x15\n\rminimum_value\x18\x01 \x01(\x02\x12\x15\n\rmaximum_value\x18\x02 \x01(\x02\"\xef\x01\n\tTargetSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x45\n\x0ftarget_ordering\x18\x02 \x01(\x0e\x32,.cirq.google.api.v2.TargetSet.TargetOrdering\x12+\n\x07targets\x18\x03 \x03(\x0b\x32\x1a.cirq.google.api.v2.Target\"`\n\x0eTargetOrdering\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tSYMMETRIC\x10\x01\x12\x12\n\nASYMMETRIC\x10\x02\x1a\x02\x08\x01\x12\x1a\n\x12SUBSET_PERMUTATION\x10\x03\x1a\x02\x08\x01\"\x15\n\x06Target\x12\x0b\n\x03ids\x18\x01 \x03(\tB.\n\x1d\x63om.google.cirq.google.api.v2B\x0b\x44\x65viceProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cirq_google.api.v2.device_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.google.cirq.google.api.v2B\013DeviceProtoP\001'
  _DEVICESPECIFICATION.fields_by_name['valid_gate_sets']._options = None
  _DEVICESPECIFICATION.fields_by_name['valid_gate_sets']._serialized_options = b'\030\001'
  _TARGETSET_TARGETORDERING.values_by_name["ASYMMETRIC"]._options = None
  _TARGETSET_TARGETORDERING.values_by_name["ASYMMETRIC"]._serialized_options = b'\010\001'
  _TARGETSET_TARGETORDERING.values_by_name["SUBSET_PERMUTATION"]._options = None
  _TARGETSET_TARGETORDERING.values_by_name["SUBSET_PERMUTATION"]._serialized_options = b'\010\001'
  _globals['_DEVICESPECIFICATION']._serialized_start=56
  _globals['_DEVICESPECIFICATION']._serialized_end=306
  _globals['_GATESPECIFICATION']._serialized_start=309
  _globals['_GATESPECIFICATION']._serialized_end=1271
  _globals['_GATESPECIFICATION_SYCAMORE']._serialized_start=1120
  _globals['_GATESPECIFICATION_SYCAMORE']._serialized_end=1130
  _globals['_GATESPECIFICATION_SQRTISWAP']._serialized_start=1132
  _globals['_GATESPECIFICATION_SQRTISWAP']._serialized_end=1143
  _globals['_GATESPECIFICATION_SQRTISWAPINV']._serialized_start=1145
  _globals['_GATESPECIFICATION_SQRTISWAPINV']._serialized_end=1159
  _globals['_GATESPECIFICATION_CZ']._serialized_start=1161
  _globals['_GATESPECIFICATION_CZ']._serialized_end=1165
  _globals['_GATESPECIFICATION_PHASEDXZ']._serialized_start=1167
  _globals['_GATESPECIFICATION_PHASEDXZ']._serialized_end=1177
  _globals['_GATESPECIFICATION_VIRTUALZPOW']._serialized_start=1179
  _globals['_GATESPECIFICATION_VIRTUALZPOW']._serialized_end=1192
  _globals['_GATESPECIFICATION_PHYSICALZPOW']._serialized_start=1194
  _globals['_GATESPECIFICATION_PHYSICALZPOW']._serialized_end=1208
  _globals['_GATESPECIFICATION_COUPLERPULSE']._serialized_start=1210
  _globals['_GATESPECIFICATION_COUPLERPULSE']._serialized_end=1224
  _globals['_GATESPECIFICATION_MEASUREMENT']._serialized_start=1226
  _globals['_GATESPECIFICATION_MEASUREMENT']._serialized_end=1239
  _globals['_GATESPECIFICATION_WAIT']._serialized_start=1241
  _globals['_GATESPECIFICATION_WAIT']._serialized_end=1247
  _globals['_GATESPECIFICATION_FSIMVIAMODEL']._serialized_start=1249
  _globals['_GATESPECIFICATION_FSIMVIAMODEL']._serialized_end=1263
  _globals['_GATESET']._serialized_start=1273
  _globals['_GATESET']._serialized_end=1353
  _globals['_GATEDEFINITION']._serialized_start=1356
  _globals['_GATEDEFINITION']._serialized_end=1517
  _globals['_ARGDEFINITION']._serialized_start=1520
  _globals['_ARGDEFINITION']._serialized_end=1738
  _globals['_ARGDEFINITION_ARGTYPE']._serialized_start=1667
  _globals['_ARGDEFINITION_ARGTYPE']._serialized_end=1738
  _globals['_ARGUMENTRANGE']._serialized_start=1740
  _globals['_ARGUMENTRANGE']._serialized_end=1801
  _globals['_TARGETSET']._serialized_start=1804
  _globals['_TARGETSET']._serialized_end=2043
  _globals['_TARGETSET_TARGETORDERING']._serialized_start=1947
  _globals['_TARGETSET_TARGETORDERING']._serialized_end=2043
  _globals['_TARGET']._serialized_start=2045
  _globals['_TARGET']._serialized_end=2066
# @@protoc_insertion_point(module_scope)
