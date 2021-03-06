# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import simple_calculate_pb2 as simple__calculate__pb2


class SimpleRpcServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Calculate = channel.unary_unary(
        '/SimpleRpcServer/Calculate',
        request_serializer=simple__calculate__pb2.Work.SerializeToString,
        response_deserializer=simple__calculate__pb2.Result.FromString,
        )
    self.GetSubjectQuestionTypes = channel.unary_stream(
        '/SimpleRpcServer/GetSubjectQuestionTypes',
        request_serializer=simple__calculate__pb2.Subject.SerializeToString,
        response_deserializer=simple__calculate__pb2.QuestionType.FromString,
        )
    self.Accumulate = channel.stream_unary(
        '/SimpleRpcServer/Accumulate',
        request_serializer=simple__calculate__pb2.Delta.SerializeToString,
        response_deserializer=simple__calculate__pb2.Sum.FromString,
        )
    self.GuessNumber = channel.stream_stream(
        '/SimpleRpcServer/GuessNumber',
        request_serializer=simple__calculate__pb2.Number.SerializeToString,
        response_deserializer=simple__calculate__pb2.Answer.FromString,
        )


class SimpleRpcServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Calculate(self, request, context):
    """unary rpc
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSubjectQuestionTypes(self, request, context):
    """server streaming rpc
    客户端发送学科，服务端多次返回该学科包含的题型
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Accumulate(self, request_iterator, context):
    """client streaming rpc
    客户端多次发送累加值，服务端返回最终的累计和
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GuessNumber(self, request_iterator, context):
    """bidirectional streaming rpc
    客户端多次发送猜的数字，对于猜中的数字，服务端返回，否则不返回
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimpleRpcServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Calculate': grpc.unary_unary_rpc_method_handler(
          servicer.Calculate,
          request_deserializer=simple__calculate__pb2.Work.FromString,
          response_serializer=simple__calculate__pb2.Result.SerializeToString,
      ),
      'GetSubjectQuestionTypes': grpc.unary_stream_rpc_method_handler(
          servicer.GetSubjectQuestionTypes,
          request_deserializer=simple__calculate__pb2.Subject.FromString,
          response_serializer=simple__calculate__pb2.QuestionType.SerializeToString,
      ),
      'Accumulate': grpc.stream_unary_rpc_method_handler(
          servicer.Accumulate,
          request_deserializer=simple__calculate__pb2.Delta.FromString,
          response_serializer=simple__calculate__pb2.Sum.SerializeToString,
      ),
      'GuessNumber': grpc.stream_stream_rpc_method_handler(
          servicer.GuessNumber,
          request_deserializer=simple__calculate__pb2.Number.FromString,
          response_serializer=simple__calculate__pb2.Answer.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SimpleRpcServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
