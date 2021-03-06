# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bees.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bees.proto',
  package='app',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbees.proto\x12\x03\x61pp\"\x19\n\tInputWord\x12\x0c\n\x04word\x18\x01 \x01(\t\"\x1b\n\nWordInDict\x12\r\n\x05\x65xist\x18\x01 \x01(\x08\x32\x36\n\x04\x42\x65\x65s\x12.\n\tCheckWord\x12\x0e.app.InputWord\x1a\x0f.app.WordInDict\"\x00\x62\x06proto3'
)




_INPUTWORD = _descriptor.Descriptor(
  name='InputWord',
  full_name='app.InputWord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='app.InputWord.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=44,
)


_WORDINDICT = _descriptor.Descriptor(
  name='WordInDict',
  full_name='app.WordInDict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exist', full_name='app.WordInDict.exist', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['InputWord'] = _INPUTWORD
DESCRIPTOR.message_types_by_name['WordInDict'] = _WORDINDICT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputWord = _reflection.GeneratedProtocolMessageType('InputWord', (_message.Message,), {
  'DESCRIPTOR' : _INPUTWORD,
  '__module__' : 'bees_pb2'
  # @@protoc_insertion_point(class_scope:app.InputWord)
  })
_sym_db.RegisterMessage(InputWord)

WordInDict = _reflection.GeneratedProtocolMessageType('WordInDict', (_message.Message,), {
  'DESCRIPTOR' : _WORDINDICT,
  '__module__' : 'bees_pb2'
  # @@protoc_insertion_point(class_scope:app.WordInDict)
  })
_sym_db.RegisterMessage(WordInDict)



_BEES = _descriptor.ServiceDescriptor(
  name='Bees',
  full_name='app.Bees',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=75,
  serialized_end=129,
  methods=[
  _descriptor.MethodDescriptor(
    name='CheckWord',
    full_name='app.Bees.CheckWord',
    index=0,
    containing_service=None,
    input_type=_INPUTWORD,
    output_type=_WORDINDICT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BEES)

DESCRIPTOR.services_by_name['Bees'] = _BEES

# @@protoc_insertion_point(module_scope)
