import grpc
from . import health_check_service_pb2
from . import health_check_service_pb2_grpc 

def check_health(server_address):
    # Create a gRPC channel
    channel = grpc.insecure_channel(server_address)

    # Create a stub (client)
    stub = health_check_service_pb2_grpc.HealthCheckServiceStub(channel)

    # Create a request
    request = health_check_service_pb2.HealthCheckRequest()

    # Call the RPC
    response = stub.Check(request)

    return response.status, response.message

if __name__ == '__main__':
    server_address = 'localhost:50051'  # Adjust the address to match your server
    status, message = check_health(server_address)
    print(f"Health check status: {status}, message: {message}")
