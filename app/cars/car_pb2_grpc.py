# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import car_pb2 as car__pb2


class CarStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchByID = channel.unary_unary(
                '/Car/SearchByID',
                request_serializer=car__pb2.CarRequestID.SerializeToString,
                response_deserializer=car__pb2.CarDataResponse.FromString,
                )
        self.GetCarDataList = channel.unary_unary(
                '/Car/GetCarDataList',
                request_serializer=car__pb2.CarRequest.SerializeToString,
                response_deserializer=car__pb2.CarDataList.FromString,
                )
        self.SearchByManufacturer = channel.unary_unary(
                '/Car/SearchByManufacturer',
                request_serializer=car__pb2.SearchByManufacturerRequest.SerializeToString,
                response_deserializer=car__pb2.CarDataList.FromString,
                )
        self.SearchByCondition = channel.unary_unary(
                '/Car/SearchByCondition',
                request_serializer=car__pb2.SearchByConditionRequest.SerializeToString,
                response_deserializer=car__pb2.CarDataList.FromString,
                )
        self.SearchByYear = channel.unary_unary(
                '/Car/SearchByYear',
                request_serializer=car__pb2.SearchByYearRequest.SerializeToString,
                response_deserializer=car__pb2.CarDataList.FromString,
                )
        self.SearchByModel = channel.unary_unary(
                '/Car/SearchByModel',
                request_serializer=car__pb2.SearchByModelRequest.SerializeToString,
                response_deserializer=car__pb2.CarDataList.FromString,
                )
        self.SearchByRegion = channel.unary_unary(
                '/Car/SearchByRegion',
                request_serializer=car__pb2.SearchByRegionRequest.SerializeToString,
                response_deserializer=car__pb2.CarDataList.FromString,
                )


class CarServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SearchByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCarDataList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByManufacturer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByCondition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByYear(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByRegion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CarServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchByID': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByID,
                    request_deserializer=car__pb2.CarRequestID.FromString,
                    response_serializer=car__pb2.CarDataResponse.SerializeToString,
            ),
            'GetCarDataList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCarDataList,
                    request_deserializer=car__pb2.CarRequest.FromString,
                    response_serializer=car__pb2.CarDataList.SerializeToString,
            ),
            'SearchByManufacturer': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByManufacturer,
                    request_deserializer=car__pb2.SearchByManufacturerRequest.FromString,
                    response_serializer=car__pb2.CarDataList.SerializeToString,
            ),
            'SearchByCondition': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByCondition,
                    request_deserializer=car__pb2.SearchByConditionRequest.FromString,
                    response_serializer=car__pb2.CarDataList.SerializeToString,
            ),
            'SearchByYear': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByYear,
                    request_deserializer=car__pb2.SearchByYearRequest.FromString,
                    response_serializer=car__pb2.CarDataList.SerializeToString,
            ),
            'SearchByModel': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByModel,
                    request_deserializer=car__pb2.SearchByModelRequest.FromString,
                    response_serializer=car__pb2.CarDataList.SerializeToString,
            ),
            'SearchByRegion': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByRegion,
                    request_deserializer=car__pb2.SearchByRegionRequest.FromString,
                    response_serializer=car__pb2.CarDataList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Car', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Car(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SearchByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Car/SearchByID',
            car__pb2.CarRequestID.SerializeToString,
            car__pb2.CarDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCarDataList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Car/GetCarDataList',
            car__pb2.CarRequest.SerializeToString,
            car__pb2.CarDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchByManufacturer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Car/SearchByManufacturer',
            car__pb2.SearchByManufacturerRequest.SerializeToString,
            car__pb2.CarDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchByCondition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Car/SearchByCondition',
            car__pb2.SearchByConditionRequest.SerializeToString,
            car__pb2.CarDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchByYear(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Car/SearchByYear',
            car__pb2.SearchByYearRequest.SerializeToString,
            car__pb2.CarDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchByModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Car/SearchByModel',
            car__pb2.SearchByModelRequest.SerializeToString,
            car__pb2.CarDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchByRegion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Car/SearchByRegion',
            car__pb2.SearchByRegionRequest.SerializeToString,
            car__pb2.CarDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
