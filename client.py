import grpc 
import greeter_pb2
import greeter_pb2_grpc 

def run():
    # [+] Nos conectamos al server
    channel = grpc.insecure_channel("localhost:50051")
    stub = greeter_pb2_grpc.GreeterStub(channel)
    
    # [+] Llamamos al método remoto 
    response = stub.SayHello(greeter_pb2.HelloRequest(name="Chris"))
    print("Respuesta del servidor", response.message)

    
if __name__ == '__main__':
    run()