# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: health_check_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ahealth_check_service.proto\x12\x0chealth_check\"\x14\n\x12HealthCheckRequest\"6\n\x13HealthCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2d\n\x12HealthCheckService\x12N\n\x05\x43heck\x12 .health_check.HealthCheckRequest\x1a!.health_check.HealthCheckResponse\"\x00\x42-Z+internal/services/health_check;health_checkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'health_check_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+internal/services/health_check;health_check'
  _globals['_HEALTHCHECKREQUEST']._serialized_start=44
  _globals['_HEALTHCHECKREQUEST']._serialized_end=64
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=66
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=120
  _globals['_HEALTHCHECKSERVICE']._serialized_start=122
  _globals['_HEALTHCHECKSERVICE']._serialized_end=222
# @@protoc_insertion_point(module_scope)
